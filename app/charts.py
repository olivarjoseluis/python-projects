import matplotlib.pyplot as plt


def generateBarChart(labels=['a', 'b', 'c'], values=[100, 200, 80]):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('images/bar.png')
    plt.close()


def generateBPieChart(labels=['a', 'b', 'c'], values=[100, 200, 80]):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('images/pie.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd', 'e']
    values = [34, 99, 25, 44, 65]
    # generateBarChart(labels, values)
    generateBPieChart(labels, values)
