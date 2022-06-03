#Program 3 -- Loops and If Conditions
#Matthew Brown, Student ID 3534279, Program 3 -- Loops and If Conditions

print("Program author: Matthew Brown")
print("Student ID#: 3534279")
print("Program 3 -- LOOPS AND IF CONDITIONS")
print(" ")

#First the loop is set to 1, as long as the loop is set to 1 the program will continue
#to ask for a password unless the correct password of "hello" is entered.
#If the correct password is entered the loop is set to 0 so the program stops
#asking for a password and instead asks the user to input their name.
#If they input Cher or Madonna the program will ask them for an autograph,
#if they enter "Matthew" the program will respond with "That's a great name!"
#If they enter any other name, the program will return the name entered and respond
#with "that's a nice name."
#The program finally asks if the user would like to repeat the program.
#If "Y" is entered the loop is set to 2 and the program returns to asking for
#a name.  If anything else is entered the program prints the goodbye message and halts.

loop = 1
while loop == 1:
    password = input("Password? " )
    if password == "hello":
        loop = 2
        while loop == 2:
            name = input("What is your name? " )
            if name == "Cher":
                print("May I have your autograph, please?")
                print(" ")
                repeat = input("Would you like to go again? Y/N: ")
                if repeat == "y" or repeat == "Y":
                    loop = 2
                else:
                    print("Thank you for using Program 3 -- LOOPS AND IF CONDITIONS. Goodbye!")
                    loop = 0
            elif name == "Madonna":
                print("May I have your autograph, please?")
                print(" ")
                repeat = input("Would you like to go again? Y/N: ")
                if repeat == "y" or repeat == "Y":
                    loop = 2
                else:
                    print("Thank you for using Program 3 -- LOOPS AND IF CONDITIONS. Goodbye!")
                    loop = 0
            elif name == "Matthew":
                print("That's a great name!")
                print(" ")
                repeat = input("Would you like to go again? Y/N: ")
                if repeat == "y" or repeat == "Y":
                    loop = 2
                else:
                    print("Thank you for using Program 3 -- LOOPS AND IF CONDITIONS. Goodbye!")
                    loop = 0
            else:
                print(name + ",", "that's a nice name.")
                print(" ")
                repeat = input("Would you like to go again? Y/N: ")
                if repeat == "y" or repeat == "Y":
                    loop = 2
                else:
                    print("Thank you for using Program 3 -- LOOPS AND IF CONDITIONS. Goodbye!")
                    loop = 0
    else:
        print("I'm sorry, that is not the correct password.")
