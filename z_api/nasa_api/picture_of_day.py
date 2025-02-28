import json
import requests
import re
import os

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

def save_title_explanation(output_path, title, explanation):
    with open(output_path, "a") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Explanation: \n")
        rows = 7
        max_length = int(len(explanation) / rows)
        start = 0
        end = max_length
        for row in range(rows+1):
            file.write(f"{explanation[start:end]}\n")
            start = end
            end += max_length
        file.write(f"\n")
        
if __name__ == "__main__":
    base_url = "https://api.nasa.gov/planetary/apod?api_key"
    file_path = "config_private.json"
    token, image_path = read_token_path(file_path)
    txt_path = image_path + "/information.txt"
    # if not os.path.isfile(txt_path):
    #     os.mkfile(txt_path)
    print(txt_path)
    apod_info = get_apod_info(base_url, token)
    
    if apod_info:
        # print(apod_info)
        # From title retrieved, delete special characters
        title = re.sub("[^a-zA-Z0-9 ]+", "", apod_info['title'])
        explanation = apod_info['explanation']
        save_title_explanation(txt_path, title, explanation)
        
        # High definition image
        hdurl = apod_info['hdurl']
        img_response = requests.get(hdurl)
        with open(f"{image_path}/{title}.jpg", "wb") as file:
            file.write(img_response.content)




