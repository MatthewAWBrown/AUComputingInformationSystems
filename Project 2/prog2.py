#Program 2 -- Using Input
#Matthew Brown, Student ID 3534279, Program 2 -- Using Input

#The following prints the identification information
#Program author name:
print("Program author: Matthew Brown")
#Student number:
print("Student ID#: 3534279")
#And program name:
print("Program 2 -- USING INPUT")
#followed by a line break
print(" ")

#The loop is set to 1 so that the program can repeat.
loop = 1
#The loop conditions are then set.
while loop == 1:
    #The program will ask for the user to input the first word
    word1 = input("Please enter a word or name: ")
    #Then it will ask for a second word
    word2 = input("Please enter another word or name: ")
    #The program will then request a number
    a = int(input("Please enter a number: "))
    #and finally ask for another number
    b = int(input("Please enter another number: "))
    #line break
    print(" ")


    #The program then prints what was entered
    #The first word
    print("The first word you entered was", word1)
    #then the second word
    print("The second word you entered was", word2)
    #followed by the first number
    print("The first number you entered was", a)
    #then the second number
    print("The second number you entered was", b)
    #line break
    print(" ")

    #The program will now combine the input
    print("Together, your two words are", word1, word2)
    #Then it will give the product of the two numbers
    print("The product of the two numbers you entered is", a*b)
    #line break
    print(" ")
    #The program then asks if you would like to repeat it
    repeat = input("Would you like to go again? Y/N: ")
    #Conditions of the repeat, if "y" or "Y" is entered then the program will repeat.
    if repeat == "y" or repeat == "Y":
        loop = 1
    else:
        #If something other than "y" or "Y" is entered the program prints the goodbye message and sets the loop to 0.
        print("Thank you for using Program 2 -- USING INPUT, goodbye!")
        loop = 0


