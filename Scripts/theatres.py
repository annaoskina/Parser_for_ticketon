import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://ticketon.kz/almaty/theatres?date_from=21.02.2023&date_to=21.03.2023'
r = requests.get(URL)
#print(r)

#bs = BeautifulSoup(r.text, 'lxml')
#print(bs)
soup = BeautifulSoup(r.content, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup)

items = soup.find_all('div', class_="block-1 list-block")
df_theatres = []
#print(items[0])
for item in items:
	try:
		theatre_a = item.find('a', class_="list-item__place")
		theatre = theatre_a['title']
		link = theatre_a['href']
		full_link = 'https://m.ticketon.kz' + link
		date = item.time.text
		title_a = item.find('a', class_="list-item__link")
		title = title_a['title']
		line = 'театр' + '\t' + theatre + '\t' + full_link + '\n'
		if line in df_theatres:
			continue
		else:
			df_theatres.append(line)
	except TypeError:
		print('TypeError')

with open('theatres.tsv', 'w', encoding = 'utf-8') as w_file:
	for row in df_theatres:
		w_file.write(row)