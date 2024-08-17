"""
create program, take 2 user inputs num1, num2 and give them
max
pow num1 to num2
sub,mul,sum,div
format your output to f{""}
"""

number1 = int(input("Enter number1= : "))
number2 = int(input("Enter number2= : "))

# print4

# print(number2)

print("Max of ", number1, " and ", number2, " is : ", max(number1,number2))

print("Value of ", number1, " to the power of ", number2, " is : ", pow(number1,number2))

print("Sum of", number1, "and", number2, "is : ", number1+number2)
print("Sub of", number1, "and", number2, "is : ", number1-number2)
print("Mul of", number1, "and", number2, "is : ", number1*number2)
print("Div of", number1, "and", number2, "is : ", number1/number2)

print("Formated_number1 is : ", f"{number1 : .4f}")
print("Formated_number2 is : ", f"{number2 : .5f}")