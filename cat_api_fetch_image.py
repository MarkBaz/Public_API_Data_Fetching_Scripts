import requests

url = "https://api.thecatapi.com/v1/images/search"

headers = {"x-api-key": "my-cat-api-key"}

params = {"limit": 5,"size": "medium"}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    cat_images = response.json()
    for image in cat_images:
    	image_url = image.get("url")
    	print(image_url)
else:
    print(f"Error fetching data: {response.status_code}")