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
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    nationality = input("Enter your nationality: ")
    print(f"I'm {name}, a {gender}, and i'm alreadty {age}. I'am born {nationality}")

def activity3():
    print()
    Name = input("PLEASE INPUT YOUR NAME : ")                      
    Nickname = input("PLEASE INPUT YOUR NICKNAME : ")
    Age = input("PLEASE INPUT YOUR AGE : ")
    Birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    Birthday = input("PLEASE INPUT YOUR BIRTHDAY : ")
    Birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    Gender = input("PLEASE INPUT YOUR GENDER : ")
    Address = input("PLEASE INPUT YOUR ADDRESS : ")
    Nationality = input("PLEASE INPUT YOUR NATIONALITY : ")
    isMarried = False
    CivilStatus = input("PLEASE INPUT YOUR CIVILSTATUS : ")
    Religion = input("PLEASE INPUT YOUR RELIGION : ")
    Citizenship = input("PLEASE INPUT YOUR CITIZENSHIP : ")
    Height = input("PLEASE INPUT YOUR HEIGHT : ")
    Weight =  input("PLEASE INPUT YOUR WEIGHT : ")
    NameofFather = input("PLEASE INPUT YOUR NAMEOFFATHER : ")
    OccupationofFather = input("PLEASE INPUT YOUR OCCUPATIONOFFATHER : ")
    ContactNumberofFather = input("PLEASE INPUT YOUR CONTACTNUMBEROFFATHER : ")
    NameofMother = input("PLEASE INPUT YOUR NAMEOFMOTHER : ")
    OccupationofMother = input("PLEASE INPUT YOUR OCCUPATIONOFMOTHER : ")
    ContactNumberofMother = input("PLEASE INPUT YOUR CONTACTNUMBEROFMOTHER : ")
    Elementary = input("PLEASE INPUT YOUR ELEMENTARY : ")
    YearAttendedElementary = input("PLEASE INPUT YOUR YEARATTENDEDELEMENTARY : ")
    YearEndedElementary = input("PLEASE INPUT YOUR YEARENDEDELEMENTARY : ")
    HighSchool = input("PLEASE INPUT YOUR HIGHSCHOOL : ")
    YearAttendedHighSchool = input("PLEASE INPUT YOUR YEARATTENDEDHIGHSCHOOL : ")
    YearEndedHighSchool = input("PLEASE INPUT YOUR YEARENDEDHIGHSCHOOL : ")
    College = input("PLEASE INPUT YOUR COLLEGE : ")
    Course = input("PLEASE INPUT YOUR COURSE : ")
    Skills = input("PLEASE INPUT YOUR SKILLS : ")
    print()

  print(f"Hello! My name is {Name}, but people also call me {Nickname}. I am {Age} years old. I was born on {Birthmonth} {Birthday}, {Birthyear}. I live at {Address}. I am {Gender} and my religion is {Religion}. My nationality is {Nationality}, and I have {Citizenship} citizenship. It is {isMarried} that I am married, and my civil status is {CivilStatus}. I am {Height} cm tall and weigh {Weight} kg. My father’s name is {NameofFather}. He works as a {OccupationofFather} and can be contacted at {ContactNumberofFather}. My mother’s name is {NameofMother}. She works as a {OccupationofMother} and can be reached at {ContactNumberofMother}. I completed my elementary education at {Elementary} from {YearAttendedElementary} to {YearEndedElementary}. Then, I went to {HighSchool} for high school from {YearAttendedHighSchool} to {YearEndedHighSchool}. I attended {College} for college, studying {Course}. I have skills in {Skills}, which help me handle challenges, grow professionally, and achieve goals more effectively.")

def activity4():
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter a number: "))
    ans = num1 + num2

    print("The sum of", num1, "and", num2, "is", ans)

def activity5():
    pass

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
    pass
def activity13():
    pass
def activity14():
    pass
def activity15():
    pass
def activity16():
    pass
def activity17():
    pass
def activity18():
    pass
def activity19():
    pass
def activity20():
    pass
def activity21():
    pass
def activity22():
    pass
def activity23():
    pass
def activity24():
    pass
def activity25():
    pass



def main():
    while True:
        x = input("enter a command: ")
        if x == "exit":
            print("programm executed")
            break
        else:
            if x == "cat1":
                sample()
            elif x == "cat2":
                activity1()
            elif x == "cat3": 
                activity2()
main()