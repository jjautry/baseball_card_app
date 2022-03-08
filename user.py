import pandas as pd
from csv_converter import baseball_data_dict
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


class Card:
    """Class for card that user entered"""
    def __init__(self, year, brand, line, set, card_id):
        self.year = year
        self.maker = brand
        self.line = line
        self.set = set
        self.card_id = card_id
        self.player = None
        self.team = None
        self.app_id = None
        self.quantity = None
        self.variation = None

    def find_in_data(self):
        id = search_dict4card(self.year, self.maker, self.line, self.set, self.card_id)
        if id:
            self.player = baseball_data_dict[int(id)]['player']
            self.team = baseball_data_dict[int(id)]['team']
            self.app_id = id
            print(f"""
            Card found, {self.player}
            \n to add it to your collection please call .add_to_user()
            """)
        else:
            print("CARD NOT FOUND")

    def add_to_user(self):
        if self.app_id:
            self.quantity = 1
            add_new_card(self.app_id, self.variation)
        else:
            print("Can't add to data - No id assigned, call .find_in_data()")
    


class Set:

    def __init__(self, year, maker, line, set):
        self.year = year
        self.maker = maker
        self.line = line
        self.set = set

    def show_set(self):
        set = []
        for key, value in baseball_data_dict.items():
            if value['year'] == str(self.year) and \
                    value['maker'] == self.maker and \
                    value['line'] == self.line and \
                    value['set'] == self.set:
                    app_id = (int(value['app_id']))
                    set.append(baseball_data_dict[app_id]['player'])
            else:
                pass
        return set
