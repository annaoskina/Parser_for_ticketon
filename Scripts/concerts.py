import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://m.ticketon.kz/almaty/concerts?date_from=22.02.2023&date_to=22.03.2023'
r = requests.get(URL)
#print(r)

#bs = BeautifulSoup(r.text, 'lxml')
#print(bs)
soup = BeautifulSoup(r.content, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup)

li = soup.find_all('li', class_="b-list__item-grid")
df_concerts = []
#print(items[0])
for tag in li:
	a_tag = tag.find_all('a')
	for a in a_tag:
		url = a['href']
		url = 'https://m.ticketon.kz/' + url
		item_img = tag.find_all('img')
		for image in item_img:
			#print(line)
			title = image['alt']
			new_line = title + '\t' + url + '\n'
			df_concerts.append(new_line)


with open('concerts.tsv', 'w', encoding = 'utf-8') as w_file:
	for line in df_concerts:
		w_file.write(line)