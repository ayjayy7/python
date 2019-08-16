items=[]
prices=[]
quantities=[]

item = input("item (enter done when finished): ")
items.append(item)

while item != 'done' :
	item = input("item (enter done when finished): ")
	price = input("price: ")
	quantity = input("quantity: ")
	#saving the inputs in a dictionary and appending it to the list of items
	items.append(item)
	prices.append(price)
	quantities.append(quantity)

x=0
tot=0

for x in list:
	print(quantity[x] , item[x] , tot)
	tot= tot + price[x]*quantity[x]
	
print("------------------ \n total: " , tot)