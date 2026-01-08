import requests
import os

df = pd.read_excel('/content/sample_data/train(1).xlsx')
df1 = pd.read_excel('/content/sample_data/test2.xlsx')
numeric_cols = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'grade', 'condition','floors','waterfront','view','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','sqft_living15','sqft_lot15']

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
df1[numeric_cols] = df1[numeric_cols].fillna(df1[numeric_cols].median())

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
download_geoapify_images(df1, "/content/drive/MyDrive/images/", api_key)


