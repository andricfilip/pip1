n = int(input("uneti n: "))
a = [[0 for i in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        x = int(input("unesi clan: "))
        a[i][j] = x

for i in range(n):
    for j in range(n):
        print("{0} ".format(a[i][j]))
    print("\n")