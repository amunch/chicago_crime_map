import csv
import geocoder
import time

zip_crime = {}
max_crime = 0
MAX_THRESHOLD_ADJUST = 0.45

location_dict = {}
with open('locations.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        location_dict[(row[0], row[1])] = row[2]

with open('../scripts/crimezipcode.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        zip_crime[row[0]] = float(row[3])
        if float(row[3]) > max_crime:
            max_crime = float(row[3])

def adjust_threshold(geo):
    if geo in location_dict:
        postal = location_dict[geo]
    else: 
        g = geocoder.google(list(geo), method='reverse')
        while not g.ok:
            time.sleep(1)
            g = geocoder.google(list(geo), method='reverse')
    
        #print(g)
        postal = g.postal
    
        with open('locations.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([geo[0], geo[1], postal])

    #print(postal)       
    if postal in zip_crime:
        return 0.5 + MAX_THRESHOLD_ADJUST * (zip_crime[postal]/max_crime)
    else:
        return 0.5
