swiss_prices = [11.98, 9.56, 189.78, 0.75, 1267.645]
for price in swiss_prices:
    euro_price = 0.86 * price
    print("price: %8.2f (%10.4f)" % (euro_price, euro_price))
print("Now with 'format'")
for price in swiss_prices:
    euro_price = 0.86 * price
    print("price: {0:8.2f} ({1:10.4f})".format(euro_price, euro_price))
