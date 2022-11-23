import requests
API_KEY="7b0a92831df3648617a9eb3d1c71c160"
BASE_URL ="https://api.openweathermap.org/data/2.5/weather"

city =input("Enter a city name:")
request_url =f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code == 200:
    data=response.json()
    #print(data)
    weather=data['weather'][0]['description']
    print(weather)
    temperature=round(data["main"]["temp"]- 273.15,2)
    print(temperature)
else:
    print("An error occured!")


