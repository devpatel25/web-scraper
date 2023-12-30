# Imports
import requests
from bs4 import BeautifulSoup
import csv

url="https://www.yelp.com/search?find_desc=Restaurants&find_loc=Toronto%2C+Ontario%2C+Canada"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# open CSV file
with open("restaurants.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Rating"])

try:
    responce= requests.get(url,headers=headers)
    responce.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)

# parse html
soup =BeautifulSoup(responce.text,"html.parser")

restaurants=soup.find_all('li',class_="css-1qn0b6x")
for restaurant in restaurants:
    name=restaurant.find('a',class_='css-19v1rkv').text.strip()
    rating=restaurant.find('span',class_=" css-gutk1c").text.strip()
    print(f"Name: {name}\nRating: {range}\n")
    writer.writerow([name,rating])
