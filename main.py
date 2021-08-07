import asyncio

from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from stats import userStats
from embedCreator import createEmbed
from database import addUser, listUsers

userToCheck = []
link = "https://eu01.playuntrusted.com/profile/"

bot = commands.Bot(command_prefix="<", help_command=None)


def checkIfUserExists(targetUser):
    userLink = link + targetUser + "/"
    html_text = requests.get(userLink).text
    soup = BeautifulSoup(html_text, 'html.parser')
    title = str(soup.title)
    title = title.replace("<title>Untrusted – web of cybercrime – |", "").replace("'s profile</title>", "").replace(" ",
                                                                                                                    "")
    if title == targetUser:
        return True
    return False


for user in listUsers():
    if checkIfUserExists(user[0]):
        userToCheck.append(user[0])


@bot.command()
async def stats(ctx, targetUser):
    stats = userStats(targetUser)

    emb = await ctx.send(embed=createEmbed(stats, targetUser, 0))

    buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
    current = 0
    for button in buttons:
        await emb.add_reaction(button)
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction,
                                                                             user: user == ctx.author and reaction.emoji in buttons,
                                                timeout=60.0)
        except asyncio.TimeoutError:
            return
        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
            elif reaction.emoji == u"\u25C0":
                if current > 0:
                    current -= 1
            elif reaction.emoji == u"\u25B6":
                if current < 10 - 1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = 25 - 1

            for button in buttons:
                await emb.remove_reaction(button, ctx.author)

            if current != previous_page:
                await emb.edit(embed=createEmbed(stats, targetUser, current))


@bot.command()
async def list(ctx):
    await ctx.send(userToCheck)


@bot.command()
async def add(ctx, targetUser):
    await ctx.send("Checking if " + targetUser + " actually exists")
    if not checkIfUserExists(targetUser):
        await ctx.send(targetUser + " is not an untrusted user")
        return

    else:
        await ctx.send(targetUser + " is an untrusted user")

        if targetUser not in userToCheck:
            userToCheck.append(targetUser)
            addUser((targetUser,))
            await ctx.send(targetUser + " is now in the database")
        else:
            await ctx.send(targetUser + " is already in the database")


if __name__ == "__main__":
    pass

userFileRead = open("userList", "r")
for User in userFileRead:
    if checkIfUserExists(User.strip()):
        userToCheck.append(User.strip())

bot.run("TOKEN")
