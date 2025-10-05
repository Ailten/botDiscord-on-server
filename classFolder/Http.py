from flask import Flask, request
from classFolder.DiscordBot import DiscordBot

class Http():
    app: None #flask.

    @staticmethod
    def startFlask():
        Http.app = Flask(__name__)
        Http.app.run(host="127.0.0.1", port="5000")


    @staticmethod
    @app.route('/event/sayInChannelDiscord', methods=['POST'])
    async def handleEvent():
        data = request.json # get package from event.
        bot = DiscordBot.currentBot # get bot discord.

        # do.
        bot.sayInChannel(data["channelName"], data["message"])

        return '', 200
    