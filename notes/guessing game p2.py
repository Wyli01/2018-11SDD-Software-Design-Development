def game1 ():
    from random import randint
    print ('Hello player w, What is your name')
    myName = input()
    myName = str(myName)
    print ("hello " + myName + ", i am a number between 0 and 100")
    number = (randint (1,100))
    str(number)
    guessTaken = 1
    print ("take a guess")
    correctGuess = False
    while correctGuess != True:

        Guess = input()
    error = True
    while error == true:
        try:
            Guess = int(Guess)
        except ValueError:
            print("that is not an integer")
            print("Take another Guess")
            Guess = input()
        else:
            error = False
    Guess = int(Guess)
    if Guess < number:
        print ("The number you have guessed is to low")
        guessTaken = guessTaken + 1
        print ("Take another turn")

        
    if Guess > number:
        print ("The number you have guessed is to high")
        guessTaken = guessTaken + 1
        print ("Take another turn")

    if Guess == number:
        correctGuess = True
        guessTaken = str(guessTaken)
        print ("well done " + myName + ", You Guessed my number")
        

        
