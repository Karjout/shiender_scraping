
def main():
    data_id =['5en_WW','2en_WW','4en_WW','7en_WW','1en_WW']
    url  = 'https://www.se.com/ww/en/all-products/categories?businessId'
    if True:

        for i in range(0,len(data_id)):
                #data=data_id[i]
            url = f'https://www.se.com/ww/en/all-products/categories?businessId={data_id[i]}'
            return url

if __name__ == '__main__':
    main()

import requests
import re
from time import sleep
from bs4 import BeautifulSoup
def (url):
    response = requests.get(url)
    if not response.ok:
        print(f'Code :{response.status_code},url:{url}')
    return response.text
print(response['products'][0]['description'])
field_names =['repositoryId','commercialReference','description','price','currency','pictureUrl','pictureAltText','pdpUrl']
def get_data(html):
    
    soup= BeautifulSoup(html,'lxml')
    pattern= r'^https://www.se.com/africa/fr/all-products'
    data= soup.find_all('a',href =re.compile(pattern))
    return data
    
def main():
    all_data=[]
    data_id =['5en_WW','2en_WW','4en_WW','7en_WW','1en_WW']
    url  = 'https://www.se.com/africa/fr/all-products/product-category'
    while True:
        data_s = get_data(get_html(url))
        if data_s:
            for i in range(0,len(data_id)):
                url = f'https://www.se.com/ww/en/all-products/categories?businessId={data_id[i]}'
                print(url)

        else:
            break
    
if __name__ == '__main__':
    main()
data_net= {'repositoryId':response['products'][0]['repositoryId'],
    'commercialReference':response['products'][0]['commercialReference'],
    'description':response['products'][0]['description'],
    'price':response['products'][0]['price'],
    'currency':response['products'][0]['currency'],
    'pictureUrl':response['products'][0]['pictureUrl'],
    'pictureAltText':response['products'][0]['pictureAltText'],
    'pdpUrl':response['products'][0]['pdpUrl']
    }