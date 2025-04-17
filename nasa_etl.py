import requests
import pandas as pd
import json
from datetime import datetime,  timedelta
import os

#NASA API key
nasa_api_key= os.getenv("NASA_API_KEY") 

#Dates
end_date = datetime.today().date()
start_date = end_date - timedelta(days=199) #This will get the data of last 200 days

#API URL
url =(  
      f"https://api.nasa.gov/planetary/apod?"
      f"api_key={nasa_api_key}&start_date={start_date}&end_date={end_date}"
      )

#API Call
response = requests.get(url)
data = response.json()

#Transforming Data into DataFrame
record = []
for entry in data:
    record.append({
        'date': entry.get('date'),
        'title': entry.get('title'),
        'explanation': entry.get('explanation'),
        'url': entry.get('url'),
        'hdurl': entry.get('hdurl'),
        'media_type': entry.get('media_type')
})

df = pd.DataFrame(record)
df.to_csv("Nasa_records.csv", index=False)


