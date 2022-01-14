n = int(input("Unesite N: "))

matrix = [[0 for i in range (n)] for i in range (n)]

for i in range(n):
    for j in range (n):
        x=int(input(""))
        if(x == 0 or x==1):
            matrix[i][j] = x
        else:
            print("Unos nije ispravan! ")


for i in range(n):
    for j in range(n):
       

print(matrix)
                    
