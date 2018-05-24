#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      WYLI01
#
# Created:     07/03/2018
# Copyright:   (c) WYLI01 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

while True: ##Infinite loop
    question = input("what would you like? ").lower()
    if ("i want" in question):
        break
    else:
     print('well thats a bit rude!')
     print(f"so you asked me - {question}!")