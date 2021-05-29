import sys
import irc.bot
import requests

from locomotion import Locomotion
import time
import config
from sensor import Sensor

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
        

    def on_welcome(self, c, e):

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0][1:]
            self.do_command(e, cmd)
        return

    def do_command(self, e, cmd):
        c = self.connection
        data = cmd
        for c in cmd:
            if 'w' == c:
                loco.forward()
            if 'a' == c:
                loco.tightLeft()
            if 'd' == c:
                loco.tightRight()
            if 's' == c:
                loco.backward()
            if 'm' == c:
                print(sense.measure())
            time.sleep(0.1)
            loco.stop()

def main():
    if len(sys.argv) != 5:
        print("Usage: twitchbot <username> <client id> <token> <channel>")
        sys.exit(1)

    username  = sys.argv[1]
    client_id = sys.argv[2]
    token     = sys.argv[3]
    channel   = sys.argv[4]

    bot = TwitchBot(username, client_id, token, channel)
    bot.start()

if __name__ == "__main__":
    main()