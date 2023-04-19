import csv


def readCsv(path):
    with open(path, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        header = next(reader)
        data = []
        # print(header)
        for row in reader:
            iterable = zip(header, row)
            # print(dict(iterable))
            countryDict = {key: value for key, value in iterable}
            data.append(countryDict)
    return data


if __name__ == '__main__':
    data = readCsv('./app/data.csv')
    print(data)
