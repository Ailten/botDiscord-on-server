from flask import Flask, request
import asyncio

class Http():

    def __init__(self, bot, port :str):
        self.app = Flask(__name__)
        print(self.app)
        asyncio.run(self.app.run(host="127.0.0.1", port=port))

        self.bot = bot
        

    @self.app.route('/event/sayInChannelDiscord', methods=['POST'])
    async def handleEvent():
        data = request.json # get package from event.

        # do.
        self.bot.sayInChannel(data["channelName"], data["message"])

        return '', 200
    