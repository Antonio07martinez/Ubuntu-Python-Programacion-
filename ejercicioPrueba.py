#This is my first programming in pyhton
#For example I want to create a programming with my Personal data

def Edad(age,name):
    total = age - 18
    if total < 0:
        print(f"Sorry {name}, but you aren't an adult")
    else: 
        print(f"Congratulations {name}, you are an adult")


Edad(name = input("Tell me your name, plese: \n"),
age = int(input("How old are you? ")))



    