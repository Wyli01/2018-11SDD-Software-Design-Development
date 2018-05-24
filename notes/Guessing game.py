print("welcome to the Game");
print('');
name = input('What is your name?' + ' ');
print('');
import random

print('welcome', name, 'to the game');
print('')
print('Here are the rules.');
print('')
print('1. Guess a number between 1-100.');
print('2. Get it right and you win!');
print('3. Get it wrong i will give you a hint (Higher/Lower).');
print('4. If you are within 6 digits of the number you will get (You are very close)');
print('5. You have got 10 attempts to win Good Luck,', name + '!');
print('')

   
guesses = 10
number = random.randint(0, 100)
correct = False
guesses -= 1
while guesses > 0 and not correct:
    guess = input("Guess what number:")
    if guess.isdigit():
        guess = int(guess)
        print("You guessed {}".format(guess))
    if guess == number:
            print(" well done {}, you guessed the number after {} attempts".format(name, attempts))
            correct = True
    

     

    if guess == number:
        win = True
        guesses = 0
    elif abs(guess - number) < 6: 
        print("You are very close")
        print('')
    elif guess > number:
        print("Your guess is too high", guesses, "remaining")
        print('')
    elif guess < number:
        print("Your guess is too low", guesses, "remaining")
        print('')

    if correct == False:
        print("Sorry, you didn't guess the number", number)
    else:
        print("Congrats, you guessed correct")
    exit()
    
