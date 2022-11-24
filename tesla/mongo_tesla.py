import pymongo

class mongo_operations():

    def __init__(self,hostname,port,database,collection):
        theclient= pymongo.MongoClient(f"mongodb://{hostname}:{port}/")
        mydb= theclient[database]
        self.mycol= mydb[collection]

    def pick_one(self,condition):
        y= self.mycol.find_one(condition)
        print(y) 


hostname = "localhost"
port = 27017
database = "prowess"
collection = "student"
mng_obj = mongo_operations(hostname,port,database,collection)
variable = mng_obj.pick_one({"name":"chaitu"})
print(variable)

