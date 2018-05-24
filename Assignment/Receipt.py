import json
import time
## dictionary for order ##
ordercheck = "yes";

Drinks = {
    "Coke" : 4.50,
    "Diet coke" : 4.50,
    "Sprite" : 4.50,
    "Asahi" : 12.75,
    "None" : 0.0,
           }

Mains = {
    "Margherita" : 14.00,
    "Napoletana" : 16.50,
    "Supreme" : 21.00,
    "Meat lovers" : 19.75,
    "Hawaiian" : 16.50,
          }


def printMenu():
        print("")
        print("=============== MENU ===============")
        count = 1
        print("")
        print("Drinks")
        for course in Drinks:
            price = Drinks[course]
            print(f" {course} - ${price}")
            count += 1
        print("")
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

### Defines Menu ###
menu = 'no'
while menu !=  ("i would like to order" in menu):
    menu = input("Would you like to Order or see the Menu? ").lower().strip()
    if ("i would like" in menu) or ("i want to" in menu):
     if ("order" in menu):
        print("Lets order shall we")
        break
    elif     ("menu" in menu):
     printMenu()
totalcost = 0
checkorder = "yes";
totalorder = "";
ordersmade = 0
while checkorder == "yes":
        order = input("What would you like for Mains friend? (Please be kind and enter 1 item in at a time)").lower().strip()
        if order == (""):
         if ("i want " in order):
            order = order.split("i want ", 1) [1];
            order = order.capitalize();
        if ("i would like " in order):
                      order = order.split("i would like " , 1) [1];
                      order = order.capitalize();
        if order in Mains:
                confirm = input(f"You have ordered {order}. Is this correct? ").lower().strip()
                if ("yes" in confirm):
                    cost = Mains[order]
                    totalcost += cost
                    ordercheckdrinks = "yes";
                    print(f"Thank's for ordering {order}, that will cost you ${cost}, and your total comes to ${totalcost}")
                    orderdrinks = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("Ooops... let's try again")
                    print("")
                    ordercheckdrinks ="no";
                else:
                    print(f"I guess that is a NO then")

                             ##Order Drinks####

                while ordercheckdrinks == "yes":

                     order = input("What Drink would you like? The key is one item at a time! ").lower().strip()
                     if order == "":
                      print("Ooops... it seems i have miss heard you could you please repeat that?")
                      print("")
                     if ("give me " in order):
                      order = order.split("give " , 1) [1];
                      order = order.capitalize();
                     if ("i would like " in order):
                      order = order.split("i would like " , 1) [1];
                      order = order.capitalize();
                     if ("i want " in order):
                      order = order.split("i want " , 1) [1];
                      order = order.capitalize();
                     if order in Drinks:
                       confirm = input(f"You have ordered {order}. Is this correct? ").lower().strip()
                       if ("yes" in confirm):
                           cost = Drinks[order]
                           totalcost += cost
                           print(f"Thank's for ordering {order}, that will cost you ${cost}, and your total comes to ${totalcost}")
                           ordermain = order.replace(" ", "@");
                           ordersmade = int(ordersmade) + 1;
                           checkorder = input("Would you like to order another meal? ").lower().strip()
                           if ("yes" in checkorder):
                             print("")
                             break
                           elif ordercheck == "no" and int(ordersmade) >= 3:
                             break
                           elif ordercheck == "no":
                            ordersleft = 3 - int(ordersmade);
                            time.sleep(1)
                            print("")
                            print(f"You must have at least three orders for home delivery please make {ordersleft} more orders to go.")
                            ordercheck = "yes";
                            print("")
                            break
                           else:
                             print("I guess that is a yes?")
                             ordercheck = "yes";
                     elif checkorder != "no" :
                      print("I'm sorry but that is not in the Available. Try saying 'i would like' or 'i want'  before you order.")
                      menucheck = input(f"Would you like to see the menu? ")
                     if ("yes" in menucheck):
                        printMenu();
                     else:
                        print("Let's try again");
        elif checkorder != "no":
                    print("I'm sorry but that is not in the Available. Try saying 'i would like' or 'i want'  before you order.")
                    print("")
                    menucheck = input(f"Would you need to see the menu? ")
                    if ("yes" in menucheck):
                       printMenu();
                    else:
                     print("")
        elif checkorder != "no":
                print("I'm sorry but that is not in the Available. Try saying 'i would like' or 'i want'  before you order.")
                print("")
                menucheck = input("--> Would you like to see the menu? ")
                if ("yes" in menucheck):
                    printMenu();
                else:
                    print("");

else:
   if checkorder == "yes":
    print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
    print("")
    menucheck = input(f"Would you like to see the menu? ")
    if ("yes" in menucheck):
     printMenu();
    else:
     print("");
   else:
     print("");

print("")
time.sleep(1);

if name == 0:
    lines.append(customername.lower())

import random
number = random.randint(5,60)
name = input("What is your name")
print("====================================")
print("               Receipt              ")
print("====================================")
print("Store Manager: Papa Giusepe")
print("Served By: Papa's Chat Bot")
print(f"Order name: {name}")
print(f"Weight time: {number} minutes")
print("")
print("Your order is:")
print(*order, sep = "\n")
print("")
print(f"the total cost comes to AUD${totalcost}")
print("")
print("------------------------------------")
print(f"Grazie, - {name}  for ordering with")
print("Papa's Chat Bot")
print("Hope enjoy!!!")
print("====================================")
print("           Papa's Pizzaria          ")
print("====================================")


def waittime():
 from random import randint

for i in range(len(lines)):
    if name.lower() in lines [i]:
        lines[i] = name.lower() + " " + order

opened = open("orderlists.text", 'w')
for i in lines:
    opened.write(i + "\n")

opened.close()





