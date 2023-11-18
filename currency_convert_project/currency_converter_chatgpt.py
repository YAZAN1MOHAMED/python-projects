#when it comes to dealing with API chat gpt did not preform well so I asked it to improve my code only


import requests

# Prompt for currency input in a loop until valid input is provided
while True:
    from_currency: str = input("Enter the currency you want to convert from: ")
    to_currency: str = input("Enter the currency you want to convert to: ")
    
    try:
        # Prompt for a valid numeric amount, ensuring it's not negative
        amount = float(input("Enter the amount you want to convert: "))
        if amount < 0.0:
            print("The value cannot be negative.")
            continue
        else:
            break
    except ValueError:
        print("Enter a valid numeric value.")
        continue

# Build the API URL for currency conversion
url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers = {"apikey": "E1VcIH7ff1IjBNwbYcdTfFpSaUH9VmeW"}

# Make the API request
response = requests.get(url, headers=headers, data=payload)

# Extract response status code and result
status_code = response.status_code
result = response.json()
convert_amount = result.get('result', None)

# Check for errors in the response
if status_code != 200:
    print("There is an error, please try again later.")
else:
    print(convert_amount)
