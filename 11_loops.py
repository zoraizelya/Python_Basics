#Type of loops 
# 1. While loops
# 2. For loops

#while loop

x=0
while (x<5):
    print(x)
    x=x+1  # use to make loop go through the whole process means upto a specific condition

#for loop

for c in range(5,50):
    print(c)


#Array with for loop

days = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun"]
for d in days:
    # if (d=="Tue"):break #loop stops
    if (d=="Mon"): continue # it will skip the selected 
    print(d)

    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# will give you the price of fruits 
fruits=["mango","orange","apple"]
for i in fruits:
    if (i=="orange"):
        print("Rs. 50")
    elif (i=="mango"):
        print("Rs. 150")
    else:
        print("Rs. 80")
    print(i)
