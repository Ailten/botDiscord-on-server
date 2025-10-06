#from flask import Flask, request
#import asyncio

#class Http():
#
#    def __init__(self, bot, port :str):
#        self.app = Flask(__name__)
#        asyncio.run(self.app.run(host="127.0.0.1", port=port))
#
#        self.bot = bot
#        
#
#    @app.route('/event/sayInChannelDiscord', methods=['POST'])
#    async def handleEvent():
#        data = request.json # get package from event.
#
#        # do.
#        self.bot.sayInChannel(data["channelName"], data["message"])
#
#        return '', 200

from flask import Flask, request # Doc : https://www.geeksforgeeks.org/python/python-introduction-to-web-development-using-flask/
import asyncio
app = Flask(__name__)
bot = None

# ---------->

@app.route('/event/sayInChannelDiscord', methods=['POST'])
def handleEvent():
    data = request.json # get package from event.

    # do.
    bot.sayInChannel(data["channelName"], data["message"])

    return '', 200

# ---------->

def runFlask(botRef, port :int):
    bot = botRef
    asyncio.run(app.run(host="127.0.0.1", port=port))
    