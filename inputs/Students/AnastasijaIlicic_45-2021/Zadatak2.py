A=[]
B=[]
C=[]
D = []
F = []
G =[]
H=[]
s = input()
n = int(input())
for i in range(n):
    A.insert(i,input())


for i in range(n):
    if(s.find(A[i])):
        B = B + [A[i]]
        D = D + [s.index(A[i])]
        C = C + [len(A[i])]




for i in range(n):
    F = F + [D[i]]
    F = F + [C[i]]


duzina = len(s)

for i in range(len(s)):
    G = G + [s[i]]

for i in range(0,len(F),2):
    for j in range(1,len(F),2):
        G.pop(F[i])
print(G)
