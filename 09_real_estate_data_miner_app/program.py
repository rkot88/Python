import csv
import os

try:
    import statistics
except:
    # error code instead
    import statistic_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('----------------------------------------')
    print('------real estate data mining app-------')
    print('----------------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # with open(filename, 'r', encoding='utf-8') as fin: # encoding didn't work in python 2.7
    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    return purchases

    # header = fin.readline().strip()
    # reader = csv.reader(fin, delimiter=',')
    # for row in reader:
    #     print(row)


# def get_data_file():  load file version 1
#     base_folder = os.path.dirname(__file__)
#     return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')
#
#
# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         lines= []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])


# def get_price(p):
#     return p.price


def query_data(data):  # : list[Purchase]): # supported only in docstrings not type hints with Pycharm
    # if data was sorted by price
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)  # don't need get_price method anymore p: is an argument return p.price

    # most expensive house?
    high_purchase = data[-1]
    # print(high_purchase.price)
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # last expensive house?
    low_purchase = data[0]
    # print(low_purchase.price)
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # average price house
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = (
        p.price  # projection or items to create
        for p in data  # the set to process
    )

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(ave_price)))

    # average price of 2 bedroom houses
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    two_bed_homes = (
        p  # projection or items to create
        for p in data  # the set to process
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test or condition
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))  # list comprehension concept
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))
    print("Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}"
          .format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
