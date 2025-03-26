import streamlit as st
import PIL
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
    apod_info = get_apod_info(base_url, token)

    st.title("NASA Picture of the Day")
    st.write("A token from NASA API is required, you can get it at: https://api.nasa.gov/")
    token = st.text_input("NASA token", token)
    
    st.image("default_img.jpg", caption='Aurora Borealis')
        
    if apod_info:
        copyright = apod_info['copyright']
        date = apod_info['date']
        media_type = apod_info['media_type']
        
        # From title retrieved, delete special characters
        title = re.sub("[^a-zA-Z0-9 ]+", "", apod_info['title'])
        explanation = apod_info['explanation']
        save_title_explanation(txt_path, title, explanation)
        
        # High definition image
        if media_type == 'image':
            try:
                url = apod_info['hdurl']
            except:
                url = apod_info['url']
            
            img_response = requests.get(url)
            with open(f"{image_path}/{title}.jpg", "rb") as file:
                btn = st.download_button(
                label="Download image",
                data=img_response.content,
                file_name=f"{title}.jpg",
                mime="image/jpg",
                )
            # file.write(img_response.content)
            
            
            
        ## UI



        
