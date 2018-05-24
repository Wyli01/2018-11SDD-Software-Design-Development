import json
order = input("Food?")
name= input("name?")
.append(name)
.append(order)
with open("orders.txt", 'w') as f:
    json.dump(order,f)
    json.dump(name,f)

#with open("orders.txt", 'r') as f:
    #new_orders = json.load(f)

#print(new_orders)