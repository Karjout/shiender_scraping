#karjout abdeslam
from bs4 import BeautifulSoup
import requests
def read_links_file():
    with open('links.txt', 'r') as f:     
        return f.read().splitlines()
    
def get_htmls(url):
    while True:
        response = requests.get(url,timeout=100)
        if response.status_code == 200:
            return response.text 
            
def get_data(html):
    ids= []
    soup = BeautifulSoup(html,'lxml')
    for ele in soup.find_all('product-cards-wrapper'):
        ids.append(ele['product-ids'])
        print('ids = ',ids)
    with open('ids.txt','a+') as f:
        for i in ids:
            ids = i.replace(',','\n')
            f.write("%s\n" % ids) 
    f.close()
    
def main():
    urls_a=read_links_file()
    print(urls_a)
    for url in range(0,len(urls_a)):
        data= get_data(get_htmls(urls_a[url]))
        print(data)
    
if __name__ == '__main__':
    main()