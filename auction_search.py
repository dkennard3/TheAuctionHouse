import requests
import json

def auction_search(item_ID):
    auction_data = requests.get(f'https://pricing-api.tradeskillmaster.com/ah/279/item/{item_ID}')
    sale_averages = requests.get(f'https://pricing-api.tradeskillmaster.com/region/13/item/{item_ID}')
