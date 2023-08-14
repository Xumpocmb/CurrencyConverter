import requests
import json

# response = requests.get(url='https://v6.exchangerate-api.com/v6/40bc0bdae61341100ad9584e/latest/USD')
# currencies = response.json().get('conversion_rates')
#
# with open('response.json', 'w') as file:
#     json.dump(response.json(), file, indent=4)
#
# with open('currencies.json', 'w') as file:
#     json.dump(currencies, file, indent=4)

with open('currencies.json', 'r') as file:
    currencies = json.load(file)

for currency in currencies:
    print(currency)
