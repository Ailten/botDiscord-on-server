from flask import Flask, request
from classFolder.DiscordBot import DiscordBot

class Http():
    app: None #flask.

    exchangePort = {
        "botTwitch": "5000" # "botTwitch - botDiscord" == 5000
    }

    @staticmethod
    def startFlask():
        Http.app = Flask(__name__)
        Http.app.run(host="127.0.0.1", port="5000")


    @staticmethod
    @app.route('/event', methods=['POST'])
    async def handleEvent():
        data = request.json # get package from event.
        bot = DiscordBot.currentBot # get bot discord.

        if data["event"] == "sayInChannel":
            bot.sayInChannel(data["channelName"], data["message"])

        return '', 200
    