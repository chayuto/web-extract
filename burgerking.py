import requests
import csv

# Replace this with the URL you want to fetch JSON data from
url = 'https://apibgk2.buzzebees.com/place?center=13.7451765,100.5081332&device_locale=1054&distance=150000000&mode=nearby&within_area=0&require_campaign=0&agencyId=7331'

# Make a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Prepare CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'id', 'latitude', 'longitude', 'address', 'working_day', 'name_en', 'address_en', 'working_day_en']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write data to CSV
        for item in data:
            name = item['name']
            id = item['id']
            latitude = item['location']['latitude']
            longitude = item['location']['longitude']
            address = item['address']
            working_day = item['working_day']
            name_en = item['name_en']
            address_en = item['address_en']
            working_day_en = item['working_day_en']

            writer.writerow({
                'name': name,
                'id': id,
                'latitude': latitude,
                'longitude': longitude,
                'address': address,
                'working_day': working_day,
                'name_en': name_en,
                'address_en': address_en,
                'working_day_en': working_day_en
            })
else:
    print(f'Error: {response.status_code}')
