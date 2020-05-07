shopping_list = ["milk", "egg", "butter", "cheese", "bread", "bananas"]
print(shopping_list)
cart = []
item = shopping_list.pop(1)
cart.append(item)
print(cart)
print(shopping_list)
cart.append(shopping_list.pop())
print(cart)
print(shopping_list)
