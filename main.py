# Main python file for price tracking automation

# importing required libraries
import pandas as pd
import requests
from win10toast import ToastNotifier

toaster = ToastNotifier()

url_mapping = 'https://prices.runescape.wiki/api/v1/osrs/mapping' # used to get names for each item_id and current price
url_latest = 'https://prices.runescape.wiki/api/v1/osrs/latest' # used to get current high and low prices
headers = {
    'User-Agent': 'ge-tracking',
    'From': 'ge-tracker'
}

resp_map_json = requests.get(url_mapping).json() # price map response in json format
resp_late_json = requests.get(url_latest).json() # latest prices repsonse in json format

df_map = pd.DataFrame.from_dict(resp_map_json) # defining dataframe for map
clean_df_map = df_map.drop(['examine', 'members', 'lowalch', 'limit', 'highalch', 'icon', 'value'], axis=1).sort_values(by=['id'], ascending=True).reset_index() #reformating
cleaner_df_map = clean_df_map.drop(['index'], axis=1) # reformating

clean_df_late = pd.DataFrame.from_dict(resp_late_json['data']).transpose().drop(['highTime','lowTime'], axis=1) # reformating
clean_df_late.reset_index(inplace=True) # reseting index
cleaner_df_late = clean_df_late.rename(columns={'index':'id'}) # renaming item_id index for merge

cleaner_df_late['id'] = cleaner_df_late['id'].astype(str).astype(int)
df_merge = pd.merge(cleaner_df_late, cleaner_df_map, how='outer',on='id')
toaster.show_toast("DataFrame's Merged!","The price map, and latest high and lows have been merged.",duration=15) # 