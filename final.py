import requests
import json
import pandas as pd

from requests.api import get
def get_items(url):
    
    response = requests.get(url).json()
    data_net= {'repositoryId':response['products'][0]['repositoryId'],
    'commercialReference':response['products'][0]['commercialReference'],
    'description':response['products'][0]['description'],
    'price':'null',
    'currency':'null',
    'pictureUrl':response['products'][0]['pictureUrl'],
    'pictureAltText':response['products'][0]['pictureAltText'],
    'pdpUrl':response['products'][0]['pdpUrl']
    }
    with open("Produits.json", 'a') as fout:
        json_dumps_str = json.dumps(data_net, indent=4)
        print(json_dumps_str, file=fout)
    
# def save_data(data):
#     try:
#         with open('Produits.csv', 'w') as f:
#             for key, value in data:
#                 writer = csv.DictWriter(f, fieldnames=key)
#                 writer.writeheader()
#                 writer.writerow(value)
#     except IOError:
#         print("I/O error")

def load_data():
    with open('ids.txt', 'r') as f:
        return f.read().splitlines()
def main():
   ids= load_data()
   url =f'https://www.se.com/ww/en/product/api/productCard/main?ids='
   for id in range(0, len(ids)):
       get_items(url+ids[id])
       #get_items(url+ids[id])
if __name__ == '__main__':
    main()