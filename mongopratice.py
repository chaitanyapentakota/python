from dataclasses import dataclass
from msilib.schema import Condition
from re import X
from unicodedata import name
import pymongo



class mongo_operations():
    
    def __init__(self,hostname,port,database,collection):
        theclient= pymongo.MongoClient(f"mongodb://{hostname}:{port}/")
        mydb= theclient[database]
        self.mycol= mydb[collection]        

    def pick_one(self,condition):         
        y= self.mycol.find_one(condition)
        print(y)
        
    def pick_all(self):
        x=self.mycol.find()
        return[i for i in x]
        
    
hostname = "localhost"
port = 27017
database = "prowess"
collection = "student"

mng_obj = mongo_operations(hostname,port,database,collection)
mng_obj.pick_one({"name":"chaitu"})
mng_obj.pick_one({"class":10})
retrun_variable = mng_obj.pick_all()
print (retrun_variable)