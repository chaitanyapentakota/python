from urllib.request import urlopen
import json
import pymongo

myclient= pymongo.MongoClient("mongodb://localhost:27017/")

mydb= myclient["covid"]

mycol = mydb["cases"]



url = "https://api.covidtracking.com/v1/us/daily.json"
response = urlopen(url)
j = json.load(response)
print(j)

for collection in j:
    print(collection)
    mycol.insert_many(j)