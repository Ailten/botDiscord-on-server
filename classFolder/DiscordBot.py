import discord #pip install -U discord.py
from classFolder.Json import Json
import pathlib

# importe functionality.
from classFolder.functionality.ruleSigne import ruleSigne

# Doc : https://realpython.com/how-to-make-a-discord-bot-python/
# Doc (event message) : https://docs.pycord.dev/en/master/api/events.html#discord.on_message

class DiscordBot(discord.Client):

    # constructor.
    def __init__(self):

        # set path folder.
        self.pathFolder = pathlib.Path(__file__).parent.parent.resolve()
        self.pathToken = f"{self.pathFolder}/json/tokenDiscord.json"

        # build intents (permission of bot).
        #intents = discord.Intents.all()

        # proper way to do it. Doc : https://discordpy.readthedocs.io/en/stable/api.html#intents
        intents = discord.Intents.default() # Discord portail dev bot : https://discord.com/developers/applications -> installation
        intents.message_content = True # for allow to read content message.
        intents.guild_reactions = True # for allow to read reactions (on guilds).
        intents.reactions = True # for allow to read reactions.

        #print(vars(discord.Intents))
        #{
        #    '__module__': 'discord.flags', 
        #    '__doc__': "Wraps up a Discord gateway intent flag.\n\n    Similar to :class:`Permissions`\\, the properties provided are two way.\n    You can set and retrieve individual bits using the properties as if they\n    were regular bools.\n\n    To construct an object you can pass keyword arguments denoting the flags\n    to enable or disable.\n\n    This is used to disable certain gateway features that are unnecessary to\n    run your bot. To make use of this, it is passed to the ``intents`` keyword\n    argument of :class:`Client`.\n\n    .. versionadded:: 1.5\n\n    .. container:: operations\n\n        .. describe:: x == y\n\n            Checks if two flags are equal.\n        .. describe:: x != y\n\n            Checks if two flags are not equal.\n\n        .. describe:: x | y, x |= y\n\n            Returns an Intents instance with all enabled flags from\n            both x and y.\n\n            .. versionadded:: 2.0\n\n        .. describe:: x & y, x &= y\n\n            Returns an Intents instance with only flags enabled on\n            both x and y.\n\n            .. versionadded:: 2.0\n\n        .. describe:: x ^ y, x ^= y\n\n            Returns an Intents instance with only flags enabled on\n            only one of x or y, not on both.\n\n            .. versionadded:: 2.0\n\n        .. describe:: ~x\n\n            Returns an Intents instance with all flags inverted from x.\n\n            .. versionadded:: 2.0\n\n        .. describe:: hash(x)\n\n               Return the flag's hash.\n        .. describe:: iter(x)\n\n               Returns an iterator of ``(name, value)`` pairs. This allows it\n               to be, for example, constructed as a dict or a list of pairs.\n\n        .. describe:: bool(b)\n\n            Returns whether any intent is enabled.\n\n            .. versionadded:: 2.0\n\n    Attributes\n    -----------\n    value: :class:`int`\n        The raw value. You should query flags via the properties\n        rather than using this raw value.\n    ", 
        #    '__slots__': (), 
        #    '__init__': <function Intents.__init__ at 0x7f25e0c79090>, 
        #    'all': <classmethod(<function Intents.all at 0x7f25e0c79120>)>, 
        #    'none': <classmethod(<function Intents.none at 0x7f25e0c791b0>)>, 
        #    'default': <classmethod(<function Intents.default at 0x7f25e0c79240>)>, 
        #    'guilds': <flag_value flag=1>, 
        #    'members': <flag_value flag=2>, 
        #    'moderation': <flag_value flag=4>, 
        #    'bans': <flag_value flag=4>, 
        #    'emojis': <flag_value flag=8>, 
        #    'emojis_and_stickers': <flag_value flag=8>, 
        #    'expressions': <flag_value flag=8>, 
        #    'integrations': <flag_value flag=16>, 
        #    'webhooks': <flag_value flag=32>, 
        #    'invites': <flag_value flag=64>, 
        #    'voice_states': <flag_value flag=128>, 
        #    'presences': <flag_value flag=256>, 
        #    'messages': <flag_value flag=4608>, 
        #    'guild_messages': <flag_value flag=512>, 
        #    'dm_messages': <flag_value flag=4096>, 
        #    'reactions': <flag_value flag=9216>, 
        #    'guild_reactions': <flag_value flag=1024>, 
        #    'dm_reactions': <flag_value flag=8192>, 
        #    'typing': <flag_value flag=18432>, 
        #    'guild_typing': <flag_value flag=2048>, 
        #    'dm_typing': <flag_value flag=16384>, 
        #    'message_content': <flag_value flag=32768>, 
        #    'guild_scheduled_events': <flag_value flag=65536>, 
        #    'auto_moderation': <flag_value flag=3145728>, 
        #    'auto_moderation_configuration': <flag_value flag=1048576>, 
        #    'auto_moderation_execution': <flag_value flag=2097152>, 
        #    'polls': <flag_value flag=50331648>, 
        #    'guild_polls': <flag_value flag=16777216>, 
        #    'dm_polls': <flag_value flag=33554432>, 
        #    'VALID_FLAGS': {'guilds': 1, 'members': 2, 'moderation': 4, 'bans': 4, 'emojis': 8, 'emojis_and_stickers': 8, 'expressions': 8, 'integrations': 16, 'webhooks': 32, 'invites': 64, 'voice_states': 128, 'presences': 256, 'messages': 4608, 'guild_messages': 512, 'dm_messages': 4096, 'reactions': 9216, 'guild_reactions': 1024, 'dm_reactions': 8192, 'typing': 18432, 'guild_typing': 2048, 'dm_typing': 16384, 'message_content': 32768, 'guild_scheduled_events': 65536, 'auto_moderation': 3145728, 'auto_moderation_configuration': 1048576, 'auto_moderation_execution': 2097152, 'polls': 50331648, 'guild_polls': 16777216, 'dm_polls': 33554432}, 
        #    'DEFAULT_VALUE': 0
        #}


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
        
        await ruleSigne(self, payload)



    # ---------> additional self function.

    # function return object json token.
    def getTokenObj(self):
        return Json.read(self.pathToken)

