
#This iis not a very accurate method and it was done like this for experemental purposes
#---------------------------------------------------------------------------------------
#program that scrape (laptop) data from ebay.com 
#and return a dictionary with (names) and (prices) from the first (two) pages
#finally save data in a csv file

import requests
from bs4 import BeautifulSoup
import csv

item_name = []
item_price = []

csv_file = open("ebay-laptops.csv","w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Item Name","Price"])

for i in range(1,3):
    ebayUrl=f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&LH_TitleDesc=0&_pgn={i}"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    html_content = requests.get(ebayUrl, headers=headers).content
    soup = BeautifulSoup(html_content, "lxml")

    for listings in soup.find_all("li", class_="s-item"):
        names = listings.find_all("h3", class_="s-item__title s-item__title--has-tags")
        price = listings.find_all("span", class_="s-item__price")
        for n in names:
            n=n.get_text()
            item_name.append(n)
        for p in price:
            p=p.get_text()
            item_price.append(p)

for na,pr in zip(item_name,item_price):
    csv_writer.writerow([na,pr])

csv_file.close()
#item_data=dict(zip(item_name,item_price))


        

        
            
