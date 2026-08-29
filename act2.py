n = int(input("Enter the number of rows you need"))
for i in range(1,n+1):
    for j in range(i):
        print("*", end='')
    print()