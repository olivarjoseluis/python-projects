import read_csv
import charts
import utils
import pandas as pd


def run():
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Europe']

    countries = df['Country/Territory'].values
    worldPopulationPercentage = df['World Population Percentage'].values

    charts.generateBPieChart('Europe', countries, worldPopulationPercentage)
    data = read_csv.readCsv('data.csv')
    country = input('Type a country: ')
    name = country

    result = utils.populationByCountry(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(name, labels, values)


if __name__ == '__main__':
    run()
