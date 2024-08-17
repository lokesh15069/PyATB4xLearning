"""
create program, take 2 user inputs num1, num2 and give them
max
pow num1 to num2
sub,mul,sum,div
format your output to f{""}
"""
num1 = int(input("enter the num1 :"))
num2 = int(input("enter the num2 :"))
print("The max of num1 and num2 :", max(num1, num2))
print("The power of num1 and num2 :", pow(num1, num2))
print("The sum of num1 and num2 :", (num1+num2))
print("The sub of num1 and num2 :", (num1-num2))
print("The div of num1 and num2 :", (num1/num2))
print("The mul of num1 and num2 :", (num1*num2))
print("formated num1 :",f"{num1:.3f}")
print("formated num2 :",f"{num2:.8f}")
