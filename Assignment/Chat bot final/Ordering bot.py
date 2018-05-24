##Variables

nameconfirm = "no";
question = "no";
question2 = "no";
cmenu = "no";
qconfirm = "no";
q1confirm = "no";
totalcost = 0
import json
import os
import time
import sys

### Menu ###

Drinks = {
    "Coke" : 4.50,
    "Diet coke" : 4.50,
    "Sprite" : 4.50,
    "Asahi" : 12.75,
    "No drinks" : 0.00,
           }
Mains = {
    "Margherita" : 14.00,
    "Napoletana" : 16.50,
    "Supreme pizza" : 21.00,
    "Meat lovers" : 19.75,
    "Hawaiian" : 16.50,
          }

def printMenu():
        print("")
        time.sleep(.4)
        print("=============== MENU ===============")
        count = 1
        print("")
        time.sleep(.3)
        print("Drinks")
        for course in Drinks:
            price = Drinks[course]
            print(f" {course} - ${price}")
            count += 1
        print("")
        time.sleep(.3)
        print("Mains")
        for course in Mains:
            price = Mains[course]
            print(f" {course} - ${price}")
        print("")
        print("")
        print("====================================")
        print("           Papa's Pizzaria          ")
        print("====================================")
        print("")


    ### Introduction ###
print("╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗     ╔═══╗╔══╗╔════╗╔════╗╔═══╗╔═══╗╔══╗╔═══╗")
time.sleep(.5)
print("║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║     ║╔═╗║╚╣─╝╚══╗═║╚══╗═║║╔═╗║║╔═╗║╚╣─╝║╔═╗║")
time.sleep(.4)
print("║╚═╝║║║─║║║╚═╝║║║─║║║╚══╗     ║╚═╝║─║║───╔╝╔╝──╔╝╔╝║║─║║║╚═╝║─║║─║║─║║")
time.sleep(.3)
print("║╔══╝║╚═╝║║╔══╝║╚═╝║╚══╗║     ║╔══╝─║║──╔╝╔╝──╔╝╔╝─║╚═╝║║╔╗╔╝─║║─║╚═╝║")
time.sleep(.2)
print("║║───║╔═╗║║║───║╔═╗║║╚═╝║     ║║───╔╣─╗╔╝═╚═╗╔╝═╚═╗║╔═╗║║║║╚╗╔╣─╗║╔═╗║")
time.sleep(.1)
print("╚╝───╚╝─╚╝╚╝───╚╝─╚╝╚═══╝     ╚╝───╚══╝╚════╝╚════╝╚╝─╚╝╚╝╚═╝╚══╝╚╝─╚╝")
time.sleep(.5)
time.sleep(1.5)
print("Ciao welcome to Papa's Pizzeria ordering system")
time.sleep(.5)
print("I am a chat bot designed by Papa Giuseppe to take your online orders")
time.sleep(.5)
print("Thus i will be taking your orders today :)")
time.sleep(1)
print("")

    ### Ask to Order food ###

while("i want to order food" not in question) or ("i want food" not in question):
    question = input("What do you want? use (i want food) ").lower()
    if ("i want food" in question) or ("i want to order food" in question):
        print("I thought you would like food :)")
        print("")
        break
    time.sleep(1)
else:
     print(f"I dont understand this - {question} - you ask of me")
     print("")
###########################################
     ### Ask for name ###

## Load
def getPreviousOrders():
        try:
                with open("order.txt","r") as f:
                        orders = json.load(f)
        except FileNotFoundError:
                orders = {}
        return orders

##########################################

## write to file
def writeOrders(q):
    with open('order.txt', 'w') as f:
        json.dump(q, f)
##########################################
def getName():
        while True:
            name = input("What is your name? please enter (My name is) ").lower().strip()
            if ("my name is" not in name):
             print("plz start again")
            else:
              searchText = "my name is"
              i = name.lower().find(searchText)
              x = i+len(searchText)
              name = name[x:].strip()
              nameconfirm = input(f"Your name is {name.title()}, yes? (Yes/No) ").lower()
              if ("yes" in nameconfirm) or ("ok" in nameconfirm):
                print("Great")
                break
              else:
                print("Oops... didnt match up please try again");
        return name
##########################################
def printOrderHistory(orders, name):
        if name == "":
                for name, pastOrder in orders.items():
                 print()
                 print(f"Previous orders for {name.title()}")
                for item in pastOrder:
                 print(f"-- {item}")
        elif name in orders:
                pastOrder = orders[name]
                print()
                print(f"Previous orders for {name.title()}")
                for item in pastOrder:
                 print(f"-- {item}")
                
print("")
previousOrder = getPreviousOrders()
totalcost = 0
count = 0
name = getName()
week = []

if name in previousOrder:
        print(f"Welcome back -- {name}!!! :)")
        printOrderHistory(previousOrder, name)
else:
        print("You have no previous orders")
print("")

######################################


     ### Ask to see Menu or Order ###
menu = 'no'
while menu !=  ("i would like to order" in menu):
    menu = input("Would you like to Order or see the Menu? (Please use [menu] or [i would like to order]) ").lower().strip()
    if ("i would like " in menu) or ("i want to" in menu):
     if ("order" in menu):
        print("Lets order shall we")
        break
    elif     ("menu" in menu):
     printMenu()
