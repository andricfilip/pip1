x=input()
n=int(input())
A=['' for i in range(n)]
B=''
br=0
z=0
for i in range(n):
    y=input()
    A[i]=y
for j in range(len(x)):
    for i in range(n):
        br=0
        for k in range(len(A[i])):
            if(x[j]==A[i]):
                br=br+1;
        if(br==0):
            B=B+x[i]
            z=z+1
                
print(B)
