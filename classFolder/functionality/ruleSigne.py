import discord

async def ruleSigne(bot, payload):

    # verify if is the message "reglement".
    if payload.message_id != bot.idMessages["rules"]:
        return

    # verify if is the channel "reglement".
    if payload.channel_id != bot.idChannel["règlement"]:
        return

    # verify if is the discord server "Ailten".
    if payload.guild_id != bot.idGuild["Ailten"]:
        return

    # verify if is the right emoji.
    if payload.emoji.name != "✅":
        return

    # verify if the user has already the role.
    nameRoles = map(lambda r: r.name, payload.member.roles)
    if "rule-reader" in nameRoles:
        return

    # add role "rule-reader" to the member.
    roleRuleReader = discord.Object(id=bot.idRole["rule-reader"], type=type(discord.Role))
    await payload.member.add_roles(roleRuleReader, reason="signe the rules.")
