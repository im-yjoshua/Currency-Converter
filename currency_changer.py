import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def currency_converter():
    base_currency = input("Enter the base currency (e.g. USD): ").upper()
    target_currency = input("Enter the target currency (e.g. EUR): ").upper()
    amount  = float(input("Enter the amount: "))
    rate  = get_exchange_rate(base_currency, target_currency)
    convertedAmount  = amount * rate
    print(f"{amount} {base_currency} is equal to {convertedAmount:.2f} {target_currency}")

currency_converter()