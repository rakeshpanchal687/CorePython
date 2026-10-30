from ctypes import pythonapi

name=input("enter your name :-")
print(name)
hindi=int(input(" hindi number:-"))
englis=int(input("english number:"))
python=int(input("python number:"))
total=hindi+englis+python
print(total)
percentage = total / 300 * 100
print("percentage",percentage)


