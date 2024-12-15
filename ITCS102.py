def sample():
    x = {"pretty": "elieza","cute":"anne"}
    print()
    print(x["pretty"])
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

def code_challenge1():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def code_challenge2():
    name = input ("Please enter your name ----->")
    print ("Hi", name)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t\t    ","Hi", name,"\t\t\t*\t\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def code_challenge3():
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

def code_challenge4():
    number1 = eval(input("Enter a number --> "))
    number2 = eval(input("Enter a number --> "))
    answer1 = number1 + number2
    answer2 = number1 - number2
    answer3 = number1 * number2
    answer4 = number1/number2
    answer5 = number1 ** number2
    answer6 = number1 % number2
    answer7 = number1 // number2
    print("The sum of", number1, "and", number2, "is", answer1)
    print("The difference of", number1, "and", number2, "is", answer2)
    print("The product of", number1, "and", number2, "is", answer3)
    print("The quotient of", number1, "and", number2, "is", answer4) 
    print("The exponent by", number1, "and", number2, "is", answer5)
    print("The remainder of", number1, "and", number2, "is", answer6)
    print("The floor division of", number1,"and", number2, "is", answer7)

def code_challenge5():
    name = input("Please enter your name: ")
    deposit = eval(input("Please enter amount to deposit: "))
    one = deposit // 1000
    one1 = deposit % 1000
    two = one1 // 500
    two1  = one1 % 500
    three = two1 // 200
    three1 = two1 % 200
    four = three1 // 100
    four1 = three1 % 100
    five = four1 // 50
    five1 = four1 % 50
    six =  five1 // 20
    six1 = five1 % 20
    seven = six1 // 10
    seven1 = six1 % 10
    eight = seven1 // 5
    eight1 = seven1 % 5
    nine = eight1 // 1

    print("Hi", name,  "the breakdown of your deposit is: ")
    print(one, "-1000")
    print(two, "-500")
    print(three, "-200")
    print(four, "-100")
    print(five, "-50")
    print(six, "-20")
    print(seven, "-10")
    print(eight, "-5")
    print(nine, "-1")

def code_challenge6():
    Prelim = eval(input("Enter Prelim grade --> "))
    Midterm = eval(input("Enter Midterm grade --> "))
    Semifinal = eval(input("Enter Semifinal grade --> "))
    Final = eval(input("Enter Final grade --> "))
    Quiz = eval(input("Enter Quiz grade --> "))
    Project = eval(input("Enter Project grade --> "))

    if(Prelim >=65 and Prelim <=100) and (Midterm >=65 and Midterm <=100) and (Semifinal >=65 and Semifinal <=100) and (Final >=65 and Final <=100) and (Quiz >=65 and Quiz <=100) and (Project >=65 and Project <=100):
        FinalGrade = (Prelim * 0.15) + (Midterm * 0.15) + (Semifinal * 0.15) + (Final * 0.15) + (Quiz * 0.25) + (Project * 0.15)
    print(f"Your grade is : {round(FinalGrade, 2)}")
    if FinalGrade > 100 :
        print("Invalid Grade, Perhaps a mistake?")
    elif FinalGrade >= 75 : 
        print("Congratulations! You've passed the course")
    else:
        print("Sorry, You failed")

def code_challenge7():
    name = input("Enter your name :")
    purchased_or_not = input("Did you purchase a grocery today? (Yes or No) :")

    if purchased_or_not.lower() == "yes": 
        purchased = input("What did you purchase :")
    else:
        print(exit("You didn't purchase a grocery today"))
    
    orig_price = eval(input("Item Price :"))
    age = int(input("Age :"))
    taxed_price = (orig_price * 0.123) + orig_price
    discount = orig_price - (orig_price * 0.038) 
    discount_taxed_price = orig_price - (discount * 0.123)
    discount_senior = orig_price - (taxed_price * 0.123)
    two_discount = orig_price - (taxed_price * 0.161)

    if age >= 60 and age <= 150 and orig_price >= 4000 :
        print(f'Total : {round(two_discount,2)}')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - two_discount,2)}')
        
    elif orig_price >= 4000 :
    print(f'Total : {round(discount_taxed_price, 2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - discount_taxed_price, 2)} ')

    elif age >= 60 and age <= 150 :
    print(f'Total : {round(discount_senior,2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - discount_senior,2)} ')
        
    else : 
    print(f'Total : {round(taxed_price,2)} ')
    payment = eval(input("Payment :"))
    print(f'Change : {round(payment - taxed_price,2)} ')

def code_challenge8():
    print("Summation of 10 random numbers")
    x = 0
    for y in range (1,11):
        add = eval(input(f"Input (y) = "))
        x += add
    print(f"The Summation of the number is: {x} ")

