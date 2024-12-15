def sample():
    x = {"kupal": "elieza","pogi":"bajade"}
    print()
    print(x["kupal"])
    print()

def activity1():
    print()
    print("hello world!")
    print()

def activity2():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("Enter a number: "))
    answer = number1 + number2
    print(number1 , " plus " , number2 , " = " , answer)


def activity3():
    Name = input("PLEASE INPUT YOUR NAME : ")                          
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")
    Address = input("PLEASE INPUT YOUR ADDRESS : ")
    Age = input("PLEASE INPUT YOUR AGE : ")
    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")
    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    Gender = input("PLEASE INPUT YOUR GENDER : ")
    Height = input("PLEASE INPUT YOUR HEIGHT : ")
    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")
    Religion = input("PLEASE INPUT YOUR RELIGION : ")
    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")
    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")
    isMarried = False
    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")
    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")
    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")
    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")
    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")
    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")
    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")
    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")
    YearStartedElementary = input("PLEASE INPUT YOUR YEARSTARTEDELEMENTARY : ")
    YearCompletedElementary = input("PLEASE INPUT YOUR YEARCOMPLETEDELEMENTARY : ")
    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")
    YearStartedHighschool = input("PLEASE INPUT YOUR YEARSTARTEDHIGHSCHOOL : ")
    YearCompletedHighschool = input("PLEASE INPUT YOUR YEARCOMPLETEDHIGHSCHOOL : ")
    College = input("PLEASE INPUT YOUR COLLEGE : ")
    Course = input("PLEASE INPUT YOUR COURSE : ")
    Skills = input("PLEASE INPUT YOUR SKILLS : ")

    print("Hi, my name is " + Name + " and I am also known as " + Nickname + ".\nMy current address is " + Address + ".\nI am ",Age," years of old, born in " + Birthmonth + " on " + Birthday + ", " + Birthyear + ".\nI am a " + Gender + " and have a height of" ,Height,"in centimeters and a weight of",Weight,"in kilogram." + "\nMy religion is " + Religion + ", and my nationality is " + Nationality + " and I hold " + Citizenship + " citizenship." + "\nIt is",isMarried, "that I am married and my civil status is " + CivilStatus + "." + "\nMy father's name is " + NameofFather + "." + "\nHe works as a " + OccupationofFather + ". He can be reached at his contact number,",ContactNumberofFather,"\b." + "\nMy mother's name " + NameofMother + ", and she is employed as a " + OccupationofMother + "." + "\nHer contact number is",ContactNumberofMother,"\b." + "\nAs for my educational background, I completed my elementary education at " + Elementary + " from" ,YearStartedElementary,"to",YearCompletedElementary,"\b." + "\nI attended " + HighSchool + " for my high school education from",YearStartedHighschool,"to",YearCompletedHighschool,"\b." + "\nI pursued higher education at " + College + ", where I studied " + Course + "." + "\nI have developed skills in " + Skills + "." + " I am confident that my background, skills, and experiences align well with your expectations.")

def activity4():
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter a number: "))
    ans = num1 + num2

    print("The sum of", num1, "and", num2, "is", ans)

def activity5():
    print("Convert Fahrenheit to Celsius")
    fahrenheit = eval(input('\nEnter temperature in Fahrenheit: '))
    celsius_temp = (fahrenheit - 32) * 5 / 9
    print(f'\n\n{fahrenheit} degrees Fahrenheit is equal to {celsius_temp} degrees Celsius\n\nor')
    print(f'\n{fahrenheit} degrees Fahrenheit is approximately {round(celsius_temp, 2)} degrees Celsius')

def activity6():
    x=5
    print(x)
    x=x+10 
    print(x)
    x=x+15 
    print(x)
    x += 20 
    print(x)
    x=25 
    print(x)

def activity7():
    gold = 0

    miner = input("What's your name? ")

    mined_gold = input("Did you find any gold today? (yes or no): ")

    if mined_gold.lower() == "yes":
        gold += 1
        print(f"Hello {miner}, you have {gold} gold today.")
    else:
        print(f"Hello {miner}, you have {gold} gold today.")

def activity8():
    password = input("Type your password: ")

    if password.lower() == "loveu":
        print("You can go in!")
        print("Feel free to use the system.")
    elif password.lower() == "0407":
        print("Hello, Kim Mingyu!")
        print("You can go in!")
    else:
        print("Wrong password. You can't go in.")

    print("Goodbye!")

def activity9():
    years = eval(input("Please enter your age: "))

    if 1 <= years <= 7:
        print("You are a young child.")
    elif 8 <= years <= 13:
        print("You are a pre-teen.")
    elif 14 <= years <= 18:
        print("You are a teenager.")
    elif 19 <= years <= 31:
        print("You are a young adult.")
    elif 32 <= years <= 45:
        print("You are in middle adulthood.")
    elif 46 <= years <= 59:
        print("You are in late adulthood.")
    elif 60 <= years <= 150:
        print("You are a senior.")

