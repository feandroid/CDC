import requests
import os

def download_geoapify_images(df, save_dir, api_key):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    base_url = "https://maps.geoapify.com/v1/staticmap"

    for idx, row in df.iterrows():
        lat, lon = row['lat'], row['long']
        
        params = {
            "apiKey": api_key,
            "style": "osm-bright",       
            "width": 224,                
            "height": 224,               
            "center": f"lonlat:{lon},{lat}", 
            "zoom": 18
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            with open(f"{save_dir}/{row['id']}.jpg", 'wb') as handler:
                handler.write(response.content)
            print(f"Saved: {row['id']}.jpg")
        else:
            print(f"Error for ID {row['id']}: {response.status_code} - {response.text}")

#the code below down was actually used on google colab

from google.colab import userdata
from google.colab import drive
drive.mount('/content/drive')

save_dir = "/content/drive/MyDrive/images"

api_key = userdata.get('geoapify_api_key')


download_geoapify_images(df, "/content/drive/MyDrive/images/", api_key)

