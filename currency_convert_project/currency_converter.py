import requests

while True:
    from_currency: str = input("enter the currency you want to convert from ")
    to_currency: str = input("enter the currency you want to convert to ")
    try:
        amount = float(input("Enter the amount you want to convert: "))
        if amount < 0.0:
            print("The value cannot be negative.")
            continue
        else:
            break
    except ValueError:
        print("Enter a valid numeric value.")
        continue

url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

payload = {}
headers = {"apikey": "E1VcIH7ff1IjBNwbYcdTfFpSaUH9VmeW"}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.json()
convert_amount=result['result']
if status_code != 200:
    print("there is an error pleas try again later")
else:
    print(convert_amount)
