import discord #pip install -U discord.py

# Doc : https://realpython.com/how-to-make-a-discord-bot-python/

class DiscordBot(discord.Client):

    def __init__(self):

        # set path.
        self.pathFolder = pathlib.Path(__file__).parent.parent.resolve()
        self.pathToken = f"{self.pathFolder}/json/tokenDiscord.json"

        # init the bot.
        super().__init__()



    # event ready, call when bot is start running.
    async def on_ready(self):
        print("bot is running.")

    # event join, call when a member join the server.
    async def on_member_join(self, member):
        print(f"{member.name} has join.")

    # event message, call when a message is send on a channel.
    async def on_message(self, message):
        if message.author == self.user: # skill self message.
            return
        if message.content == "!hello": # cmd !hello.
            await message.channel.send("Hello !")

    # function return object json token.
    def getTokenObj(self):
        return json.read(self.pathToken)

    # overide run methode.
    def run(self):
        tokenDiscord = self.getTokenObj()["bot"]["loginToken"]
        super().run(tokenDiscord)

