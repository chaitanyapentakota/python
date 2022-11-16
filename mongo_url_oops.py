from urllib.request import urlopen
import json
import pymongo

class mongo_url_operations():
    def __init__(self,hostname,port,database,collection):
        theclient= pymongo.MongoClient(f"mongodb://{hostname}:{port}/")
        mydb= theclient[database]
        self.mycol= mydb[collection]      

    def put_all(self):
        for collection in j:
            self.mycol.insert_one(collection)

hostname = "localhost"
port = 27017
database = "covid"
collection = "cases"        


url = "https://api.covidtracking.com/v1/us/daily.json"
response = urlopen(url)
j = json.load(response)


mng_obj = mongo_url_operations(hostname,port,database,collection)
retrun_variable = mng_obj.put_all()
print(retrun_variable)