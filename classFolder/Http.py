from flask import Flask, request

class Http():

    def __init__(self, bot, port :str):
        self.app = Flask(__name__)
        self.app.run(host="127.0.0.1", port=port)

        self.bot = bot
        

    @app.route('/event/sayInChannelDiscord', methods=['POST'])
    async def handleEvent():
        data = request.json # get package from event.

        # do.
        self.bot.sayInChannel(data["channelName"], data["message"])

        return '', 200
    