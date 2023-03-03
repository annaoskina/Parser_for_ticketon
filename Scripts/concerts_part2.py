import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import csv
import re

def find_coordinates(address):
	geolocator = Nominatim(user_agent='annaoskina@gmail.com')
	location = geolocator.geocode(address)
	try:
		lat = location.latitude
		lon = location.longitude
		coordinates = []
		#coordinates.append('\t')
		coordinates.append(str(lat))
		#coordinates.append('\t')
		coordinates.append(str(lon))
		#print(coordinates)
	except AttributeError:
		print(address)
	return coordinates

def extract_data(name_csv, delim):
    with open(name_csv, encoding = 'utf-8') as r_file:
        data = csv.reader(r_file, delimiter = delim)
        data_list = list(data)
        #print(data_list)
    return data_list

def make_soup(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'lxml') # If this line causes an error, run 'pip install html5lib' or install html5lib
	#little_soup = soup.find_all("h3")
	#href = little_soup['href']
	return soup

def write_csv(df, name):
	with open('{}.tsv'.format(name), 'w', encoding = 'utf-8') as w_file:
		for row in df:
			for line in row:
				w_file.write(line)


def find_address(soup):
	divs_active = soup.find_all('div', class_='b-text')
	for divs in divs_active:
		ps = divs.find('p')
		try:
			for p in ps:
				result = re.findall('г. Алматы.*', p)
				if result:
					address = result[0].strip('г. ')
					print(address)
		except TypeError:
			print('TypeError')
	return address

delim = '\t'
name = 'concerthalls_with_address.tsv'
table = extract_data(name, delim)
concerthalls_coord = []
for line in table:
	address = line[3]
	try:
		coordinates = find_coordinates(address)
		new_line = line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + coordinates[0] + '\t' + coordinates[1] + '\n'
		concerthalls_coord.append(new_line)
	except UnboundLocalError:
		print(line[3])


name = 'concerthalls_with_coord'
write_csv(concerthalls_coord, name)
