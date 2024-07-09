import pandas as pd
import requests

url = "https://api.msrc.microsoft.com/cvrf/v3.0/updates" # URL for the Microsoft Security Response Center API
update_string = '2022' # String to filter for updates
response = requests.get(url) # Make a GET request to the API
# Check if the request was successful
if response.status_code == 200:
    data = response.json() # Parse the JSON response
    updates_filtered = [entry for entry in data['value'] if update_string in entry['DocumentTitle']] # Filter for SharePoint-related updates
    df_all_updates = pd.DataFrame(data['value']) # Convert all updates to DataFrame
    df_all_updates.to_excel("updates_all.xlsx", index=False) # Save to Excel
    df_filtered = pd.DataFrame(updates_filtered) # Convert to DataFrame
    df_filtered.to_excel("updates_filtered.xlsx", index=False) # Save to Excel

else:
    print("Failed to fetch data. Status code:", response.status_code) # Print an error message
