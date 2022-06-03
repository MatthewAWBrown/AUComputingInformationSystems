#Program 4 -- Functions
#This program is adapted from the calculator demo of Lesson 4 of "A Beginner's Python Tutorial/Functions" https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Functions
#Matthew Brown, 3534279, Program 4 -- Functions

print("Program author: Matthew Brown")
print("Student ID#: 3534279")
print("Program 4 -- FUNCTIONS")
print(" ")

def menu():
    print("Welcome to Program 4 -- FUNCTIONS!")
    print(" ")

    print("Please choose one of the following options:")
    print("1) Area (Square)")
    print("2) Area (Rectangle)")
    print("3) Area (Circle)")
    print("4) Perimeter (Square)")
    print("5) Perimeter (Rectangle)")
    print("6) Perimeter (Circle)")
    print("7) Quit Program 4 -- Functions")
    print(" ")
    return int(input("Choose your option: "))

def arsq(a):
    print("Area:", a,"**2","=", a ** 2)
    print(" ")

def persq(a):
    print("Perimiter:", "4*",a,"=", a + a + a + a)
    print(" ")
    
def arr(a,b):
    print("Area:", a,"*",b,"=", a * b)
    print(" ")

def perr(a,b):
    print("Perimeter:", "2*",a,"+","2*",b,"=", (2 * a) + (2 * b))
    print(" ")

def arcl(a):
    print("Area:", "3.14*",a,"**2","=", 3.14 * a ** 2)
    print(" ")

def percl(a):
    print("Perimeter:", "2*3.14*",a,"=", 2 * 3.14 * a)
    print(" ")

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        print("You have chosen Area (Square)")
        arsq(int(input("Length: ")))
    elif choice == 2:
        print("You have chosen Area (Rectangle)")
        arr(int(input("Length: ")),int(input("Width: ")))
    elif choice == 3:
        print("You have chosen Area (Circle)")
        arcl(int(input("Radius: ")))
    elif choice == 4:
        print("You have chosen Perimeter (Square)")
        persq(int(input("Length: ")))        
    elif choice == 5:
        print("You have chosen Perimeter (Rectangle)")
        perr(int(input("Length: ")),int(input("Width: ")))
    elif choice == 6:
        print("You have chosen Perimeter (Circle)")
        percl(int(input("Radius: ")))
    elif choice == 7:
        loop = 0
print("Thank you for using Program 4 -- FUNCTIONS!")
        
