def getPopulation(country):
    populationDict = {
        '2022': int(country['2022 Population']),
        '2020': int(country['2020 Population']),
        '2015': int(country['2015 Population']),
        '2010': int(country['2010 Population']),
        '2000': int(country['2000 Population']),
        '1990': int(country['1990 Population']),
        '1980': int(country['1980 Population']),
        '1970': int(country['1970 Population']),
    }
    keys = populationDict.keys()
    values = populationDict.values()
    return keys, values


def populationByCountry(data, country):
    result = list(
        filter(lambda item: item['Country/Territory'] == country, data))

    return result


def getWorldPopulationPercentage(data):
    result = []
    for row in data:
        result.append(
            {row['Country/Territory']: row['World Population Percentage']})
    return result


def stringTypeId(string):
    return string.lower().replace(' ', '-')
