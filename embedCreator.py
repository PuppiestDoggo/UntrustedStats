import datetime

import discord


def createEmbed(stats, targetUser, page):
    if page == 0:
        embed = discord.Embed(
            title=targetUser + '\'s Profile',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Level",
            value=stats.get("level") + " " + stats.get("strLevel"),
            inline=False
        )

        embed.add_field(
            name="TOTAL",
            value="Wins : " + stats.get("totalGameWon") + "\nLoses : " + stats.get("totalGameLost")
                  + " \nRatio : " + stats.get("totalGameRatio"),
            inline=True

        )
        embed.add_field(
            name="SEASON",
            value="Wins : " + stats.get("seasonGameWon") + "\nLoses : " + stats.get("seasonGameLost")
                  + " \nRatio : " + stats.get("seasonGameRatio"),
            inline=True

        )

        embed.add_field(
            name="Badges",
            value=str(stats.get("badges")).replace("'", "").replace("[", "").replace("]", ""),
            inline=True

        )

        return embed


    elif page == 1:
        embed = discord.Embed(
            title=targetUser + '\'s OL Games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="OL",
            value="Wins : " + stats.get("OLWin") + "\nLoses : " + stats.get("OLLoses")
                  + " \nRatio : " + stats.get("OLRatio"),
            inline=True

        )
        return embed

    elif page == 2:
        embed = discord.Embed(
            title=targetUser + '\'s CTTV Games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="CCTV",
            value="Wins : " + stats.get("CCTVWin") + "\nLoses : " + stats.get("CCTVLoses")
                  + " \nRatio : " + stats.get("CCTVRatio"),
            inline=True

        )
        return embed

    elif page == 3:
        embed = discord.Embed(
            title=targetUser + '\'s Enforcer games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="ENFORCER",
            value="Wins : " + stats.get("ENFWin") + "\nLoses : " + stats.get("ENFLoses")
                  + " \nRatio : " + stats.get("ENFRatio"),
            inline=True

        )
        return embed