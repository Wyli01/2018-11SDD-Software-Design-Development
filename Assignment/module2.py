## order = {}  ## empty dictionary
import json

def insertOrder(order, name, choice):
    if name in orders:
        choices = orders[name]
        print(f"{name}, you have ordered these before : {choices}")
        choices.append(choice)
    else:
        choices =[choice]

        orders[name] = choices
        displayData(order)
    return orders

## input some data
def inputData(orders):
    while True:
        name = input("Name?")
        if name == "":
            break
        choice = input("Menu choice?")
        orders = insertOrder(orders, name, choice)
    return orders



## store it in a file
def storeData(orders):
    with open("data.text", 'w') as f:
        json.dump(orders, f)


## get it from file
def getData():
    try:
        with open("data.txt", 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
                orders = {}
    return orders

## display contents
def displayData(orders):
    print(orders)

orders = getData()
displayData(orders)
orders = inputData(orders)

storeData(orders)
displayData(orders)

