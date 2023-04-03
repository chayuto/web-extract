import csv
import requests
import json


# Read the content of the HTML file
with open('data/pizza1112_en.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    headers = data[0].keys()

    print(headers)
    # Write the data to a CSV file
    with open('pizza1112_en.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

