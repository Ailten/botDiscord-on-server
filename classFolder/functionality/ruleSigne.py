import discord

async def ruleSigne(bot, payload):

    # verify if is the message "reglement".
    if payload.message_id != 1420025908000985162:
        return

    # verify if is the channel "reglement".
    if payload.channel_id != 1420019325368012961:
        return

    # verify if is the discord server "Ailten".
    if payload.guild_id != 1099296948974006302:
        return

    # verify if is the right emoji.
    if payload.emoji.name != "✅":
        return

    # verify if the user has already the role.
    nameRoles = map(lambda r: r.name, payload.member.roles)
    if "rule-reader" in nameRoles:
        return

    # add role "rule-reader" to the member.
    roleRuleReader = discord.Object(id=1223358254852083749, type=type(discord.Role))
    await payload.member.add_roles(roleRuleReader, reason="signe the rules.")