def activity10():
    username = input("What's your name? ")
    student_status = input("Are you a DLL student? (yes/no): ")

    if student_status.lower() == "yes":
        print("Welcome to the DLL BSIT Scholarship Application!")

        is_resident = input("Do you live in Barangay Gulang-Gulang? (yes/no): ")
        
        if is_resident.lower() == "yes":
            print("Please proceed to the next form.")
        
            year_level = input("What year are you in?\nF - Freshman\nS - Sophomore\nJ - Junior\nR - Senior\nEnter your answer here: ")
            
            if year_level.lower() == "f":
                print(f"Hello {username}, Freshman! Welcome to DLL!")
            elif year_level.lower() == "s":
                print(f"Hello {username}, Sophomore! Welcome to DLL!")
            elif year_level.lower() == "j":
                print(f"Hello {username}, Junior! Welcome to DLL!")
            elif year_level.lower() == "r":
                print(f"Hello {username}, Senior! Welcome to DLL!")
            else:
                print("Sorry, that's not a valid option.")
            
            wants_scholarship = input("Do you want to apply for the scholarship? (yes/no): ")
            
            if wants_scholarship.lower() == "yes":
                print("Your scholarship application has been approved!")
            else:
                print("This scholarship is only available to Barangay Gulang-Gulang residents.")
            
            print("Your application form has been successfully submitted.")
        else:
            print("Sorry, this scholarship is only for residents of Barangay Gulang-Gulang.")
    else:
        print("You must be a DLL student to apply.")

def activity11():
    for mingoo in range(1,5):
        print("mingooya")
        name = input("Hi! Please input your name: ")
        print(f"Hi {name}")


def activity12():
    for m in range(1,10,3):
	    print(m)

def activity13():
    print("Calculate Factorial\n")

    number = int(input("Enter a number to find its factorial: "))
    result = 1
    for i in range(number, 0, -1):
        result *= i

    print(f"The factorial of {number} is {result}")

def activity14():
    for m in range (0,11):
	    for z in range(0,11):
		    print("*", end="")
	    print()
def activity15():
    for z in range(0, 11):  # Outer loop from 0 to 10
        print(z, end="")  # Print the number without a newline
        for y in range(0, z):  # Inner loop to print asterisks
            print("*", end="")  # Append an asterisk for each iteration
        print("")  # Move to the next line after printing all asterisks for the current number


def activity16():
    for x in range(1,6):
        for y in range(1, x + 1):
            print(" ", end = " ")
        for z in range(6, x, -1):
            print("^",end=" ")
        for k in range(6, x, -1):
            print("*",end=" ")
    print()

def activity17():
    columns = eval(input("Enter the number of columns: "))

    for r in range(1, 11):
        for co in range(1, columns + 1):
            print(f"{r} x {col} = {r * c}", end="\t")
        print()

def activity18():
    n = eval(input("Enter the number of triangles: "))
    for a in range(1, 5):
        for b in range(1, n + 1):
            for c in range(1, a + 1):
                print("*", end=" ")

            for d in range(5, a, -1):
                print(" ", end=" ")
        print()

def activity19():
    tuloy = True
    while tuloy == True:
        name = input("Please enter a name: ")

        if name.lower() == "stop":
            print("Program Terminated")
            break
            tuloy = False
        else:
            continue

def activity20():
    isContinue = True
    triangleCount = 0

    while isContinue:
        userInput = input("Do you want to add another triangle? (yes / no): ")

        if userInput.lower() == "no":
            print("PROGRAM ENDED")
            break
        else:
            triangleCount += 1
            for o in range(1, 5):
                for t in range(1, triangleCount + 1):
                    for s in range(1, o + 1):
                        print("*", end=" ")
                    for q in range(5, o, -1):
                        print(" ", end=" ")
                print()
def activity21():
    def say_hello():
        print("Hello Elieza")

    def say_hello_v2(name):
        print(f"Hello {name}")

    def activity2():
        number1 = eval(input("Enter a number: "))
        number2 = eval(input("Enter another number: "))
        total = number1 + number2
        print(number1, " plus ", number2, " = ", total)

    tuloy = True
    while tuloy:
        ask = input("Please provide a name: ")

        if ask.lower() != "stop":
            say_hello_v2(ask)
            if ask.lower() == "2":
                activity2()
            continue
        
        else:
            break

def activity22():
    print("\n----------------------------------------------------------------------\n")
    print("Activity 22\n")
    #Name listing and then count names

    loop = True
    names = []
    while loop == True:
        Name = input("What name would you like to add? ")
        if Name.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names! ")
            break
        else:
            names.append(Name)
    print("\n-----------------------------------------------------------------------\n")
    

def activity23():
    def factorial(number):
        fact = 1
        for a in range(number, 0, -1):
            fact *= 1
        return fact

def activity24():
    from Activity23 import factorial

    print(f"The Factorial of 4 is {factorial(4)}")

def activity25():
    # Python list
    fruit_list = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(fruit_list)

    #Indexing / Index - position or location of an item in a list
    #           0       1           2           3           4
    #fruit_list = ["apples", "banana", "oranges", "star apple", "grapes"]
    print(f"My favorite childhood fruit is {fruit_list[3]}")

    print(f"The last item on the list is {fruit_list[-1]}")

    #adding another item to the list
    fruit_list.append("longgan")
    print(fruit_list)
    fruit_list.append("strawberry")
    print(fruit_list)

    #inserting an item at a specific index
    fruit_list.insert(3, "strawberry")
    print(fruit_list)
    fruit_list.remove("longgan")
    print(fruit_list)

    while True:
        new_fruit = input("Do you want to add more fruits? ")

        if new_fruit.lower() == "no":
            print("You chose not to add more fruits.")
            break
        else:
            fruit_list.append(new_fruit)
            print("Fruit added to the list.")
            continue

def main():
    while True:
        x = input("enter a command: ")
        if x == "exit":
            print("programm executed")
            break
        else:
            if x == "sample":
                sample()
            elif x == "cat1":
                activity1()
            elif x == "cat2": 
                activity2()
            elif x == "cat3":
                activity3()
main()