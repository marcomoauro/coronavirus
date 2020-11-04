import csv
import numpy as np
import matplotlib.pyplot as plt
import plot.utils as utils
import matplotlib.dates as mdates
import datetime
import plot.calculator as calculator


def axis(field, name):
    dates = []
    csv_file = open('/home/marco/Documenti/COVID-19/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
    csv_dict = csv.DictReader(csv_file)
    data = calculator.calculate_data(csv_dict, field)
    csv_file.seek(0)
    csv_dict = csv.DictReader(csv_file)
    for row in csv_dict:
        dates.append(datetime.datetime.strptime(row['data'], '%Y-%m-%dT%H:%M:%S'))

    locator = mdates.MonthLocator()  # every month
    fmt = mdates.DateFormatter('%b')

    plt.title(name)
    plt.grid()
    plt.plot(dates, data)
    X = plt.gca().xaxis
    X.set_major_locator(locator)
    # Specify formatter
    X.set_major_formatter(fmt)
    fig1 = plt.gcf()
    fig1.savefig(utils.filepath(name.replace(' ', '_').lower()), dpi=200)
    plt.close()


def bar_chart(field, name):
    data = []
    dates = []
    csv_file = open('/home/marco/Documenti/COVID-19/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
    csv_dict = csv.DictReader(csv_file)
    for row in csv_dict:
        data.append(int(row[field]))
        dates.append(row['data'].split('T')[0])

    x = np.arange(len(data))  # the label locations
    width = 0.35  # the width of the bars

    fig = plt.figure(figsize=(50, 7))
    ax = fig.add_subplot(111)
    rects1 = ax.bar(x, data, width)

    ax.set_title(name)
    ax.set_xticks(x)
    ax.set_xticklabels(dates)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=80)
    utils.autolabel(ax, rects1)
    fig.tight_layout()
    fig1 = plt.gcf()
    plt.grid()
    plt.show()
    fig1.savefig(utils.filepath(name.replace(' ', '_').lower()), dpi=200)
