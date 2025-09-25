import discord

async def addSubRoleCode(bot, payload, isAdd: bool):

    # verify if is the right message.
    if payload.message_id != bot.idMessages["role-code"]:
        return

    # verify if is the right channem.
    if payload.channel_id != bot.idChannel["roles"]:
        return

    # verify if is the discord server "Ailten".
    if payload.guild_id != bot.idGuild["Ailten"]:
        return

    # verify if is the right emoji.
    if payload.emoji.name != "✅":
        return

    # get member.
    member = payload.member or await bot.getMemberFromId(payload.user_id)

    # verify if the user has already the role.
    isMemberHasTheRole = "code" in map(lambda r: r.name, member.roles)

    # add or remove role.
    roleCode = discord.Object(id=bot.idRole["code"], type=type(discord.Role))
    if isAdd and not isMemberHasTheRole: # do add.

        await member.add_roles(roleCode, reason="signe for the role.")

    elif not isAdd and isMemberHasTheRole: # do remove.

        await member.remove_roles(roleCode, reason="un-signe for the role.")

    
    
