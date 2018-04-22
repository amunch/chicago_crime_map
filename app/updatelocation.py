import sys
import csv
import tweepy
from datetime import datetime,timedelta

class listener(tweepy.StreamListener):
    def on_status(self, status):
        text = status.text.encode('utf-8')
        timestamp = str(status.created_at)
        coor = status.geo
        t_id = str(status.id)
        print("hi")
        if coor != None:
            classify(text,timestamp,coor,t_id)
        return True

    def on_error(self, status):
        print(status)

def classify(text,timestamp,coor,t_id):
    iscrime = 1
    further_classify(timestamp,coor,t_id,iscrime)

def further_classify(timestamp,coor,t_id,iscrime):
    if iscrime:
        outputTweet(coor,timestamp)
    else:
        return

def outputTweet(coor,timestamp):
    filename = sys.argv[1]
    csvfile = open(filename, 'w+b')
    csv_reader = csv.reader(csvfile)
    csvfile.seek(0)
    for row in csv_reader:
        dt = datetime.strptime(row[3], "%a %b %d %H:%M:%S +0000 %Y")
        currenttime = datetime.now() - timedelta(hours=1) # time from hour ago
        if dt >= currenttime: # too old
            csvfile.write(row)
    writer = csv.writer(csvfile)
    writer.writerow([coor[0],coor[1],timestamp])
    print("yoooo")
    csvfile.truncate()
    csvfile.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need File in argument")
        exit(1)
    run_loop = True
    AUTH_KEY = '3zQlzwdC5DT8pRPVg5buxOYbc'
    AUTH_SECRET = '8ydzsbvclgExILxGCdaN9K24gP4sZMD5GsBMHv47BhonWkzTaI'
    ACCESS_TOKEN = '2317927801-ebLnR1nVkI55W6XJ30NqMUHE4cRM8zlHQe4njEM'
    ACCESS_SECRET = 'eaid7nfIcRy5iCzA6vpj85x1oSucFFYR9ZSoz2Wzgf6d3'
    auth = tweepy.OAuthHandler(AUTH_KEY, AUTH_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    stream_listener = listener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(locations=[-87.7219,41.7806,-87.6187,41.9130],async=True)
