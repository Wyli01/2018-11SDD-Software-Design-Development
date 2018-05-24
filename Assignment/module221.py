
while ordercheck == "yes":
        order = input("What would you like for Mains friend? (Please be kind and enter 1 item in at a time) ").lower().strip()
        if order == (""):
         print("Ooops... it seems i have miss heard you could you please repeat that?")
         print("")
         if ("i want " in order):
            order = order.split("i want ", 1) [1];
            order = order.capitalize();
         if ("i would like " in order):
          order = order.split("i would like ", 1) [1];
          order = order.capitalize();
         if ("give me " in order):
                      order = order.split("give " , 1) [1];
                      order = order.capitalize();
         if order in Mains:
                confirm = input(f"You have ordered {order}. Is this correct? ").lower().strip()
                if ("yes" in confirm):
                    cost = Mains[order]
                    totalcost += cost
                    ordercheckdrink = "yes";
                    print(f"Thank's for ordering {order}, that will cost you ${cost}, and your total comes to ${totalcost}")
                    orderfood = order.replace(" ", "@")
                    print("")
                elif ("no" in confirm):
                    print("Ooops... let's try again")
                    print("")
                    ordercheckdrink ="no";
                else:
                    print(f"I guess that is a NO then")
