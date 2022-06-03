#Program 1 -- Math Functions
#This program is adapted from the calculator demo of Lesson 4 of "A Beginner's Python Tutorial/Functions" https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Functions
#Matthew Brown, 3534279, Program 1 -- Math Functions

#The following line prints identification information; name, student ID number, and the name of the program.
#Program author name:
print("Program author: Matthew Brown")
#Student number:
print("Student ID#: 3534279")
#And program name:
print("Program 1 -- MATH FUNCTIONS")
#This adds a line break, making the output easier to read
print(" ")

#This prints an example of what the program is capable of
print("Please allow me to demonstrate my functionality:")
#Demonstrating addition
print("Addition: 2 + 2 =", 2+2)
#Demonstrating subtraction
print("Subtraction: 4 - 2 =", 4-2)
#Demonstrating multiplication
print("Multiplication: 4 * 2 =", 4*2)
#Demonstrating division
print("Division: 4 / 2 =", 4/2)
#Demonstrating exponents
print("Exponents: 2 ** 3 =", 2**3)
#Demonstrating remainders
print("Remainder: 5 % 2 =", 5%2)
#Another line break
print(" ")

#The following line defines the Math Functions to be used and prints the main menu prompting a choice
def menu():
    #print the options that the program is capable of, placing each option on a new line.
    print("Try one for yourself!")
    print("your options are:")
    print(" ")
    
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exponents")
    print("6) Remainder")
    print("7) Quit Program 1 -- MATH FUNCTIONS")
    #Line break
    print(" ")
    #The following prompts the user for an interger input corresponding with the menu options
    return int(input("Choose your option: "))

#The following defines all of the options available in the menu, it is not code to be run
#This adds two numbers given
def add(a,b):
    #This will print the equastion with the variables replaced by future input from the user
    print(a,"+",b,"=", a + b)
    #With a line break between the equasition and beginning of the new loop
    print(" ")

#This subtracts two numbers given
def sub(a,b):
    #This line prints the equastion.
    print(b,"-",a,"=", b - a)
    #Line break
    print(" ")

#This multiplies two numbers given
def mul(a,b):
    #again, we print the equastion that we want to display
    print(a,"*",b,"=", a * b)
    #Line break
    print(" ")

#This divides two numbers given
def div(a,b):
    #With the equasition that will be displayed
    print(a,"/",b,"=", a / b)
    #Line break
    print(" ")

#This finds the exponential total of two numbers
def exp(a,b):
    #Printing the equasition to be displayed
    print(a,"**",b,"=", a ** b)
    #Line break
    print(" ")

#This finds the remainder of two numbers that were divided
def rem(a,b,):
    #Printing the equasition
    print(a,"%",b,"=", a % b)
    #Line break
    print(" ")

#NOW THE CODE TO BE RUN BEGINS
#First we set the loop to 1
loop = 1
#Setting the choice to 0
choice = 0
#Setting the condition of the loop, while the loop is 1 the program will continue to repeat
while loop == 1:
    #the choice now changes depending on the input given in the main menu
    choice = menu()
    #The following defines the condiditions of the "if" "elif" loop depending on the new value of choice
    if choice == 1:
        #we now call back our previous definitions, first addition.  We also ask for the user to input an integer with int(input)
        add(int(input("Add this: ")),int(input("to this: ")))
    #Now the elif conditions are set out
    elif choice == 2:
        sub(int(input("Subtract this: ")),int(input("from this: ")))
    elif choice == 3:
        mul(int(input("Multiply this: ")),int(input("by this: ")))
    elif choice == 4:
        div(int(input("Divide this: ")),int(input("by this: ")))
    elif choice == 5:
        exp(int(input("The base: ")),int(input("to the power of: ")))
    elif choice == 6:
        rem(int(input("Find what remains of this: ")),int(input("Divided by this: ")))
    elif choice == 7:
        #This sets the loop to 0 which halts the program
        loop = 0

#Prints a goodbye message        
print("Thank you for using Program 1 -- MATH FUNCTIONS!")
