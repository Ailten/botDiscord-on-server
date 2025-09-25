import discord

async def addSubRoleArt(bot, payload, isAdd: bool):

    # verify if is the right message.
    if payload.message_id != bot.idMessages["role-art"]:
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
    isMemberHasTheRole = "art" in map(lambda r: r.name, member.roles)

    # add or remove role.
    roleArt = discord.Object(id=bot.idRole["art"], type=type(discord.Role))
    if isAdd and not isMemberHasTheRole: # do add.

        await member.add_roles(roleArt, reason="signe for the role.")

    elif not isAdd and isMemberHasTheRole: # do remove.

        await member.remove_roles(roleArt, reason="un-signe for the role.")

    
    
