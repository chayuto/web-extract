import csv
from bs4 import BeautifulSoup

# Read the content of the HTML file
with open('data/mac.html', 'r', encoding='utf-8') as file:
    html = file.read()

# soup = BeautifulSoup(html, 'lxml')

soup = BeautifulSoup(html, 'html.parser')

# Find all store containers
store_containers = soup.find_all('a', class_='store-container')

# Prepare CSV file
with open('mcdonalds_locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'location', 'latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Extract and write data to CSV
    for store in store_containers:
        name = store.find('div', class_='name').text
        location = store.find('div', class_='address').text
        latitude = store['data-lat']
        longitude = store['data-lng']

        writer.writerow({'name': name, 'location': location, 'latitude': latitude, 'longitude': longitude})
