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

    elif page == 4:
        embed = discord.Embed(
            title=targetUser + '\'s IM games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Inside man",
            value="Wins : " + stats.get("IMWin") + "\nLoses : " + stats.get("IMLoses")
                  + " \nRatio : " + stats.get("IMRatio"),
            inline=True

        )
        return embed

    elif page == 5:
        embed = discord.Embed(
            title=targetUser + '\'s Analyst games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Analyst",
            value="Wins : " + stats.get("AnalWin") + "\nLoses : " + stats.get("AnalLoses")
                  + " \nRatio : " + stats.get("AnalRatio"),
            inline=True

        )
        return embed

    elif page == 6:
        embed = discord.Embed(
            title=targetUser + '\'s Network Specialist games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Network Specialist",
            value="Wins : " + stats.get("NSWin") + "\nLoses : " + stats.get("NSLoses")
                  + " \nRatio : " + stats.get("NSRatio"),
            inline=True

        )
        return embed

    elif page == 7:
        embed = discord.Embed(
            title=targetUser + '\'s SE games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Social Engineer",
            value="Wins : " + stats.get("SEWin") + "\nLoses : " + stats.get("SELoses")
                  + " \nRatio : " + stats.get("SERatio"),
            inline=True

        )
        return embed

    elif page == 8:
        embed = discord.Embed(
            title=targetUser + '\'s Blackhat games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Blackhat",
            value="Wins : " + stats.get("BHWin") + "\nLoses : " + stats.get("BHLoses")
                  + " \nRatio : " + stats.get("BHRatio"),
            inline=True

        )
        return embed

    elif page == 9:
        embed = discord.Embed(
            title=targetUser + '\'s Improvised Hacker games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="IH",
            value="Wins : " + stats.get("IHWin") + "\nLoses : " + stats.get("IHLoses")
                  + " \nRatio : " + stats.get("IHRatio"),
            inline=True

        )
        return embed

    elif page == 10:
        embed = discord.Embed(
            title=targetUser + '\'s Spearphisher games',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Spearphisher",
            value="Wins : " + stats.get("SpearWin") + "\nLoses : " + stats.get("SpearLoses")
                  + " \nRatio : " + stats.get("SpearRatio"),
            inline=True

        )
        return embed

    elif page == 11:
        embed = discord.Embed(
            title=targetUser + '\'s Bounty Hunter',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Bounty Hunter",
            value="Wins : " + stats.get("BoHuWin") + "\nLoses : " + stats.get("BoHuLoses")
                  + " \nRatio : " + stats.get("BoHuRatio"),
            inline=True

        )
        return embed