def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme :
        jour, heure, minute, seconde."""
    jts = temps[0] * 86400
    hts = temps[1] * 3600
    mts = temps[2] * 60
    return jts + hts + mts + temps[3]


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde)
       qui correspond au nombre de seconde passé en argument"""
    stj = seconde // 86400
    sth = seconde // 3600 % 24
    stm = seconde // 60 % 60
    return stj, sth, stm, seconde % 60


def ex1():
    temps = (3, 23, 1, 34)
    print(type(temps))
    print(tempsEnSeconde(temps))
    temps = secondeEnTemps(100000)
    print(temps[0], "jours",
          temps[1], "heures",
          temps[2], "minutes",
          temps[3], "secondes")


def affichePluriel(val, mot):
    if val != 0:
        print(" ", val, mot, end="")
    if val > 1:
        print("s", end="")


def afficheTemps(temps):
    affichePluriel(temps[0], "jour")
    affichePluriel(temps[1], "heure")
    affichePluriel(temps[2], "minute")
    affichePluriel(temps[3], "seconde")


def isBisextile(year):
    return (year % 4 == 0 and (year % 100 and year % 400 == 0))


def nombreBisextile(day):
    currentYear = 1970
    nbBisextile = 0
    bisextile = False
    while day > 365 + bisextile:
        day = day - 365
        currentYear = currentYear + 1
        bisextile = isBisextile(currentYear)
        nbBisextile = nbBisextile + bisextile
    return nbBisextile


def getYearAndDay(day):
    currentYear = 1970
    bisextile = False
    while day > 365 + bisextile:
        day = day - 365
        currentYear = currentYear + 1
        bisextile = isBisextile(currentYear)
    return currentYear, day


day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def tempsEnDate(temps):
    year, day = divmod(temps[0], 365)
    year = year + 1970
    month = 0
    while day > day_in_month[month]:
        day = day - day_in_month[month]
        month = month + 1

    return (year,
            month,
            day,
            temps[1],
            temps[2],
            temps[3])


def afficheDate(date=-1):
    if(date == -1):
        return

    def strMonth(date):
        print("mois", date[1])

    def strYear(date):
        return "année " + str(date[0])

    print(strYear(date) + strMonth(date))
    afficheTemps((date[2], date[3], date[4], date[5]))


tempsEnDate(1000000000)
