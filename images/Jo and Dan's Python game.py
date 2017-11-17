#importing the time module
import time

#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play"

print "Are you ready?????????????????"

#wait for 1 second
time.sleep(1)

print "Guess now!!"
time.sleep(0.5)

#here we set the secret
word = "pee pee smell"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print "You win!"
    if failed == 0:        
        print "You win! You don't stink like pee pee smell!"  

    # exit the scriptChange working directory...
        break              

    print

    # ask the user guess a letter
    guess = raw_input("guess a letter:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # prints the message "incorrect"
        print "Incorrect"    
 
    # prints how many guesses you have left
        print "You have", + turns, 'guesses left' 
 
    # if the turns equal zero
        if turns == 0:           
    
        # prints the message "You Loose"
            print "You Loose. You stink like pee pee smell."