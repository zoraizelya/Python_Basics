#Function definition
#1st Way
def abc():
    print("salam Pakistan")

abc()#printing

#2nd way

def xyz():
    text="salam Pakistan"
    print(text)
    print(text)
    print(text)
xyz()

#3rd way
def xyz(text):
    print(text)
    print(text)
    print(text)
xyz("salam Pakistan")

# An example of a school

def school_calculator():
    age=input("Age of Kid is?")
    age=int(age)
    if age==5:
        print("Can Join School")
    elif age > 5:
        print("Should Join Higher class")
    else:
        print("Too Young to join")
school_calculator()

#definition a function of future predicted age
def future_age():
    age=input("Whats your  age? ")
    age=int(age)
    new_age=age+24 #we want to know after 24 years
    return new_age
    print(new_age)
predicted_age=future_age()
print("YOUR FUTURE PREDICTED AGE IS : ",predicted_age)