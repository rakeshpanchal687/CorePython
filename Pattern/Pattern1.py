# Rows: 5
for i in range(1, 6):
    for j in range(i, 6):
        # Pehli row, pehla column ya aakhri column print hoga
        if i == 1 or j == i or j == 5:
            print(j, end="  ")
        else:
            print(" ", end=" ")
    print()