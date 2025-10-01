import discord #pip install -U discord.py
from classFolder.Json import Json
import pathlib

# importe functionality.
from classFolder.functionality.AddRoleFromReaction import AddRoleFromReaction
from classFolder.functionality.AddSubRoleFromReaction import AddSubRoleFromReaction

# Doc : https://realpython.com/how-to-make-a-discord-bot-python/
# Doc (event message) : https://docs.pycord.dev/en/master/api/events.html#discord.on_message

class DiscordBot(discord.Client):

    # constructor.
    def __init__(self):

        # set path folder.
        self.pathFolder = pathlib.Path(__file__).parent.parent.resolve()
        self.pathToken = f"{self.pathFolder}/json/tokenDiscord.json"

        # set dictionary ID.
        self.idMessages = {
            "rules": 1420025908000985162,
            "role-nsfw": 1420428198331809984,
            "role-art": 1420742218762948608,
            "role-code": 1420742661673058356,
            "role-ping-stream": 1422960746966417448
        }
        self.idChannel = {
            "règlement": 1420019325368012961,
            "roles": 1420425489444507761
        }
        self.idGuild = {
            "Ailten": 1099296948974006302
        }
        self.idRole = {
            "rule-reader": 1223358254852083749,
            "nsfw": 1420427253946388572,
            "art": 1420741388445810849,
            "code": 1420741549389647952,
            "ping-stream": 1422958935668818112
        }

        # get functionality class.
        self.functionality = [
            AddRoleFromReaction(bot=self, messageKey="rules", roleKey="rule-reader", channelKey="règlement"),
            AddSubRoleFromReaction(bot=self, messageKey="role-nsfw", roleKey="nsfw"),
            AddSubRoleFromReaction(bot=self, messageKey="role-art", roleKey="art"),
            AddSubRoleFromReaction(bot=self, messageKey="role-code", roleKey="code"),
            AddSubRoleFromReaction(bot=self, messageKey="role-ping-stream", roleKey="ping-stream")
        ]

        # build intents (permission of bot).
        #intents = discord.Intents.all()

        # proper way to do it. Doc : https://discordpy.readthedocs.io/en/stable/api.html#intents
        intents = discord.Intents.default() # Discord portail dev bot : https://discord.com/developers/applications -> installation
        intents.message_content = True # for allow to read content message.
        intents.guild_reactions = True # for allow to read reactions (on guilds).
        intents.reactions = True # for allow to read reactions.

        # init the bot (parent).
        super().__init__(intents=intents)

    # overide run methode.
    def run(self):
        tokenDiscord = self.getTokenObj()["bot"]["loginToken"]
        super().run(tokenDiscord)

    # ---------> event discord bot (lib).

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
        if message.content.lower() == "!hello": # cmd !hello.
            await message.channel.send("Hello !")

    # event reaction, call when a user add a reaction in a message.
    async def on_raw_reaction_add(self, payload): # https://docs.pycord.dev/en/master/api/events.html#discord.on_raw_reaction_add
        for f in self.functionality:
            if not "on_raw_reaction_add" in f.isUseOnEvent:
                continue
            if not f.isFullCheck(self, payload):
                continue
            await f.addReaction(self, payload)

    async def on_raw_reaction_remove(self, payload):
        for f in self.functionality:
            if not "on_raw_reaction_remove" in f.isUseOnEvent:
                continue
            if not f.isFullCheck(self, payload):
                continue
            await f.removeReaction(self, payload)


    # ---------> additional self function.

    # function return object json token.
    def getTokenObj(self):
        return Json.read(self.pathToken)

    # functon to get member from id member (need also guild name).
    async def getMemberFromId(self, idMember, guildName="Ailten"):
        guild = discord.utils.find(lambda g : g.id == self.idGuild[guildName], self.guilds)
        member = await guild.fetch_member(idMember)
        return member

