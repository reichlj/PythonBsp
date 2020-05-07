supermarket = {
   'milk': {'quantity':5 , 'price':1.19},
   'biscuits': {'quantity':13 , 'price':1.45},
   'butter': {'quantity':20 , 'price':2.29},
   'cheese': {'quantity':15 , 'price':1.9},
   'bread': {'quantity':10 , 'price':1.29},
   'apples': {'quantity':35 , 'price':3.15}
   
  }
print(supermarket)

customers = ['Frank', 'Mary', 'Paul', 'Jennifer']
print(customers)
shopping_list = {
   'Frank':[('cheese',4),('milk',5),('oranges',1),('apples',5),
            ('bananas',4),('yogurt',1),('cookies',1),('bread',0),
            ('butter',1),('biscuits',2)],
   'Mary':[('oranges',2),('butter',2),('bananas',4),('apples',1),
           ('cookies',2),('biscuits',1),('yogurt',4)],     
   'Paul':[('bread',3),('cheese',3),('milk',3),('cookies',4),
           ('bananas',1),('oranges',4)],
   'Jennifer':[('milk',4),('biscuits',4),('butter',3),('apples',3)]     
   }

print(shopping_list)
carts ={}
for customer in customers:
    carts[customer]= []
    for article,quantity in shopping_list[customer]:
        if article in supermarket:
            if supermarket[article]['quantity'] < quantity: 
                quantity = supermarket[article]['quantity'] 
            if quantity: 
                supermarket[article]['quantity'] -= quantity
                carts[customer].append((article,quantity))
for customer in carts:
    print('Checkout for', customer)
    total = 0.0
    for article, quantity in carts[customer]:
        item_price = supermarket[article]['price']
        price = quantity * item_price
        print('{0:3d} {1:20s} {2:8.2f} {3:8.2f}'.format(
                quantity,article,item_price,price))
        total += price
    print('total_sum {0:32.2f}'.format(total))
                 