from re import T
from urllib import response
import requests

class tesla_url():
    def __init__(self,base_url,Bearer_token):
        base_url = urls
        Bearer_token = token
       
       
    def list_all_vehicles(self):
        response = requests.get(url_1,headers={'Authorization':token})
        print(response.content)

    def charge_state(self):
        response = requests.get(url_2,headers={'Authorization':token})
        print(response.content)

    def vehicle_state(self):
        response = requests.get(url_3,headers={'Authorization':token})
        print(response.content)

    def drive_and_position(self):
        response = requests.get(url_4,headers={'Authorization':token})
        print(response.content)



url_1 = 'https://owner-api.teslamotors.com/api/1/vehicles'
url_2 = 'https://owner-api.teslamotors.com/api/1/vehicles/1492932163186321/data_request/charge_state'
url_3 = 'https://owner-api.teslamotors.com/api/1/vehicles/1492932163186321/data_request/vehicle_state'
url_4 = 'https://owner-api.teslamotors.com/api/1/vehicles/1492932163186321/data_request/drive_state'
urls = url_1,url_2,url_3,url_4
token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR3bjV2bmNQUHhYNmprc2w5SUYyNnF4VVFfdyJ9.eyJpc3MiOiJodHRwczovL2F1dGgudGVzbGEuY29tL29hdXRoMi92MyIsImF1ZCI6WyJodHRwczovL293bmVyLWFwaS50ZXNsYW1vdG9ycy5jb20vIiwiaHR0cHM6Ly9hdXRoLnRlc2xhLmNvbS9vYXV0aDIvdjMvdXNlcmluZm8iXSwiYXpwIjoib3duZXJhcGkiLCJzdWIiOiIyOTY0OTYyYy03NWYwLTRhMDMtYjk4Yi00MzE3OTcwMjUxMWMiLCJzY3AiOlsib3BlbmlkIiwiZW1haWwiLCJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsicHdkIl0sImV4cCI6MTY2NjE4NjQ4MiwiaWF0IjoxNjY2MTU3NjgyLCJhdXRoX3RpbWUiOjE2NjI0NjM1Mzh9.vTxe57KznfxWHhBFxeSRaxSvBfSxdZymq_7pmhjSij6GqAiuWxPidah_tIos6aMWesgaKwiqrkg9OTLdgu4oktyWj1YpfReW2pq0ec23XS3XpNpFsDTcYLCsJLaikun4-E39J7_qkW2srVQ5WD4fJvjiLfsnOqWKmRTfgGzDSHjWgSad4bqJuamCwsPRbRnuDzqCPSJZlZLe5nAr2zzmrry_faDHo6m5cYD9cyg7Amwsci9te1_7LR01PtVXgsh6KbFETs4EEDckcRVryhRU47X8zY4QIGLJhPloX13V6LkpAkDtbijHfTjExXZ-AM1MCz-KP_oF5-TVmoUQ7xAO5Q'

tesla_oper = tesla_url(urls,token)
output = int(input("which operation do u want:"))
if output == 1:
    return_variable = tesla_oper.list_all_vehicles()
elif output == 2:
    return_variable = tesla_oper.charge_state()
elif output == 3:
    return_variable = tesla_oper.vehicle_state()
else:
    return_variable = tesla_oper.drive_and_position()     

print(return_variable)
