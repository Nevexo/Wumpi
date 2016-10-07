import discord
import asyncio
import time
import random
admins = []
def admin(message):
    if message.author.id in admins:
        return True
    else:
        return False
version = "0.2 Beta Flight"
build = "15"
token = ''
client = discord.Client()
print("Getting ready. GET DAT WUMPI")
def getUptime():
    global startTime
    """
    Returns the number of seconds since the program started.
    """

    upsec = round(time.time() - startTime)
    m, s = divmod(upsec, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)
@client.event
async def on_ready():
    print("Running")
    global startTime
    startTime = time.time()
    await client.change_presence(game=discord.Game(name="github.com/nevexo kthx"))
@client.event
async def on_message(message):
    if message.content.startswith("~duh"):
        await client.send_message(message.channel, ":poop: - Asian confuseush. ")
    if message.content.startswith("~die"):
        if admin(message):
            await client.send_message(message.channel, "kthxbye")
            await client.logout()
    if message.content.startswith("~help"):
        await client.send_message(message.channel, "```simon says <message> - **Says what ever you placed in the place holder <message>**```")
    if message.tts:
        print("Pooshush.")
        if message.server.id == "220231489437040641":
            alertID = random.randint(1, 13456765024576)
            print(alertID)
            await client.send_message(message.channel, ":poop: Don't use TTS. [Warning: " + str(alertID) + "]")
            await client.send_message(discord.Object(id="233645463314759680"), "```Alert ID: " + str(alertID) + "\nAlerted user: @" + message.author.name + "\nWarning reason: Used TTS. Like pls. Kthx.```")
        else:
            await client.send_message(message.channel, ":poop: - Com'on. TTS really?")
    if message.content.startswith("simon says"):
        await client.send_message(message.channel, message.content[10:])
    if message.content.startswith("~dot"):
        if message.author.id in admins:
            if message.content[5:] == "online":
                await client.change_presence(status=None)
                await client.send_message(message.channel, ":ok:")
            elif message.content[5:] == "dnd":
                await client.change_presence(status=discord.Status.dnd)
                await client.send_message(message.channel, ":ok:")
            elif message.content[5:] == "ninja":
                await client.change_presence(status=discord.Status.invisible)
                await client.send_message(message.channel, ":ok:")
            else:
                await client.send_message(message.channel, ":no_entry: - Whaaaat. U havin a laugh?")
        else:
            await client.send_message(":no_entry: - no perms 4 u.")
    if message.content.startswith("~status"):
        if message.author.id in admins:
            await client.change_presence(game=discord.Game(name=message.content[7:]))
            await client.send_message(message.channel, ":white_check_mark: - All done kthx")
        else:
            await client.send_message(message.channel, ":no_entry: - U got no perms. kthxbye")

    if message.content.startswith("~servers"):
        if admin(message):
            servers = list(client.servers)
            listsrv = []
            for i in servers:
                listsrv.append(i.name)
                listsrv.append(i.id)
            await client.send_message(message.channel, "```[servername, serverid] \n " + str(listsrv) + "```")
    if message.content.startswith("~invite"):
        if admin(message):
            temp = await client.send_message(message.author, ":clock3: Creating invite for: " + message.content[8:] + ".")
            try:
                id = message.content[8:]
                print("Making invite for " + id)
                invite = await client.create_invite(discord.Object(id), max_uses=2, temporary=True, max_age=300000)
                print("Created invite: " + str(invite))
                await client.edit_message(temp, ":white_check_mark: Created invite for: " + message.content[11:] + ", valid for 5 minutes: " + str(invite))
            except:
                await client.edit_message(temp, ":no_entry: Failed to create invite.")

    if message.content.startswith('~info'):
        count = str(len(client.servers))
        await client.send_message(message.channel, "```Bot uptime: " + getUptime() + "``` ```python\nBot Developer: Nevexo\nBot version: " + version + "\nBot build: " + build + "\nServer count: " + count +"\nGithub: https://github.com/Nevexo/Wumpi```")
    if message.content.startswith('~updateimage'):
        print("Updating image now...")
        if message.author.id == "101742709093445632":
            print(message.content[13:])
            if message.content[13:] == "SEALO":
                file = "seal.png"
            else:
                file = "logo.png"
            print("Updating profile image...")
            logo = open(file,"rb")
            msg = await client.send_message(message.channel, ":clock1: - Processing image from assets server...")
            await client.edit_profile(avatar=logo.read())
            await client.edit_message(msg, ":white_check_mark: - Updated image!")
def run():
    client.run(token)
run()
