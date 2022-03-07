
import csv

baseball_data_dict = {}
"""converting csv into above dictionary for card info"""
with open("data/baseball_card_data.csv") as data:
    reader = csv.DictReader(data)
    for line in reader:
        new_id = int(line['app_id'])
        baseball_data_dict[new_id] = line


def get_set(year, maker, line, set):
    """returns list of all cards needed to complete a provided set"""
    set_list = []
    for card in baseball_data_dict:
        if baseball_data_dict[card]['year'] == str(year) and \
                baseball_data_dict[card]['maker'] == maker and \
                baseball_data_dict[card]['line'] == line and \
                baseball_data_dict[card]['set'] == set:
            set_list.append(card)
    return set_list

redux_1952 = get_set(2021, 'Topps', 'Series 1', 'Topps 1952 Redux')

