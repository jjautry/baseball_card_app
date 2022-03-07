import csv
import pandas as pd
from csv_converter import baseball_data_dict, get_set
from datetime import datetime


# add card to user_data
def add_new_card(app_id, variation=None):
    """Adds new card to user_data from app_id"""
    today_date = datetime.today().date()
    data = {
        'app_id': [app_id],
        'quantity': [1],
        'variation': [variation],
        'date_entered': [today_date]
    }
    df = pd.DataFrame(data)
    df.to_csv('data/user_data.csv', mode='a', index=False, header=False)
    print('Card added successfully!')

def search_dict4card(year, maker, line, set, card_number):
    """Searches dict for card and returns False if not found, the app_id for card if found"""
    for key, value in baseball_data_dict.items():
        if value['year'] == str(year) and \
                value['maker'] == maker and \
                value['line'] == line and \
                value['set'] == set and \
                value['card_id'] == str(card_number):
            return value['app_id']
        else:
            pass


def add_card_test():
    input_year = input("Year: \n")
    input_maker = input("Card Brand: \n")
    input_line = input("Brand Line: \n")
    input_set = input("Specific set or Base: \n")
    input_id = input("# on top-back of card: \n")
    if search_dict4card(input_year, input_maker, input_line, input_set, input_id):
        new_card_id = int(search_dict4card(input_year, input_maker, input_line, input_set, input_id))
        variation = input("Is this card a variation, if so what is it? EX: 'Gold' \nClick ENTER if no:")
        agreement = input(f"Are you sure you want to input {baseball_data_dict[new_card_id]['player']}? y/n :\n")
        if agreement == 'y':
            add_new_card(new_card_id, variation)
        else:
            pass
    else:
        print("Card not found in 'Database'")



