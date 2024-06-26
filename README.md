# Currency Converter

This Python script converts an amount from one currency to another using real-time exchange rates from ExchangeRate-API.

## Features

- Fetches the latest exchange rates.
- Converts an amount from a base currency to a target currency.

## Usage

### Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

### Instructions

1. Clone this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python.


```bash
python currency_converter.py
```
4. Follow the prompts to enter the base currency, target currency, and the amount to convert.

```
Enter the base currency (e.g. USD): USD
Enter the target currency (e.g. EUR): EUR
Enter the amount: 100
100 USD is equal to 90.00 EUR
```

# Code 

```python 
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def currency_converter():
    base_currency = input("Enter the base currency (e.g. USD): ").upper()
    target_currency = input("Enter the target currency (e.g. EUR): ").upper()
    amount = float(input("Enter the amount: "))
    rate = get_exchange_rate(base_currency, target_currency)
    convertedAmount = amount * rate
    print(f"{amount} {base_currency} is equal to {convertedAmount:.2f} {target_currency}")

currency_converter()

```

# Improvements
1. **Error Handling**: Implement error handling to manage network issues, invalid inputs, and other potential errors.
2. **API Key Management**: If an API key is required, ensure it is securely managed and not hard-coded in the script.
3. **Code Readability**: Improve readability by following PEP 8 guidelines and adding comments.

# License

This project is licensed under the MIT License.
