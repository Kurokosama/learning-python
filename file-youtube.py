"""
num1 = input("enter your number1:  ")
num2 = input("enter your number2： ")
result = float(num1) + float(num2)
print(result)
"""

numbers = [1,2,3,4,5]
people = ["Kevin", "Sam", "Karen", "Oman"]

people.extend(numbers)

people.append("SB")

people.insert(1, "USB")

people.remove("Sam")
print(people)
print(people.index("SB"))

#tuple

tup1 = ('Google', 'Bing', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#Functions

a_name = "Kuroko"
a_age = "25"

def sayhi(name, age):
    print("Hello " + name + " You are: " + age)


sayhi(a_name, a_age)

def cube(num):
    return num*num*num

print(cube(3))

print("*********************************")
#if statement
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):
    print("You are not tall")
elif not(is_male) and is_tall:
    print("You are tall not male")
else:
    print("You are not male and tall")

print("*********************************")

num1 = float(input("enter num1  "))
num2 = float(input("enter num2  "))
num3 = float(input("enter num3  "))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("The MAX is: " + str(max_num(num1, num2, num3)))