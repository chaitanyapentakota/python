import pymongo

myclient= pymongo.MongoClient("mongodb://localhost:27017/")

mydb= myclient["prowess"]

#print(myclient.list_database_names())

mycol = mydb["employee"]
#print(mydb.list_collection_names())
myquery= {"lang":"python"}
newvalue={"$set":{"lang":"c"}}
mycol.update_one(myquery,newvalue)
for x in mycol.find():
    print(x)
