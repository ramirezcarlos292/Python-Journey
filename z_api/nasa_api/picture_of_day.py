import json
import requests
import re

# read token from file
def read_token_path(file_path):
    try:
        with open(file_path, "r") as file:
            content = json.load(file)
            token = content['token']
            img_path = content['path_images']
            return token, img_path
    except FileNotFoundError:
        print("token file was not found")
        
def get_apod_info(base_url, token):
    url = f"{base_url}={token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data {response.status_code}")


if __name__ == "__main__":
    base_url = "https://api.nasa.gov/planetary/apod?api_key"
    file_path = "config_private.json"
    token, image_path = read_token_path(file_path)
    apod_info = get_apod_info(base_url, token)
    
    if apod_info:
        # From title retrieved, delete special characters
        title = re.sub("[^a-zA-Z0-9 ]+", "", apod_info['title'])
        # High definition image
        hdurl = apod_info['hdurl']
        img_response = requests.get(hdurl)
        with open(f"{image_path}/{title}.jpg", "wb") as file:
            file.write(img_response.content)




