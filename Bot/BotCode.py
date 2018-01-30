import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = ":")

@client.event
async def on_ready():
    print("Bot is running! GG")

@client.event
async def on_message(message):
    if message.content.upper().startswith(":OWNER"):
        userID = message.author.id
        server_owner = discord.utils.get()
        await client.send_message(message.channel, "<@%s> the Owner is MrRos" % (userID))
    if message.content.upper().startswith(":ANNOUNCE"):
        role = discord.utils.get(message.server.roles,name="Announcer")
        if role.id in [role.id for role in message.author.roles]:
            userID = message.author.id
            
            args = message.content.split(" ")
            channel = discord.utils.get(message.server.channels, name='announcements', type=discord.ChannelType.text)
            await client.send_message(client.get_channel(channel.id), "%s" % (" ".join(args[1:])))
            UserMsg = " ".join(args[1:])
            embed=discord.Embed(title="Msg sent", description="Your message was successfully sent", color=0x06ce97)
            embed.set_author(name="CraftOLeague", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
            embed.add_field(name="Message:", value=UserMsg, inline=False)
            await client.send_message(message.channel, embed=embed)
            
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> you do not have permission to use this command :)" % (userID))
    if message.content.upper().startswith(":HELP"):
        embed=discord.Embed(title="Help", description="Display all the commands", color=0x06ce97)
        embed.set_author(name="CraftOLeague", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
        #embed.add_field(name=":owner", value="Displays the Owner of the server", inline=False)
        embed.add_field(name=":annouce [msg]", value="Announces [msg] in the announcements channel (Only for @Announcer role)", inline=False)
        embed.add_field(name=":cmembers", value="Counts all the members in the server", inline=False)
        embed.add_field(name=":nick [nickname]", value="Set your nickname to [nickname]", inline=False)
        embed.add_field(name=":binfo", value="Displays some bot info", inline=False)
        await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith(":NICK"):
        args = message.content.split(" ")
        await client.change_nickname(message.author, " ".join(args[1:]))
    if message.content.upper().startswith(":CMEMBERS"):
        memberCount = 0
        x = message.server.members
        for member in x:
            memberCount = memberCount + 1
        await client.send_message(message.author, "There are %s members in your server(I am counting the bots too)" % (memberCount))
    if message.content.upper().startswith(":BINFO"):
        embed=discord.Embed(title="Bot Info", description="Some information about the bot", color=0x7d7d7d)
        embed.set_author(name="CraftOLeague", url="https://discord.gg/gFuac2r", icon_url="https://stavzog.github.io/craftoleague/McAvatar.png")
        embed.add_field(name="Creator:", value="The creator of the bot is <@398580757335113739>", inline=False)
        embed.add_field(name="Made for:", value="The bot was originally made for a discord server called Craft O' League", inline=False)
        embed.set_footer(text="Copyright Craft O' League")
        await client.send_message(message.channel, embed=embed)
    



@client.event
async def on_member_join(member):
    await client.change_nickname(member, "[Member]%s" % (member.name))





client.run("NDA2NzYwMDIwNDUwMDgyODM2.DU3q4A.8XrAUxZOTF-xB2X7Rv8qetUHb4A")
