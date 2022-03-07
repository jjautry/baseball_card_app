import csv
import pandas as pd



# add card to user_data
def add_new_card(app_id, variation=None):
    """Adds new card to user_data from app_id"""
    data = {
        'app_id': [app_id],
        'quantity': [1],
        'variation': [variation]
    }
    df = pd.DataFrame(data)
    df.to_csv('data/user_data.csv', mode='a', index=False, header=False)
    print('Card added successfully!')
