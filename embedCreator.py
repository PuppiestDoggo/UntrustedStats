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

    elif page == 12:
        embed = discord.Embed(
            title=targetUser + '\'s Journalist',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Journalist",
            value="Wins : " + stats.get("JournoWin") + "\nLoses : " + stats.get("JournoLoses")
                  + " \nRatio : " + stats.get("JournoRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 13:
        embed = discord.Embed(
            title=targetUser + '\'s Script Kiddie',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Script Kiddie",
            value="Wins : " + stats.get("SkiddieWin") + "\nLoses : " + stats.get("SkiddieLoses")
                  + " \nRatio : " + stats.get("SkiddieRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 14:
        embed = discord.Embed(
            title=targetUser + '\'s Panicked Blabbermouth',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Panicked Blabbermouth",
            value="Wins : " + stats.get("BlubberWin") + "\nLoses : " + stats.get("BlubberLoses")
                  + " \nRatio : " + stats.get("BlubberRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 15:
        embed = discord.Embed(
            title=targetUser + '\'s Resentful Criminal',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Resentful Criminal",
            value="Wins : " + stats.get("RCWin") + "\nLoses : " + stats.get("RCLoses")
                  + " \nRatio : " + stats.get("RCRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 16:
        embed = discord.Embed(
            title=targetUser + '\'s Sociopath',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Sociopath",
            value="Wins : " + stats.get("SocioWin") + "\nLoses : " + stats.get("SocioLoses")
                  + " \nRatio : " + stats.get("SocioRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 17:
        embed = discord.Embed(
            title=targetUser + '\'s Rival Hacker',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Rival Hacker",
            value="Wins : " + stats.get("RHWin") + "\nLoses : " + stats.get("RHLoses")
                  + " \nRatio : " + stats.get("RHRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 18:
        embed = discord.Embed(
            title=targetUser + '\'s Corrupt Detective',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Corrupt Detective",
            value="Wins : " + stats.get("CDWin") + "\nLoses : " + stats.get("CDLoses")
                  + " \nRatio : " + stats.get("CDRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 19:
        embed = discord.Embed(
            title=targetUser + '\'s Agent Leader',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Agent Leader",
            value="Wins : " + stats.get("ALWin") + "\nLoses : " + stats.get("ALLoses")
                  + " \nRatio : " + stats.get("ALRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 20:
        embed = discord.Embed(
            title=targetUser + '\'s Field Agent',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Field Agent",
            value="Wins : " + stats.get("FAWin") + "\nLoses : " + stats.get("FALoses")
                  + " \nRatio : " + stats.get("FARatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 21:
        embed = discord.Embed(
            title=targetUser + '\'s Converted NETSEC/Field-OP',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Converted NETSEC/Field-OP",
            value="Wins : " + stats.get("Mole FOWin") + "\nLoses : " + stats.get("Mole FOLoses")
                  + " \nRatio : " + stats.get("Mole FORatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 22:
        embed = discord.Embed(
            title=targetUser + '\'s Converted NETSEC/Investigative',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Converted NETSEC/Investigative",
            value="Wins : " + stats.get("Mole invWin") + "\nLoses : " + stats.get("Mole invLoses")
                  + " \nRatio : " + stats.get("Mole invRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 23:
        embed = discord.Embed(
            title=targetUser + '\'s Converted NETSEC/offensive',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Converted NETSEC/offensive",
            value="Wins : " + stats.get("Mole offWin") + "\nLoses : " + stats.get("Mole offLoses")
                  + " \nRatio : " + stats.get("Mole offRatio"),
            inline=True

        )
        return embed
        # add 1 to elif page ==  ; Modify name, stats.get("OLWin" etc
        # looks nicer
    elif page == 24:
        embed = discord.Embed(
            title=targetUser + '\'s Runaway Snitch',
            timestamp=datetime.datetime.utcnow(),
            colour=discord.colour.Colour.orange()
        )

        embed.add_field(
            name="Runaway Snitch",
            value="Wins : " + stats.get("RSWin") + "\nLoses : " + stats.get("RSLoses")
                  + " \nRatio : " + stats.get("RSRatio"),
            inline=True

        )
        return embed