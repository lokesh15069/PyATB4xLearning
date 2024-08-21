# Program grade calculator of the student in a class
# A-90-100
# B-80-89
# C-70-79
# D-60-69
# F-0-59

score = int(input("enter the score\n"))
if 100 >= score >= 90:  # simplified chaining format this also can use ---> 90<=score<=100
    grade = "A"
    print("your grade is", grade)
elif 89 >= score >= 80:
    grade = "B"
    print("your grade is", grade)
elif 79 >= score >= 70:
    grade = "C"
    print("your grade is", grade)
elif 69 >= score >= 60:
    grade = "D"
    print("your grade is", grade)
else:
    if 59 >= score >= 0:
        grade = "F"
        print("your grade is", grade)
