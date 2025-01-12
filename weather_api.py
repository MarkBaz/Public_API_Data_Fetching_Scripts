import requests

url = "http://api.weatherapi.com/v1/forecast.json"

params = {"key": "a05c37dc841646eb832123824251101", "q": "Athens", "days": 5, "lang": "el"}

response = requests.get(url, params=params)

if response.status_code == 200:
    weather = response.json()
    location = weather["location"].get("name")
    print(f"Ο Καιρός για την τοποθεσία {location} τις επόμενες 5 ημέρες:")

    for day in weather["forecast"]["forecastday"]:

    	date = day["date"]
    	condition = day["day"]["condition"]["text"]
    	max_temp = day["day"]["maxtemp_c"]
    	min_temp = day["day"]["mintemp_c"]

    	print(f"{date}: {condition}")
    	print(f"  Μέγιστη Θερμοκρασία: {max_temp} C, Ελάχιστη Θερμοκρασία: {min_temp} C")
    	print("\n")
else:
    print(f"Error fetching data: {response.status_code}")