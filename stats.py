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

    rolesDB = {"OL" :{}, "CCTV": {}, "Enforcer": {}, "IM": {}, "Anal": {}, "NS": {}}

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

    print(rolesDB["Anal"])


    return {"level": level,
            "strLevel": stringLevel,
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

            }