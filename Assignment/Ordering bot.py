import time
##Variables

nameconfirm = "no";
question = "no";
question2 = "no";
cmenu = "no";
qconfirm = "no";
q1confirm = "no";
totalcost = 0
import json
### Menu ###

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
 }
Mains = {
    "Margherita pizza" : 14.00,
    "Napoletana pizza" : 16.50,
    "Supreme pizza" : 21.00,
    "Meat lovers" : 19.75,
    "Hawaiian pizza" : 16.50,
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


    ### Introduction ###
print("╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗     ╔═══╗╔══╗╔════╗╔════╗╔═══╗╔═══╗╔══╗╔═══╗")
print("║╔═╗║║╔═╗║║╔═╗║║╔═╗║║╔═╗║     ║╔═╗║╚╣─╝╚══╗═║╚══╗═║║╔═╗║║╔═╗║╚╣─╝║╔═╗║")
print("║╚═╝║║║─║║║╚═╝║║║─║║║╚══╗     ║╚═╝║─║║───╔╝╔╝──╔╝╔╝║║─║║║╚═╝║─║║─║║─║║")
print("║╔══╝║╚═╝║║╔══╝║╚═╝║╚══╗║     ║╔══╝─║║──╔╝╔╝──╔╝╔╝─║╚═╝║║╔╗╔╝─║║─║╚═╝║")
print("║║───║╔═╗║║║───║╔═╗║║╚═╝║     ║║───╔╣─╗╔╝═╚═╗╔╝═╚═╗║╔═╗║║║║╚╗╔╣─╗║╔═╗║")
print("╚╝───╚╝─╚╝╚╝───╚╝─╚╝╚═══╝     ╚╝───╚══╝╚════╝╚════╝╚╝─╚╝╚╝╚═╝╚══╝╚╝─╚╝")
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
    question = input("What do you want? ").lower()
    if ("i want food" in question) or ("i want to order food" in question):
        print("I thought you would like food :)")
        print("")
        break
    time.sleep(1)
else:
     print(f"I dont understand this - {question} - you ask of me")
     print("")

     ### Ask for name ###

while nameconfirm != "yes":
    name = input("What is your name? ").lower().strip()
    if ("my name is" not in name):
     print("plz start again")
    else:
      searchText = "my name is"
      i = name.lower().find(searchText)
      x = i+len(searchText)
      name = name[x:].strip().title()
      nameconfirm = input(f"Your name is {name}, yes? ").lower()
      if ("yes" in nameconfirm) or ("ok" in nameconfirm):
        print("")
        break
      else:
        print("Oops... didnt match up please try again");

print("")

## put lines into a list called "Lines"##
with open('orderlist.txt') as f:
    lines = r.readlines()
for i in range(len(lines)):
    if"\n" in lines[i]:
        lines[i] = lines[i].replace("\n", "")

##-##
namefound = 0
for i in lines:
    entry = i.split()
    if name.lower() in i:
        prevorders = entry[1:]
        print(f"Welcome back {name}! Great to see you again.")
        if (len(prevorders) == 0):
            print("Yet you haven't ordered anything from us.")
        elif (len(prevorders) > 0):
            print("Last time you were with us, your order was: ")
            lastorder = " ".join(entry[1:])
            tempvalue = lastorder
            lastorder = lastorder.split("&%&")
            firstinlist = 1;
            for u in lastorder:
                if (firstinlist == 1):
                    print(" " + u)
                    firstinlist = 0;
                else:
                    print(u)
        namefound = 1

ordersame = 0
if namefound == 1:
    cont = 0;
    while cont == 0:
        print("")
        print("Would you like to order your last order again?")
        orderrepeat = input("---> ")
        if ("yes" in orderrepeat) or (orderrepeat == "y") or ("correct" in orderrepeat) or ("true" in orderrepeat) or ("yea" in orderrepeat):
            ordersame = 1;
            print("OK! Re-ordering your last order.")
            cont = 1;
        elif ("no" in orderrepeat) or (orderrepeat == "n") or ("incorrect" in orderrepeat) or ("false" in orderrepeat) or ("nah" in orderrepeat):
            print("Alright. Let's continue.")
            print("")
            cont = 1;
        else:
            print("I don't know what that means.")
            print("Please choose Y/N")



if namefound == 0:
    lines.append(name.lower())

######################################


     ### Ask to see Menu or Order ###
menu = 'no'
while menu !=  ("i would like to order" in menu):
    menu = input("Would you like to Order or see the Menu? ").lower().strip()
    if ("i would like" in menu) or ("i want to" in menu):
     if ("order" in menu):
        print("Lets order shall we")
        break
    elif     ("menu" in menu):
     printMenu()
        ### order

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
                    ordercheckdrink = "yes";
                    print(f"--> Thank you for ordering {order}, that will cost {cost}, and your total is now {totalcost}")
                    orderfood = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("--> Sorry let me try again")
                    print("")
                    ordercheckdrink ="no";
                else:
                    print(f"--> I'll uhhh... I'll take that as a no then")

                              ####Order Drinks####

                while ordercheckdrink == "yes":
                     order = input("And what drink would you like with that meal? Remember one at a time! ").lower().strip()
                     if order == "":
                      print("I'm sorry i didn't quite hear what you said. Could you repeat that?")
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
                       confirm = input(f"You ordered {order}. Is this correct? ").lower().strip()
                       if ("yes" in confirm):
                           cost = Drinks[order]
                           totalcost += cost
                           print(f"Thank you for ordering {order}, that will cost {cost}, and your total is now {totalcost} ")
                           orderdrink = order.replace(" ", "@");
                           meal = (f"{orderfood}+{orderdrink} ")
                           totalorder = (totalorder + meal);
                           ordersmade = int(ordersmade) + 1;
                           ordercheck = input("Would you like to order another meal? ").lower().strip()
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
                      print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                      menucheck = input(f"Would you like to see the menu? ")
                     if ("yes" in menucheck):
                        printMenu();
                     else:
                        print("Let's try again");
            elif ordercheck != "no":
                    print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                    print("")
                    menucheck = input(f"Would you like to see the menu? ")
                    if ("yes" in menucheck):
                       printMenu();
                    else:
                     print("")
        elif ordercheck != "no":
                print("I'm sorry but that is not in the Menu. Try saying 'i want' before what you want.")
                print("")
                menucheck = input("Would you like to see the menu? ")
                if ("yes" in menucheck):
                    printMenu();
                else:
                    print("");

else:
   if ordercheck == "yes":
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

## receipt
print("")
import random
number = random.randint(5,60)
print("====================================")
print("               Receipt              ")
print("====================================")
print("Store Manager: Papa Giusepe")
print("Served By: Papa's Chat Bot")
print(f"Order name: {name}")
print(f"Weight time: {number} minutes")
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

for i in range(len(lines)):
    if name.lower() in lines[i]:
        lines[i] = name.lower()  + " " + order

opened = open('orderlist.txt', 'w')
for e in lines:
    opened.write(e + "\n")
opened.close()

print("")
print("")
print("your NAME and ORDER has been saved for future reference!!")


