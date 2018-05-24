qconfirm = "no";
q1confirm = "no";
cmenu = "no";
question2 = "no";
import json
import time
### Menu ###
menu = {
"Drinks": {
    " Coke" : 4.50,
    " Diet Coke" : 4.50,
    " Sprite" : 4.50,
    " Sparking Mineral Water" : 9.00,
    " Asahi" : 12.75,
           },
"Entres": {
    " Garlic Bread" : 10.00,
    " Garlic Pizza" : 12.50,
    " Garden Salad" : 12.00,
    " Ceasar Salad" : 14.50,
           },
"Mains": {
    " Margherita" : 14.00,
    " Napoletana" : 16.50,
    " Supreme" : 21.00,
    " Meat lovers" : 19.75,
    " Hawaiian" : 16.50,
          },
"Deserts": {
    " Tiramusu " : 9.00,
    " Mango Gelato" : 4.50,
    " Lemon Gelato" : 4.30,
    " Vanilla Gelato" : 4.45,
    " Mix Gelato" : 12.50,
    }
}

def printMenu():
        print("")
        print("=============== MENU ===============")

        for course in menu:
            choices = menu[course]
            print(f"{course}")
            print("")
            for dish in choices:
                price = choices[dish]
                print(f"> {dish} - ${price}")
        print("====================================")
        print("")
        print("====================================")
        print("")


while question2 !=  ("i would like to order" in question2):
    question2 = input("Would you like to Order or see the Menu? ").lower()
    if ("order" in question2):
        print("Lets order shall we")
        break
    elif     ("menu" in question2):
        printMenu()

order = input("What would you like to order?")