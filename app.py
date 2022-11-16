import requests

api_key = 'ae56901d67ea313e3424442581ff58c7'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/3.0/onecall?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
#print(weather_data.status_code)    



