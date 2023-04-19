import matplotlib.pyplot as plt


def generatePieChart():
    labels = ['A', 'B', 'C', 'D']
    values = [250, 150, 456, 200]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #plt.show()
    plt.savefig('pie.png')
    plt.close()