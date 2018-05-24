import json
import time
import os
## dictionary for order ##
ordercheck = "yes";

Drinks = {
    "Coke" : 4.50,
    "Diet coke" : 4.50,
    "Sprite" : 4.50,
    "Asahi" : 12.75,
    "No drinks" : 0.00,
           }
Entre = {
 "Garlic bread" : 7.50,
 "Garlic pizza" : 10.50,
 "Antipasto salad" : 9.00,
 "No entre" : 0.00,
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
        print("=============== MENU ===============")
        count = 1
        print("")
        print("Drinks")
        for course in Drinks:
            price = Drinks[course]
            print(f" {course} - ${price}")
            count += 1
        print("")
        print("Entre")
        for course in Entre:
            price = Entre[course]
            print(f" {course} - ${price}")
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
menu = 'no'
while menu !=  ("i would like to order" in menu):
    menu = input("Would you like to Order or see the Menu? ").lower().strip()
    if ("i would like" in menu) or ("i want to" in menu):
     if ("order" in menu):
        print("Lets order shall we")
        print("")
        break
    elif     ("menu" in menu):
     printMenu()
     print("")

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
                confirm = input(f"--> You have ordered {order}. This correct? [Yes/No] ").lower().strip()
                if ("yes" in confirm):
                    cost = Mains[order]
                    totalcost += cost
                    orderentre = "yes";
                    print(f"--> Thank you for ordering {order}, that will cost {cost}, and your total is now {totalcost}")
                    orderfoodM = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("--> Sorry let me try again")
                    print("")
                    orderentre ="no";
                else:
                    print(f"--> I'll uhhh... I'll take that as a no then")

                              ####Order Drinks####
                while orderentre == "yes":
                    order = input("What would you like for Entre friend? (Please be kind and enter 1 item in at a time)  ").lower().strip()
                    if order == (""):
                        time.sleep(.5)
                    if ("i want a " in order):
                        order = order.split("i want a ", 1) [1];
                        order = order.capitalize();
                    if ("i would like a " in order):
                        order = order.split("i would like a ", 1) [1];
                        order = order.capitalize();
                        if order in Entre:
                            confirm = input(f"--> You have ordered {order}. This correct? [Yes/No] ").lower().strip()
                            if ("yes" in confirm):
                                cost = Entre[order]
                                totalcost += cost
                                ordercheckdrink = "yes";
                                print(f"--> Thank you for ordering {order}, that will cost {cost}, and your total is now {totalcost}")
                                orderfoodE = order.replace(" ", "@")
                                print("")
                            elif ("no" in confirm):
                                print("--> Sorry let me try again")
                                print("")
                                ordercheckdrink ="no";
                            else:
                                print(f"--> I'll uhhh... I'll take that as a no then")

                      ##################
                while ordercheckdrink == "yes":
                     order = input("--> And what drink would you like with that meal? Remember one at a time! ").lower().strip()
                     if order == "":
                      print("--> I'm sorry i didn't quite hear what you said. Could you repeat that?")
                      print("")
                      time.sleep(.5)
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
                       confirm = input(f"--> You ordered {order}. Is this correct? [Yes/No] ").lower().strip()
                       if ("yes" in confirm):
                           cost = Drinks[order]
                           totalcost += cost
                           print(f"--> Thank you for ordering {order}, that will cost {cost}, and your total is now {totalcost} ")
                           orderdrink = order.replace(" ", "@");
                           meal = (f"{orderfoodE}+{orderfoodM}+{orderdrink} ")
                           totalorder = (totalorder + meal);
                           ordersmade = int(ordersmade) + 1;
                           ordercheck = input("--> Would you like to order another meal? [Yes/No] ").lower().strip()
                           if ("yes" in ordercheck):
                             print("")
                             break
                           elif ordercheck == "no" and int(ordersmade) >= 3:
                             break
                           elif ordercheck == "no":
                            ordersleft = 3 - int(ordersmade);
                            time.sleep(1)
                            print("")
                            print(f"You must have at least three orders for home delivery please make {ordersleft} more orders.")
                            ordercheck = "yes";
                            print("")
                            break
                           else:
                             print("Uhh... I'll take that as a yes?")
                             ordercheck = "yes";
                     elif ordercheck != "no" :
                      print("--> I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                      menucheck = input(f"--> Would you like to see the menu? ")
                     if ("yes" in menucheck):
                        printMenu();
                     else:
                        print("Let's try again");
            elif ordercheck != "no":
                    print("--> I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                    print("")
                    menucheck = input(f"--> Would you like to see the menu? ")
                    if ("yes" in menucheck):
                       printMenu();
                    else:
                     print("")
        elif ordercheck != "no":
                print("--> I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                print("")
                menucheck = input("--> Would you like to see the menu? ")
                if ("yes" in menucheck):
                    printMenu();
                else:
                    print("");

else:
   if ordercheck == "yes":
    print("--> I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
    print("")
    menucheck = input(f"--> Would you like to see the menu? ")
    if ("yes" in menucheck):
     printMenu();
    else:
     print("");
   else:
     print("");


print("")
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

while confirmingorder == 'no':
 corder = input("You are happy with this order yes?").lower().strip()
 if("yes" in corder) or("i am happy" in corder):
    print("Perfect")
    break
 else:
  if ('no' in corder):
    print("Back to the top we go :(")
    os.execl(sys.executable, sys.executable, *sys.argv)
def waittime():
 from random import randint


