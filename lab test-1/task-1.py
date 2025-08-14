def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported.")
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

currency_rates = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.93,
    'GBP': 0.79,
    'JPY': 157.0
}

amount = float(input("Enter the amount to convert: "))
from_curr = input("Enter the currency code of the amount (e.g., USD, INR): ").upper()
to_curr = input("Enter the currency code to convert to (e.g., USD, INR): ").upper()

try:
    result = convert_currency(amount, from_curr, to_curr, currency_rates)
    print(f"{amount} {from_curr} is equal to {result:.2f} {to_curr}")
except ValueError as e:
    print(e)