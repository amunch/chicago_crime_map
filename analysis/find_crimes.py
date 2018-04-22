import csv
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians

tweet_txt = open('../data/crime_text.txt', 'wb')

def find_centroid(geo):
    fixed = geo.replace(' ','').split(',')
    lat = 0
    lon = 0
    for index, i in enumerate(fixed):
        if index%2 == 0:
            lon += float(i)
        else:
            lat += float(i)

    return(lat/4, lon/4)

def geo_distance(geo1, geo2):
    geo1 = geo1.replace('(', '').replace(')', '').replace(' ', '').split(',')
    
    R = 6373.0

    lat1 = radians(float(geo1[0]))
    lon1 = radians(float(geo1[1]))
    lat2 = radians(float(geo2[0]))
    lon2 = radians(float(geo2[1]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def find_tweets(dt, geo, tweets):
    for i in tweets:
        diff = abs((dt - i[2]).total_seconds())
        if diff < 3600:
            if geo_distance(geo, i[1]) < 5:
                tweet_txt.write(i[0] + '\n')
                

tweets = []
with open('../data/chicago_geo.csv', 'rb') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        geo = (row[1], row[2])
        dt = datetime.strptime(row[3], "%a %b %d %H:%M:%S +0000 %Y")
        tweets.append([row[0], tuple(geo), dt])

with open('../data/crimes.csv', 'rb') as csvfile:
    csv_reader = csv.reader(csvfile)
    for i, row in enumerate(csv_reader):
        print(row)
        if row[1][0:4] == 'DATE':
            continue
        dt = datetime.strptime(row[1], "%m/%d/%Y %I:%M:%S %p")
        if row[16] != '':
            find_tweets(dt, row[16], tweets)