######################################
        ### order

Checkmenu = 'no'
week = []
totalcost = 0
ordercheck = "yes";
totalorder = "";
ordersmade = 0
time.sleep(0.05)

while ordercheck == "yes":
        order = input("What would you like for Mains friend? (Please be kind and enter 1 item in at a time)  ").lower().strip()
        if order == (""):
            time.sleep(.5)
        if ("i want a " in order):
            order = order.split("i want a ", 1) [1];
            order = order.capitalize();
        if ("i would like a " in order):
            order = order.split("i would like a ", 1) [1];
            order = order.capitalize();
            if order in Mains:
                confirm = input(f"You have ordered {order}. This correct? (Yes/No) ").lower().strip()
                if ("yes" in confirm):
                    cost = Mains[order]
                    totalcost += cost
                    week.append(order)
                    ordercheckdrink = "yes";
                    print(f"Thank you for ordering {order}, that will cost ${cost}, and your total is now ${totalcost}")
                    orderfood = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("Sorry let me try again")
                    print("")
                    ordercheckdrink ="no";
                else:
                    print(f"Ooops... it seems you said NO")

                              ####Order Drinks####

                while ordercheckdrink == "yes":
                     order = input("And what drink would you like with that meal? Remember one at a time! ").lower().strip()
                     if order == "":
                      print("I'm sorry i didn't quite hear what you said. Could you repeat that?")
                      print("")
                      time.sleep(.3)
                     if ("i want " in order):
                      order = order.split("i want " , 1) [1];
                      order = order.capitalize();
                     if ("i would like " in order):
                      order = order.split("i would like " , 1) [1];
                      order = order.capitalize();
                     if ("give me " in order):
                      order = order.split("give " , 1) [1];
                      order = order.capitalize();
                     if order in Drinks:
                       confirm = input(f"You ordered {order}. Is this correct? (Yes/No) ").lower().strip()
                       if ("yes" in confirm):
                           cost = Drinks[order]
                           totalcost += cost
                           week.append(order)
                           print(f"Thank you for ordering {order}, that will cost ${cost}, and your total is now ${totalcost} ")
                           orderdrink = order.replace(" ", "@");
                           meal = (f"{orderfood}+{orderdrink} ")
                           totalorder = (totalorder + meal);
                           ordersmade = int(ordersmade) + 1;
                           ordercheck = input("Would you like to order another meal? (Yes/No) ").lower().strip()
                           if ("yes" in ordercheck):
                             print("")
                             break
                           elif ordercheck == "no" and int(ordersmade) >= 3:
                             break
                           elif ordercheck == "no":
                            ordersleft = 3 - int(ordersmade);
                            time.sleep(.7)
                            print("")
                            print(f"You must have at least three orders for home delivery please make {ordersleft} more orders.")
                            ordercheck = "yes";
                            print("")
                            break
                           else:
                             print("Ooops... it seems you said yes")
                             ordercheck = "yes";
                     elif ordercheck != "no" :
                      print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                      menucheck = input(f"Would you like to see the menu? (Yes/NO) ")
                     if ("yes" in menucheck):
                        printMenu();
                     else:
                        print("Let's try again");
            elif ordercheck != "no":
                    print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                    print("")
                    menucheck = input(f"Would you like to see the menu? (Yes/No) ")
                    if ("yes" in menucheck):
                       printMenu();
                    else:
                     print("")
        elif ordercheck != "no":
                print("I'm sorry but that is not in the Menu. Try saying 'i would like a ' before what you want.")
                print("")
                menucheck = input("Would you like to see the menu? (Yes/No) ")
                if ("yes" in menucheck):
                    printMenu();
                else:
                    print("");

else:
   if ordercheck == "yes":
    print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
    print("")
    menucheck = input(f"Would you like to see the menu? (Yes/No) ")
    if ("yes" in menucheck):
     printMenu();
    else:
     print("");
   else:
     print("");

print("")
##################################################
## receipt

print("")
import random
number = random.randint(5,60)
time.sleep(2)
print("========================================")
time.sleep(.5)
print("                Receipt                 ")
print("========================================")
time.sleep(.3)
print("Store Manager: Papa Giusepe")
print("Served By: Papa G's Chat Bot")
time.sleep(.2)
print(f"Order name: {name.title()}")
print(f"Wait time: {number} minutes")
print("")
print(f"Order:")
print(*week, sep='\n')
print("")
print(f"the total cost comes to AUD${totalcost}")
print("")
time.sleep(.5)
print("----------------------------------------")
print(f"Grazie, - {name}  for ordering with")
print("Papa's Chat Bot")
print("Hope you enjoy!!!")
print("========================================")
print("               Papa's Pizzaria          ")
print("========================================")
print("")
print("")

#time.sleep(10)
#print(previousOrder)
#previousWeek = previousOrder[name]
#print(previousWeek)
#print(name)

previousOrder[name] = week #previousWeek
#print(previousOrder)
writeOrders(previousOrder)
time.sleep(1)


br = input("Please PRESS ENTER to end the call")
sys.exit()


