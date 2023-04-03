import csv
import requests

# Replace this with the URL you want to fetch JSON data from
url = 'https://www.dairyqueenthailand.com/mapen'

# Make a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Prepare CSV file
    with open('dairyqueen.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['lat', 'lng', 'address', 'type', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write data to CSV
        for item in data:
            lat = item['position']['lat']
            lng = item['position']['lng']
            address = item['position']['address']
            type = item['type']
            content = item['content']

            writer.writerow({
                'lat': lat,
                'lng': lng,
                'address': address,
                'type': type,
                'content': content
            })
else:
    print(f'Error: {response.status_code}')
