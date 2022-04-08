# Main python file for price tracking automation

# importing required libraries
import json
import pandas
import requests

# Defining functions
def get_price_data():
    url_mapping = 'https://prices.runescape.wiki/api/v1/osrs/mapping' # used to get names for each item_id and current price
    url_latest = 'https://prices.runescape.wiki/api/v1/osrs/latest' # used to get current high and low prices
    headers = {
        'User-Agent': 'ge-tracking',
        'From': 'ge-tracker'
    }
