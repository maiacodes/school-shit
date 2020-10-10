import urllib3
import json

http = urllib3.PoolManager()
response = http.request('GET', 'https://api.exchangeratesapi.io/latest?base=GBP')
currencies = json.loads(response.data)

toCurrency = input("What currency do you want to convert to? ").upper()
if not toCurrency in currencies['rates']:
    print("This isn't a valid currency")
    quit()

rate = currencies['rates'][toCurrency]

convert = input(f"How many GBP do you want to convert to {toCurrency}? £")

converstion = float(convert)*float(rate)
print("Your £" +convert+ " will be "+ str(int(converstion)) + f" {toCurrency}.")

if converstion >= 50:
    print("You would recieve "+str(int(converstion/50))+ " 50 notes")
    quit()

if converstion >= 20:
    print("You would recieve "+str(int(converstion/20))+ " 20 notes")
    quit()

if converstion >= 10:
    print("You would recieve "+str(int(converstion/10))+ " 10 notes")
    quit()

if converstion >= 5:
    print("You would recieve "+str(int(converstion/5))+ " 5 notes")
    quit()

