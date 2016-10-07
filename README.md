# Wumpi Discord Bot
This is my kinda pointless Discord bot!

# Getting setup.

First, you'll need python3.5
You can download this from python.org or search for how to install python3.5 on your OS.

Next, you'll need DiscordPy, at the time of writing this I have no voice commands, but I may add them in the future. Just incase, the following command install the required files for DiscordPyVoice

Run this command to setup DiscordPY.

```
pip3 install --upgrade discord.py[voice]
```
If you're reading this in the future.. (hey future) but please go to the Discord API server and type
```
?tag update
```
R.Danny will get your the latest install instructions.
# Getting your token
Head to https://discordapp.com/developers/applications/me and create a new app, name it, give it a snazzy logo and then click create bot user. Say yes to the warning.

Then grab the token. Keep it for later.

# Configuring the bot.

Open main.py in your editor of choice
Find the 'admins = []' line, it's right at the top. 

Add your userID and anyone else's ID you want to have control of the most powerful commands of the bot. (Comma seperated)
Example:
```
admins = ["12812333387814145", "12812834653894573445"]
```
Now, find the 'token = ""' line and chuck in your token.
Exmaple:
```
token = "MjMzNjEwOTc2Nzc4MjU2Mzg0.CtmRpA.nnyE9c-Zeq365XWHcw"
```
(No that token doesn't exist. It's actually too small.)

# Starting the bot.

Exit (oh, and save) main.py.

Now (on Linux) run:
```
python3.5 main.py
```
On Windows, just run it.

Rightio. Any problems submit them as issues, or ask in the Discord API Python, mention me, my name is: @Nevexo#3876.
kthxbye.
