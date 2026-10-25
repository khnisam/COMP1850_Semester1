
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # your code here

    if float(amount) <= 0:
        return f"The converted value is: {0.0} {to_currency}"
    else:
        if from_currency == to_currency:
            return f"The converted value is: {float(amount):.2f} {to_currency}"
        else:
            rate = conversion_rate[from_currency][to_currency]
            result = float(amount) * rate
            rounded_result = round(result, 2)
            return f"The converted value is: {rounded_result} {to_currency}"


# Submit only this file currency_converter.py with the completed function.

print("GBP, CNY, PHP, INR")
from_currency = input("Please enter your current currency. The options are listed above.\n")
upper_from_currency = from_currency.upper()

amount = input("Please enter the amount you would like to convert ")

print("GBP, CNY, PHP, INR")
to_currency = input("Please enter what currency you would like to convert it to. The options are listed above. ")
upper_to_currency = to_currency.upper()

print(currency_converter(amount, upper_from_currency, upper_to_currency))



# Remove any additional code you may have added during development and testing.
