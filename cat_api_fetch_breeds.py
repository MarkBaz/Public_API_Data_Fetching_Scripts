import requests

url = "https://api.thecatapi.com/v1/breeds"

headers = {"x-api-key": "my-cat-api-key"}

params = {"limit": 5}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    cat_breeds = response.json()
    for index, breed in enumerate(cat_breeds, start=1):

    	name = breed.get("name")
    	origin = breed.get("origin")
    	description = breed.get("description")
    	temperament = breed.get("temperament")

    	print(f"Cat {index} Information:")
    	print(f"Breed: {name}")
    	print(f"Temperament: {temperament}")
    	print(f"Origin: {origin}")
    	print(f"Description: {description}")
    	print("\n")
else:
    print(f"Error fetching data: {response.status_code}")