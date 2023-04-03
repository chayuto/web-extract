import csv
import requests

# Replace this with the URL you want to fetch JSON data from
url = 'https://corporate.lotuss.com/location/json-data/'

# Make a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Extract 'data' from the response
    data = response_data["data"]

    # Get the headers (keys) for the CSV file
    headers = data[0].keys()

    # Write the data to a CSV file
    with open('lotus.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

else:
    print(f'Error: {response.status_code}')