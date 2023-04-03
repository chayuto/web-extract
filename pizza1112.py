import csv
import requests

# Replace this with the URL you want to fetch JSON data from
url = 'https://api2.1112.com/api/v1/store-service?store_type=RBD,DLC,DWS,FSR'

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,th-TH;q=0.8,th;q=0.7,fr;q=0.6",
    "dnt": "1",
    "language": "th",
    "origin": "https://1112.com",
    "referer": "https://1112.com/"
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    headers = data[0].keys()

    print(headers)
    # Write the data to a CSV file
    with open('pizza1112_en.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

else:
    print(f'Error: {response.status_code}')