def code_challenge9():
    z = eval(input("Enter a number: "))
    for x in range(z, 0,-1):
        for y in range(z,x,-1):
            print(" ", end=" ")
        print("* " * x)

def code_challenge10():
    for m in range(1,6):
        for i in range(6, m, -1):
            print(" ", end = " ")
        for n in range(1, m+1):
            print("*", end=" ")
        for g in range(1, m+1):
            print("*", end =" ")
        print()

    for m in range(1,6):
        for i in range(1, m + 1):
            print(" ", end = " ")
        for n in range(6, m ,-1):
            print("*", end=" ")
        for g in range(6, m, -1):
            print("*", end =" ")
        print()

def code_challenge11():
    for l in range(1,5):
        for o in range(5, l, -1):
            print(" ", end = " ")
        for v in range(0, l+0):
            print("*", end=" ")
        for e in range(1, l+0):
            print("*", end =" ")
    print()

for l in range(1,4):
        for o in range(1, l + 2):
            print(" ", end = " ")
        for v in range(4, l ,-1):
            print("*", end=" ")
        for e in range(3, l, -1):
            print("*", end =" ")
        print()

def code_challenge12():
    for l in range(1,5):
        for o in range(5, l, -1):
            print(" ", end = " ")
        for v in range(1, l+1):
            print("*", end=" ")
        for e in range(1, l+1):
            print("*", end =" ")
        print()

    for l in range(0,4):
        for o in range(4, 0, -1):
            print(" ", end = " ")
        for v in range(2,4):
            print("*", end=" ")
        for e in range(4, 0, -1):
            print(" ", end =" ")
        print()

def code_challenge13():
    for l in range(1,7):
        for o in range(6, l, -1):
            print(" ", end = " ")
        for o in range(l, 1, -1):
            print(o, end=" ")
        for v in range(1, l+1):
            print(v, end =" ")
        print()

    for l in range(5,0,-1):
        for o in range(6, l, -1):
            print(" ", end = " ")
        for o in range(l,1,-1):
            print(o, end=" ")
        for v in range(1,l+1):
            print(v, end =" ")
        print()

def code_challenge14():
    tuloy = True
    total = 0
    while tuloy == True:
        num = eval(input("Enter a number: "))

        if num ==0:
            print("Okay tama na")
            print(f"The total of your inputted numbers is {total}!")
            break

        else:
            total += num
            continue

def code_challenge15():
    import os
    tuloy = True
    num = 0
    while tuloy == True:
        tria = input("Would you like to add a triangle?(Y/N): ")
        if tria.lower() == "n":
            os.system('cls')
            print("PROGRAM TERMINATED. THANK YOU FOR USING ME")
            break
        elif tria.lower() == "y":
            os.system('cls')
            num += 1
            for x in range(1,6):
                for r in range(1, num+1):
                    for y in range(1,x+1):
                        print("*", end=" ")
                    for z in range (6,x,-1):
                        print("  ",end="")
                print()
            continue
        else:
            os.system('cls')
            print("INVALID ANSWER. PLEASE TRY AGAIN")
            continue

def code_challenge16():
    def denomination(amount):
        print("\nDenomination Breakdown:")
        
        # Breaking the amount into denominations
        thousands = amount // 1000
        remainder = amount % 1000

        five_hundreds = remainder // 500
        remainder = remainder % 500

        two_hundreds = remainder // 200
        remainder = remainder % 200

        hundreds = remainder // 100
        remainder = remainder % 100

        fifties = remainder // 50
        remainder = remainder % 50

        twenties = remainder // 20
        remainder = remainder % 20

        tens = remainder // 10
        remainder = remainder % 10

        fives = remainder // 5
        remainder = remainder % 5

        ones = remainder // 1

        # Printing the breakdown
        print("1000---", thousands)
        print("500----", five_hundreds)
        print("200----", two_hundreds)
        print("100----", hundreds)
        print("50-----", fifties)
        print("20-----", twenties)
        print("10-----", tens)
        print("5------", fives)
        print("1------", ones)

    accounts = {}

    def create_account():
        username = input("Enter a username: ")
        if username in accounts:
            print("Account already exists!")
        else:
            accounts[username] = 0
            print(f"Account created successfully for {username}.")

    def deposit():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    accounts[username] += amount
                    print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")

    def withdrawal():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amount <= accounts[username]:
                    accounts[username] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")

    def check_balance():
        username = input("Enter your username: ")
        if username in accounts:
            print(f"Your balance: {accounts[username]}")
        else:
            print("Account not found!")

    def options():
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid option. Please try again.")

    options()


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