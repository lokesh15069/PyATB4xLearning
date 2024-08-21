# program to find maximun of 3 numbers

# logic building
# user inputs--num1,num2,num3>>>>int
# output---int or string with max number
# Logic---if else---->1 condition
# morethan 1 condition--->if elif else

# syntax
# if(condition1):
# print("do 1")
# elif (condition2):
# print("do 2")
# else
# print("do 3)


num1 = float(input("enter the num1\n"))
num2 = float(input("enter the num3\n"))
num3 = float(input("enter the num3\n"))
if num1 > num2 and num1 > num3:
    print("The greater number is", num1)
elif num2 > num3 and num2 > num1:
    print("The greater number is", num2)
else:
    print("The greater number is", num3)
#      OR
result = float(max(num1, num2, num3))
print(result)
