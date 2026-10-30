
notes=[200,10,100,500,20,10,2,1]
notes.sort()
notes.reverse()
# print(notes)

amount=25266
count=0

for i in notes :
    count=amount//i
    if  count > 0:
        print(i,"=",count)
        amount=amount % i
