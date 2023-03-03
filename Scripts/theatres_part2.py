import requests
from bs4 import BeautifulSoup
import csv
import re

def find_address_str(p):
	try:
		result = re.findall('г. Алматы.*', p)
		address = result[0]
	except TypeError:
		print('TypeError')
	return address
									

with open('theatres.tsv', encoding = 'utf-8') as r_file:
	data = csv.reader(r_file, delimiter = '\t')
	data_list = list(data)
	#print(data_list)
	df = []
	for one_line in data_list:
		if one_line[2]:
			URL = one_line[2]
			r = requests.get(URL)
			soup = BeautifulSoup(r.content, 'lxml')
			divs_active = soup.find_all('div', class_='b-text')
			for divs in divs_active:
				ps = divs.find('p')
				try:
					for p in ps:
						result = re.findall('г. Алматы.*', p)
						if result:
							address = result[0]
							new_line = one_line[0] + '\t' + one_line[1] + '\t' + one_line[2] + '\t' + address + '\n'
							df.append(new_line)
							print(new_line)
				except TypeError:
					print('TypeError')
		

with open('theatres_address_new.tsv', 'w', encoding = 'utf-8') as w_file:
	for row in df:
		w_file.write(row)
