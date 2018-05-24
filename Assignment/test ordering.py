import json
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
"Pizza" : 15.00,
"cum" :0.00,}
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
        print("Entre")
        for course in Entre:
            price = Entre[course]
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
        print("")
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



import time

### Ordering

totalcost = 0
Checkorder = "yes";
totalorder = "";
ordersmade = 0
time.sleep(0.05)
while Checkorder == "yes":
        order = input("What would you like for Mains friend? (Please be kind and enter 1 item in at a time)").lower().strip()
        if order == (""):
            time.sleep(.5)
        if ("i want " in order):
          order = order.split("i want " , 1) [1];
          order = order.capitalize();
        if ("i would like " in order):
          order = order.split("i would like " , 1) [1];
          order = order.capitalize();
        if ("get me " in order):
          order = order.split("get me " , 1) [1];
          order = order.capitalize();
        if ("give me " in order):
          order = order.split("give " , 1) [1];
          order = order.capitalize();
        if order in Mains:
                confirm = input(f"You have ordered {order}. Is this correct? ").lower().strip()
                if ("yes" in confirm):
                    cost = Mains[order]
                    totalcost += cost
                    Checkorderdrinks = "yes";
                    print(f"Thank's for ordering {order}, that will cost you ${cost}, and your total comes to ${totalcost}")
                    orderdrinks = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("Ooops... let's try again")
                    print("")
                    Checkorderdrinks ="no";
                else:
                    print(f"I guess that is a NO then")



while Checkorderdrinks == "yes":
         print("if you want no drinks with your order plz enter 'No Drinks'!")
         order = input("What would you like for Mains friend? (Please be kind and enter 1 item in at a time)").lower().strip()
         if order == "":
          print("Ooops... it seems i have miss heard you could you please repeat that?")
          print("")
         if ("i want " in order):
          order = order.split("i want " , 1) [1];
          order = order.capitalize();
         if ("i would like " in order):
          order = order.split("i would like " , 1) [1];
          order = order.capitalize();
         if ("get me " in order):
          order = order.split("get me " , 1) [1];
          order = order.capitalize();
         if ("give me " in order):
          order = order.split("give " , 1) [1];
          order = order.capitalize();
         if order in Entre:
                  confirm = input(f"--> You for ordered {order} is this correct?").lower().strip()
                  if ("yes" in confirm):
                        cost = Entre[order]
                        totalcost += cost
                        ordercheckdrink = "yes";
                        print(f"--> Thank you for ordering {order}, that will cost {cost}, and your total cost is {totalcost}")
                        print("")
                  elif ("no" in confirm):
                    print("Sorry let me try again")
                    print("")
                    ordercheckdrink = "no";
                  else:
                    print(f"I'm going to interpret that as a No then")
         if ("no " in order):
