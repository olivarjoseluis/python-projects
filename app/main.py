import read_csv
import charts
import utils


def run():
    data = read_csv.readCsv('data.csv')
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    worldPopulationPercentage = list(
        map(lambda x: x['World Population Percentage'], data))
    charts.generateBPieChart('South America',countries, worldPopulationPercentage)

    country = input('Type a country: ')
    name=country

    result = utils.populationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(name, labels, values)


if __name__ == '__main__':
    run()
