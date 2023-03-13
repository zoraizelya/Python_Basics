# Equal to :                     ==
# less than :                    <
# Greater than :                 <
# Less than  & equal to :        <=
# Greater than  & equal to :     <=

# 3 is equal to 3?
print(3==3) #True
# 3 is not equal to 3?
print(3!=3) #False

#Less Greater
print(3<=4) #True
print(3>=4) #False

# A simple example
ahad_age=4
required_age_at_school=5
print(" Can ahad take admission at school? ")
print(ahad_age==required_age_at_school)

#Using input function
required_age_at_school=5
ahad_age=input("How old is ahad? ")# but this is string we need it integer so write ahad_age=int(ahad_age) first
ahad_age=int(ahad_age)
print(" Can ahad take admission at school? ")
print(ahad_age==required_age_at_school)
