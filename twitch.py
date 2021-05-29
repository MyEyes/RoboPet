import sys
import irc.bot
import requests

from locomotion import Locomotion
import time
import config
from sensor import Sensor

from twitchio.ext import commands

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

def do_command(cmd):
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

@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    if ctx.content[:1] == '!':
        do_command(ctx.content[1:])

if __name__ == "__main__":
    bot.run()