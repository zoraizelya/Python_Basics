a=10.3
b=7
c="salam"

print(type(a))#int
print(type(b))#int
print(type(c))#str

#implicit type conversion
a=a*b
print(a,"Type of 'a' is : ", type(a)) #float

#explicit type conversion
age=input("How old are you? ")
#age=int(age)
print("Your Age is ",age," And Type is -> ",type(int(age)))
#name + age
name=input("What is your name? ")
print("My name is ",name," And I am ",age,type(str(name)))
