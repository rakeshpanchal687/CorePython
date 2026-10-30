num = 1
for i in range(1, 5):  # 4 rows
    for j in range(i):
        print(num * num, end=" ")
        num += 1
    print()