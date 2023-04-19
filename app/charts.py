import matplotlib.pyplot as plt
from datetime import datetime
import utils


def generateBarChart(name="example-bar", labels=['a', 'b', 'c'], values=[100, 200, 80]):
    name = utils.stringTypeId(name)
    now = datetime.now()
    nowDate = now.strftime("%H%M%S%d%m%Y")
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'images/{name}-{nowDate}.png')
    plt.close()


def generateBPieChart(name="example-pie", labels=['a', 'b', 'c'], values=[100, 200, 80]):
    name = utils.stringTypeId(name)
    now = datetime.now()
    nowDate = now.strftime("%H%M%S%d%m%Y")
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'images/{name}-{nowDate}.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd', 'e']
    values = [34, 99, 25, 44, 65]
    generateBPieChart('Automatic Pie', labels, values)
