import requests
from bs4 import BeautifulSoup

link = "https://eu01.playuntrusted.com/profile/"



def userStats(targetUser):
    userLink = link + targetUser + "/"
    html_text = requests.get(userLink).text
    soup = BeautifulSoup(html_text, 'html.parser')

    divLevel = soup.find_all("div", {"class": "level-text"})
    level = str(divLevel[0]).replace('<div class="level-text"><span class="part">Level', "").split("<")[0]
    stringLevel = str(divLevel[0]).split("(")[1].split(")")[0]

    winstreakTitle = soup.find_all("h1", {"class": "win-streak"})

    winstreak = str(winstreakTitle).split("wins")[0].replace('[<h1 class="win-streak"><span class="part">Current Winning Streak:</span> <span class="part">', "")
    winstreakXP =  str(winstreakTitle).split("wins")[1].split('(')[1].split(')')[0]
    if not winstreakXP:
        winstreakXP = 1.0
    if not winstreak:
        winstreak = 0


    games = soup.find_all("table", {"class": "grid-table win-table"})
    season = str(games[0]).split("SEASON")[1].split("TOTAL")[0]
    seasonGameWon = season.split("<td>")[1].replace("</td>", "")
    seasonGameLost = season.split("<td>")[2].replace("</td>", "")
    seasonGameRatio = season.split("<td>")[3].replace('</td><td class="win-type">', "")

    total = str(games[0]).split("TOTAL")[1]
    totalGameWon = total.split("<td>")[1].replace("</td>", "")
    totalGameLost = total.split("<td>")[2].replace("</td>", "")
    totalGameRatio = total.split("<td>")[3].replace('</td><td class="win-type">', "").replace("</td></table>", "")

    badgesli = str(soup.find_all("li", {"class": "badge"})).split("id")

    badges = []
    for x in range(0, 100):
        try:
            foundBadge = badgesli[x].split("<img alt=")[1].replace('class="icon" ', "").replace('"', "")
            if "Played as Operation Leader" in foundBadge:
                break

            if "Good k" in foundBadge:
                foundBadge = foundBadge + "id"
            badges.append(foundBadge)
        except:
            pass
    totalofbadges = len(badges)

    rolesStart = str(soup.find_all("p", {"class": "role-start"})).split("</p>")
    rolesStats = str(soup.find_all("li", {"class": "role-item role-stat"})).split("</li>")

    rolesDB = {"OL" :{}, "CCTV": {}, "Enforcer": {}, "IM": {}, "Anal": {}, "NS": {}, "SE": {}, "BH": {}, "IH": {}, "Spear": {}, "BoHu": {}, "Journo":{}, "Skiddie": {}, "Blubber": {}, "RC": {}, "Socio": {}, "RH": {}, "CD": {}, "AL": {}, "FA": {}, "Mole FO": {}, "Mole inv": {}, "Mole off": {}, "RS": {}}

    rolesDB["OL"]["Start"] = rolesStart[0].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["OL"]["Finished"] = rolesStart[0].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["OL"]["Win"] = rolesStats[0].replace('[<li class="role-item role-stat">', "")
    rolesDB["OL"]["Loses"] = rolesStats[1].replace(', <li class="role-item role-stat">', "")
    rolesDB["OL"]["Ratio"] = rolesStats[2].replace(', <li class="role-item role-stat">', "")

    rolesDB["CCTV"]["Start"] = rolesStart[1].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["CCTV"]["Finished"] = rolesStart[1].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["CCTV"]["Win"] = rolesStats[7].replace('[<<li class="role-item role-stat">', "").replace('<li class="role-item role-stat">', "")
    rolesDB["CCTV"]["Loses"] = rolesStats[8].replace(', <li class="role-item role-stat">', "")
    rolesDB["CCTV"]["Ratio"] = rolesStats[9].replace(', <li class="role-item role-stat">', "")

    rolesDB["Enforcer"]["Start"] = rolesStart[2].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Enforcer"]["Finished"] = rolesStart[2].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Enforcer"]["Win"] = rolesStats[14].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Enforcer"]["Loses"] = rolesStats[15].replace(', <li class="role-item role-stat">', "")
    rolesDB["Enforcer"]["Ratio"] = rolesStats[16].replace(', <li class="role-item role-stat">', "")

    rolesDB["IM"]["Start"] = rolesStart[3].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["IM"]["Finished"] = rolesStart[3].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["IM"]["Win"] = rolesStats[19].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["IM"]["Loses"] = rolesStats[20].replace(', <li class="role-item role-stat">', "")
    rolesDB["IM"]["Ratio"] = rolesStats[21].replace(', <li class="role-item role-stat">', "")

    rolesDB["Anal"]["Start"] = rolesStart[4].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Anal"]["Finished"] = rolesStart[4].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Anal"]["Win"] = rolesStats[28].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Anal"]["Loses"] = rolesStats[29].replace(', <li class="role-item role-stat">', "")
    rolesDB["Anal"]["Ratio"] = rolesStats[30].replace(', <li class="role-item role-stat">', "")

    rolesDB["NS"]["Start"] = rolesStart[5].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["NS"]["Finished"] = rolesStart[5].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["NS"]["Win"] = rolesStats[35].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["NS"]["Loses"] = rolesStats[36].replace(', <li class="role-item role-stat">', "")
    rolesDB["NS"]["Ratio"] = rolesStats[37].replace(', <li class="role-item role-stat">', "")

    rolesDB["SE"]["Start"] = rolesStart[6].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["SE"]["Finished"] = rolesStart[6].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["SE"]["Win"] = rolesStats[42].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["SE"]["Loses"] = rolesStats[43].replace(', <li class="role-item role-stat">', "")
    rolesDB["SE"]["Ratio"] = rolesStats[44].replace(', <li class="role-item role-stat">', "")

    rolesDB["BH"]["Start"] = rolesStart[7].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["BH"]["Finished"] = rolesStart[7].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["BH"]["Win"] = rolesStats[49].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["BH"]["Loses"] = rolesStats[50].replace(', <li class="role-item role-stat">', "")
    rolesDB["BH"]["Ratio"] = rolesStats[51].replace(', <li class="role-item role-stat">', "")

    rolesDB["IH"]["Start"] = rolesStart[8].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["IH"]["Finished"] = rolesStart[8].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["IH"]["Win"] = rolesStats[56].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["IH"]["Loses"] = rolesStats[57].replace(', <li class="role-item role-stat">', "")
    rolesDB["IH"]["Ratio"] = rolesStats[58].replace(', <li class="role-item role-stat">', "")

    rolesDB["Spear"]["Start"] = rolesStart[9].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Spear"]["Finished"] = rolesStart[9].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Spear"]["Win"] = rolesStats[63].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Spear"]["Loses"] = rolesStats[64].replace(', <li class="role-item role-stat">', "")
    rolesDB["Spear"]["Ratio"] = rolesStats[65].replace(', <li class="role-item role-stat">', "")

    rolesDB["BoHu"]["Start"] = rolesStart[10].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["BoHu"]["Finished"] = rolesStart[10].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["BoHu"]["Win"] = rolesStats[70].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["BoHu"]["Loses"] = rolesStats[71].replace(', <li class="role-item role-stat">', "")
    rolesDB["BoHu"]["Ratio"] = rolesStats[72].replace(', <li class="role-item role-stat">', "")

    rolesDB["Journo"]["Start"] = rolesStart[11].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Journo"]["Finished"] = rolesStart[11].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Journo"]["Win"] = rolesStats[77].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Journo"]["Loses"] = rolesStats[78].replace(', <li class="role-item role-stat">', "")
    rolesDB["Journo"]["Ratio"] = rolesStats[79].replace(', <li class="role-item role-stat">', "")

    rolesDB["Skiddie"]["Start"] = rolesStart[12].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Skiddie"]["Finished"] = rolesStart[12].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Skiddie"]["Win"] = rolesStats[84].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Skiddie"]["Loses"] = rolesStats[85].replace(', <li class="role-item role-stat">', "")
    rolesDB["Skiddie"]["Ratio"] = rolesStats[86].replace(', <li class="role-item role-stat">', "")

    rolesDB["Blubber"]["Start"] = rolesStart[13].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Blubber"]["Finished"] = rolesStart[13].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Blubber"]["Win"] = rolesStats[91].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Blubber"]["Loses"] = rolesStats[92].replace(', <li class="role-item role-stat">', "")
    rolesDB["Blubber"]["Ratio"] = rolesStats[93].replace(', <li class="role-item role-stat">', "")

    rolesDB["RC"]["Start"] = rolesStart[14].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["RC"]["Finished"] = rolesStart[14].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["RC"]["Win"] = rolesStats[98].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["RC"]["Loses"] = rolesStats[99].replace(', <li class="role-item role-stat">', "")
    rolesDB["RC"]["Ratio"] = rolesStats[100].replace(', <li class="role-item role-stat">', "")

    rolesDB["Socio"]["Start"] = rolesStart[15].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Socio"]["Finished"] = rolesStart[15].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Socio"]["Win"] = rolesStats[105].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Socio"]["Loses"] = rolesStats[106].replace(', <li class="role-item role-stat">', "")
    rolesDB["Socio"]["Ratio"] = rolesStats[107].replace(', <li class="role-item role-stat">', "")

    rolesDB["RH"]["Start"] = rolesStart[16].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["RH"]["Finished"] = rolesStart[16].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["RH"]["Win"] = rolesStats[112].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["RH"]["Loses"] = rolesStats[113].replace(', <li class="role-item role-stat">', "")
    rolesDB["RH"]["Ratio"] = rolesStats[114].replace(', <li class="role-item role-stat">', "")

    rolesDB["CD"]["Start"] = rolesStart[17].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["CD"]["Finished"] = rolesStart[17].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["CD"]["Win"] = rolesStats[119].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["CD"]["Loses"] = rolesStats[120].replace(', <li class="role-item role-stat">', "")
    rolesDB["CD"]["Ratio"] = rolesStats[121].replace(', <li class="role-item role-stat">', "")

    rolesDB["AL"]["Start"] = rolesStart[18].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["AL"]["Finished"] = rolesStart[18].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["AL"]["Win"] = rolesStats[126].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["AL"]["Loses"] = rolesStats[127].replace(', <li class="role-item role-stat">', "")
    rolesDB["AL"]["Ratio"] = rolesStats[128].replace(', <li class="role-item role-stat">', "")

    rolesDB["FA"]["Start"] = rolesStart[19].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["FA"]["Finished"] = rolesStart[19].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["FA"]["Win"] = rolesStats[133].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["FA"]["Loses"] = rolesStats[134].replace(', <li class="role-item role-stat">', "")
    rolesDB["FA"]["Ratio"] = rolesStats[135].replace(', <li class="role-item role-stat">', "")

    rolesDB["Mole FO"]["Start"] = rolesStart[20].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Mole FO"]["Finished"] = rolesStart[20].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Mole FO"]["Win"] = rolesStats[140].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Mole FO"]["Loses"] = rolesStats[141].replace(', <li class="role-item role-stat">', "")
    rolesDB["Mole FO"]["Ratio"] = rolesStats[142].replace(', <li class="role-item role-stat">', "")

    rolesDB["Mole inv"]["Start"] = rolesStart[21].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Mole inv"]["Finished"] = rolesStart[21].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Mole inv"]["Win"] = rolesStats[147].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Mole inv"]["Loses"] = rolesStats[148].replace(', <li class="role-item role-stat">', "")
    rolesDB["Mole inv"]["Ratio"] = rolesStats[149].replace(', <li class="role-item role-stat">', "")

    rolesDB["Mole off"]["Start"] = rolesStart[22].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["Mole off"]["Finished"] = rolesStart[22].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["Mole off"]["Win"] = rolesStats[154].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["Mole off"]["Loses"] = rolesStats[155].replace(', <li class="role-item role-stat">', "")
    rolesDB["Mole off"]["Ratio"] = rolesStats[156].replace(', <li class="role-item role-stat">', "")

    rolesDB["RS"]["Start"] = rolesStart[23].split("</span>")[0].split('"part"')[1].replace(">", "")
    rolesDB["RS"]["Finished"] = rolesStart[23].split("</span>")[1].split('"part"')[1].replace(">", "")
    rolesDB["RS"]["Win"] = rolesStats[161].replace('[<<li class="role-item role-stat">', "").replace(
        '<li class="role-item role-stat">', "")
    rolesDB["RS"]["Loses"] = rolesStats[162].replace(', <li class="role-item role-stat">', "")
    rolesDB["RS"]["Ratio"] = rolesStats[163].replace(', <li class="role-item role-stat">', "")



    return {"level": level,
            "strLevel": stringLevel,
            "WinStreak": winstreak,
            "winStreakBoost": winstreakXP,
            "seasonGameWon": seasonGameWon,
            "seasonGameLost": seasonGameLost,
            "seasonGameRatio": seasonGameRatio,
            "totalGameWon": totalGameWon,
            "totalGameLost": totalGameLost,
            "totalGameRatio": totalGameRatio,
            "totalOfBadges": totalofbadges,
            "badges": badges,
            "OLWin": rolesDB["OL"]["Win"],
            "OLLoses": rolesDB["OL"]["Loses"],
            "OLRatio": rolesDB["OL"]["Ratio"],
            "CCTVWin": rolesDB["CCTV"]["Win"],
            "CCTVLoses": rolesDB["CCTV"]["Loses"],
            "CCTVRatio": rolesDB["CCTV"]["Ratio"],
            "ENFWin": rolesDB["Enforcer"]["Win"],
            "ENFLoses": rolesDB["Enforcer"]["Loses"],
            "ENFRatio": rolesDB["Enforcer"]["Ratio"],
            "IMWin": rolesDB["IM"]["Win"],
            "IMLoses": rolesDB["IM"]["Loses"],
            "IMRatio": rolesDB["IM"]["Ratio"],
            "AnalWin": rolesDB["Anal"]["Win"],
            "AnalLoses": rolesDB["Anal"]["Loses"],
            "AnalRatio": rolesDB["Anal"]["Ratio"],
            "NSWin": rolesDB["NS"]["Win"],
            "NSLoses": rolesDB["NS"]["Loses"],
            "NSRatio": rolesDB["NS"]["Ratio"],
            "SEWin": rolesDB["SE"]["Win"],
            "SELoses": rolesDB["SE"]["Loses"],
            "SERatio": rolesDB["SE"]["Ratio"],
            "BHWin": rolesDB["BH"]["Win"],
            "BHLoses": rolesDB["BH"]["Loses"],
            "BHRatio": rolesDB["BH"]["Ratio"],
            "IHWin": rolesDB["IH"]["Win"],
            "IHLoses": rolesDB["IH"]["Loses"],
            "IHRatio": rolesDB["IH"]["Ratio"],
            "SpearWin": rolesDB["Spear"]["Win"],
            "SpearLoses": rolesDB["Spear"]["Loses"],
            "SpearRatio": rolesDB["Spear"]["Ratio"],
            "BoHuWin": rolesDB["BoHu"]["Win"],
            "BoHuLoses": rolesDB["BoHu"]["Loses"],
            "BoHuRatio": rolesDB["BoHu"]["Ratio"],
            "JournoWin": rolesDB["Journo"]["Win"],
            "JournoLoses": rolesDB["Journo"]["Loses"],
            "JournoRatio": rolesDB["Journo"]["Ratio"],
            "SkiddieWin": rolesDB["Skiddie"]["Win"],
            "SkiddieLoses": rolesDB["Skiddie"]["Loses"],
            "SkiddieRatio": rolesDB["Skiddie"]["Ratio"],
            "BlubberWin": rolesDB["Blubber"]["Win"],
            "BlubberLoses": rolesDB["Blubber"]["Loses"],
            "BlubberRatio": rolesDB["Blubber"]["Ratio"],
            "RCWin": rolesDB["RC"]["Win"],
            "RCLoses": rolesDB["RC"]["Loses"],
            "RCRatio": rolesDB["RC"]["Ratio"],
            "SocioWin": rolesDB["Socio"]["Win"],
            "SocioLoses": rolesDB["Socio"]["Loses"],
            "SocioRatio": rolesDB["Socio"]["Ratio"],
            "RHWin": rolesDB["RH"]["Win"],
            "RHLoses": rolesDB["RH"]["Loses"],
            "RHRatio": rolesDB["RH"]["Ratio"],
            "CDWin": rolesDB["CD"]["Win"],
            "CDLoses": rolesDB["CD"]["Loses"],
            "CDRatio": rolesDB["CD"]["Ratio"],
            "ALWin": rolesDB["AL"]["Win"],
            "ALLoses": rolesDB["AL"]["Loses"],
            "ALRatio": rolesDB["AL"]["Ratio"],
            "FAWin": rolesDB["FA"]["Win"],
            "FALoses": rolesDB["FA"]["Loses"],
            "FARatio": rolesDB["FA"]["Ratio"],
            "Mole FOWin": rolesDB["Mole FO"]["Win"],
            "Mole FOLoses": rolesDB["Mole FO"]["Loses"],
            "Mole FORatio": rolesDB["Mole FO"]["Ratio"],
            "Mole invWin": rolesDB["Mole inv"]["Win"],
            "Mole invLoses": rolesDB["Mole inv"]["Loses"],
            "Mole invRatio": rolesDB["Mole inv"]["Ratio"],
            "Mole offWin": rolesDB["Mole off"]["Win"],
            "Mole offLoses": rolesDB["Mole off"]["Loses"],
            "Mole offRatio": rolesDB["Mole off"]["Ratio"],
            "RSWin": rolesDB["RS"]["Win"],
            "RSLoses": rolesDB["RS"]["Loses"],
            "RSRatio": rolesDB["RS"]["Ratio"]



            }