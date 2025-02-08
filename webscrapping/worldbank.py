from bs4 import BeautifulSoup
import requests
import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd

## Opens a website and read its binary contents
def url_get_contents(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


url = "https://en.wikipedia.org/wiki/World_Bank"

soup = url_get_contents(url)

# print('Classes of each table: ')
# for table in soup.find_all('table'):
#     print(table.get('class'))
    
table = soup.find('table', class_='wikitable')
# print(table)
# df = pd.DataFrame(columns=['sector', 'before 2007', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 'sum'])
df = pd.DataFrame(columns=['Name', 'Dates', 'Nationality', 'Previous work'])



for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if (columns != []):
        president = columns[0].text.strip()
        dates = columns[1].text.strip()
        nationality = columns[2].text.strip()
        prev_work = columns[3].text.strip()
        new_row = pd.DataFrame([{'Name':president, 'Dates': dates, 'Nationality': nationality, 'Previous work':prev_work}])
        print(new_row)
        df = pd.concat([df, new_row], ignore_index=True)

df.head()

df.to_csv('output.csv', sep=',')