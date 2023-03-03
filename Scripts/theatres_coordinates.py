from geopy.geocoders import Nominatim
import csv

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
		coordinates.append('\n')
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

delim = '\t'
name = 'theatres_address.tsv'
table = extract_data(name, delim)
new_table = []
for line in table:
	coord = find_coordinates(line[3])
	new_line = line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + line[3] + '\t' + coord[0] + '\t' + coord[1] + '\n'
	new_table.append(new_line)
with open('theatres_coordinates.tsv', 'w', encoding = 'utf-8') as w_file:
	for row in new_table:
		for l in row:
			w_file.write(l)