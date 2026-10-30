name = input("Enter your name: ")

hindi = int(input("Enter Hindi marks: "))
english = int(input("Enter English marks: "))
python = int(input("Enter Python marks: "))
total = hindi + english + python
percentage = total / 3

print("Total:", total)
print("Percentage:", percentage)
marks = [hindi, english, python]

print("Highest Marks:", max(marks))
if hindi >= 33 and english >= 33 and python >= 33:
    print("Pass")
else:
    print("Fail")
