from urllib.request import urlopen
import json
url = "https://api.covidtracking.com/v1/us/daily.json"
response = urlopen(url)
j = json.load(response)
#print(j)
print(json.dumps(j, indent = 1))
'''n = 0
cases = 0
for i in j:
    if (j[n])['state'] == 'CA':
        print(j[n])
        cases += (j[n])['positiveIncrease']
    else:
         n += 1
         continue
    n += 1
print(cases)'''