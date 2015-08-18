# Week 3 
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# helper function to start and restart the game
def remaining_attempts(low, high):
    return math.ceil(math.log(((high-low)+1),2))

def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses, low, high
    secret_number = random.randrange(low, high)
    remaining_guesses = remaining_attempts(low, high)
    # print '[' + str(secret_number) + ']'
    
# define event handlers for control panel
def range100():
    global low, high # Change the global values
    low, high = 0, 100
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range set to [0,100)"
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range set to [0,1000)"
    global secret_number, remaining_guesses, low, high
    low, high= 0, 1000 # change the global values
    secret_number = random.randrange(low,high)
    remaining_guesses = remaining_attempts(low,high)
    # print '[' + str(secret_number) + ']'
def input_guess(guess):
    global remaining_guesses
   
    # Decrement remaining number of guesses
    remaining_guesses-=1
    print 'Guess was: ' + guess # Leave in string form
    print 'Number of remaining guesses: ' + str(int(remaining_guesses)) 

    guess = int(guess) # Convert string to int
    if (guess > secret_number):
        print "Lower!"
    elif(guess < secret_number):
        print "higher!"
    elif (guess == secret_number):
        print "Correct!\n"
        new_game()
    
    if (remaining_guesses <= 0):
        print 'Game Over: The number was ' + str(secret_number) + '\n'
        new_game()
    
# create frame
f = simplegui.create_frame("Guess the number",200, 200)

# register event handlers for control elements and start frame
f.add_input("Enter a guess", input_guess, 200)
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
# call new_game - Initialze state 
global low, high
low, high = 0, 100

new_game()

