menu = {
    "pizza" : 3.40,
    "tacos" : 5.50,
    "curry Chicken" : 13.00
}

nigger = input("bonjour cest moi si papi how are you?")

print("menu")
for item in menu:
        price = menu[item]
        print(f"> {item} - ${price}")

totalcost = 0
while True:
    order = input("what do you want to eat?").lower().strip()
    order.split(" ")[0]
    if order =="":
        break
    if order in menu:
        cost = menu[order]
        totalcost += cost
        print(f"Thanks for ordering at Papa's Pizzaria your order is - {order}, that will cost {cost}, and your total cost comes to {totalcost}")
    else:
        print(f"What!! {order} is not on the menu!!")
        if totalcost > 0:
            print(f"Thanks... you now owe me ${totalcost}")