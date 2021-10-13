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
print(people.index("SB"))0