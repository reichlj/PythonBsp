swiss_prices = [11.98, 9.56, 189.78, 0.75, 1267.645]

for price in swiss_prices:
    print("price: {swiss:8.2f} ({swiss:10.4f})".format(swiss=0.86*price))
print("Now with 'f-string'")
for price in swiss_prices:
    print(f"price: {0.81*price:8.2f} ({0.81*price:10.4f})")
