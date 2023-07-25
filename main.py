import random
#                                       Functions
# Function Greeting
def greeting():
    greet = "Hello, my name is Mac.  How may I help you?"
    return (greet)

#dice roll function for multiple uses including games.
def dice(sides):
    roll = random.randint(1, int(sides))
    return (roll)


#                                       Define Variables
userInput = ""
runMac = False

# Bootup Greeting add time check later for good morning or good evening etc
print (greeting())


#                                       Main Interface Loop
while runMac == False:
    userInput = input(">")
    userInput = userInput.lower()
    if "dice" in userInput or "roll" in userInput:
        sides = input("Roll a dice?  Sure.  Please enter the number of sides on the dice.  >")
        if sides.isdigit() == False:
            print ("That is not a number.")
        elif sides.isdigit() == True:
            roll = dice(int(sides))
            print ("I rolled a " + str(roll))
    if "exit" in userInput or "goodbye" in userInput or "quit" in userInput or "logout" in userInput:
        exit()



