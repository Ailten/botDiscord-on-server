import discord

class AddSubRoleFromReaction():

    # constructor.
    def __init__(self, bot, messageKey: str, roleKey :str, channelKey="roles", guildKey="Ailten", emojiName="✅"):

        # set parameters.
        self.messageKey = messageKey
        self.roleKey = roleKey
        self.channelKey = channelKey
        self.guildKey = guildKey
        self.emojiName = emojiName

        self.role = discord.Object(id=bot.idRole[self.roleKey], type=type(discord.Role))

        self.isUseOnEvent = [
            "on_raw_reaction_add",
            "on_raw_reaction_remove"
        ]


    # ----------> function when add or remove reaction.

    async def addReaction(self, bot, payload):
        await self.addRemoveReaction(bot, payload, isAdd=True)

    async def removeReaction(self, bot, payload):
        await self.addRemoveReaction(bot, payload, isAdd=False)
    
    async def addRemoveReaction(self, bot, payload, isAdd: bool):
        member = await self.getMember(bot, payload)
        isMemberHasTheRole = self.isMemberHasTheRole(bot, member)

        if isAdd and not isMemberHasTheRole: # do add.
            await member.add_roles(self.role, reason="signe for the role.")
        elif not isAdd and isMemberHasTheRole: # do remove.
            await member.remove_roles(self.role, reason="un-signe for the role.")


    # ----------> function get elements.

    async def getMember(self, bot, payload) -> discord.Member:
        return payload.member or await bot.getMemberFromId(payload.user_id)


    # ----------> function verification.

    def isOnRightMessage(self, bot, payload) -> bool:
        return payload.message_id == bot.idMessages[self.messageKey]

    def isOnRightChannel(self, bot, payload) -> bool:
        return payload.channel_id == bot.idChannel[self.channelKey]

    def isOnRightGuild(self, bot, payload) -> bool:
        return payload.guild_id == bot.idGuild[self.guildKey]

    def isRightEmoji(self, bot, payload) -> bool:
        return payload.emoji.name == self.emojiName
    
    def isMemberHasTheRole(self, bot, member) -> bool:
        return bot.idRole[self.roleKey] in map(lambda r: r.id, member.roles)

    def isFullCheck(self, bot, payload) -> bool:
        return (
            self.isOnRightMessage(bot, payload) and
            self.isOnRightChannel(bot, payload) and
            self.isOnRightGuild(bot, payload) and
            self.isRightEmoji(bot, payload)
        )