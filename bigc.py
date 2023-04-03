import csv
import requests

# Replace this with the URL you want to fetch JSON data from
url = 'https://corporate.bigc.co.th/include/markers'

# Make a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Convert Unicode strings to Thai language
    # for item in data:
    #     for key, value in item.items():
    #         if isinstance(value, str):
    #             item[key] = value.encode('utf-8').decode('unicode_escape')

    # Get the headers (keys) for the CSV file
    headers = data[0].keys()

    # Write the data to a CSV file
    with open('bigc.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

else:
    print(f'Error: {response.status_code}')
