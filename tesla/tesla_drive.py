from urllib import response
import pymongo
import requests
import json


class tesla_url():

    def __init__(self,hostname,port,database,collection,url_4,token):
        theclient= pymongo.MongoClient(f"mongodb://{hostname}:{port}/")
        mydb= theclient[database]
        self.mycol= mydb[collection]

    def drive_and_position(self):
        response = requests.get(url_4,headers={'Authorization':token})
        print(response.content) 
        

               
hostname = "localhost"
port = 27017
database = "tesla"
collection = "drive_position"
url_4 = 'https://owner-api.teslamotors.com/api/1/vehicles/1492932163186321/data_request/drive_state'
token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5ZdVZJWTJTN3gxVHRYM01KMC1QMDJad3pXQSJ9.eyJpc3MiOiJodHRwczovL2F1dGgudGVzbGEuY29tL29hdXRoMi92MyIsImF1ZCI6WyJodHRwczovL293bmVyLWFwaS50ZXNsYW1vdG9ycy5jb20vIiwiaHR0cHM6Ly9hdXRoLnRlc2xhLmNvbS9vYXV0aDIvdjMvdXNlcmluZm8iXSwiYXpwIjoib3duZXJhcGkiLCJzdWIiOiIyOTY0OTYyYy03NWYwLTRhMDMtYjk4Yi00MzE3OTcwMjUxMWMiLCJzY3AiOlsib3BlbmlkIiwiZW1haWwiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl0sImV4cCI6MTY2Njk0Mjc0NSwiaWF0IjoxNjY2OTEzOTQ1LCJhdXRoX3RpbWUiOjE2NjY3MTEwMjJ9.tmUbeWKVE7PdO3CdUFqfOgRStg_KVAKkDQMZO61lOxkPVu2nL9SpGQeCDnnx1IiR5SxnvwAfk6-NlFINFeNAVdWYW7mOPbXmylRSsIyuPkkfiM1xZwd2RGRhmylfwshlH1vwQb32Ufasv0c3IbJeOuz6JmkE-Mucqd8OcBBtkBdRtTGuuUersVytGqY9s4iL6gndRkJQjtVlsZe9CdV3blHNdV1MQfa4RBuw8kG18r2k3oXSeDlopi7st7cUdDgQnE8KhghxpUNAidjH7WLMbLKWyG05LVeeguMVuNjpSeo-75lUeje6mdDIqzwoqFWm5XA1CDwj9NLNhjgfDVotVA'
mng_obj = tesla_url(hostname,port,database,collection,url_4,token)
mng_obj.drive_and_position()
'''return_variable = mng_obj.drive_and_position()
print(return_variable)'''