#create a currency Converter...
import pprint
path = "C:/python work/estfolder/prices.txt"
with open(path) as f:
   lines = f.readlines()


pricedict = {}
for line in lines:
   parsed = line.split('\t')
   pricedict[parsed[0]] = parsed[1]
   
amount = int(input("Enter amount to convert: \n"))
pprint.pprint(pricedict.keys())
currency = input("Enter currency to calculate: \n")


if currency in pricedict:
   print(f"{amount} inr is = {amount * float(pricedict[currency])} {currency}.")











