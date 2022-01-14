# broj1=int(input())
# broj2=int(input())
# operacija=input()

# b1=[]
# b2=[]
# n1=0
# n2=0

# while broj1!=0:
#     x=broj1%10
#     b1.insert(n1,x)
#     n1=n1+1
#     broj1=broj1//10
# b1.reverse()
# print(b1)

# while broj2!=0:
#     x=broj2%10
#     b2.insert(n2,x)
#     n2=n2+1
#     broj2=broj2//10
# b2.reverse()
# print(b2)

# rezultat=[]
# duzina=0
# if(operacija=='+'):
#     for i in range(n1-n2,n1):
#         for j in range(duzina,n2,n2):
#             rezultat.insert(duzina,b1[i]+b2[j])
#             if(rezultat[duzina]>9):
#                 rezultat[duzina]=rezultat[duzina]%10
#                 rezultat[duzina+1]=rezultat[duzina]//10
#         duzina=duzina+1
# print(rezultat)

# string1=''
# string2=''
# for i in range(n1):
#     string1=string1+str(b1[i])
# print(string1)
# for i in range(duzina):
#     string2=string2+str(rezultat[i])
# print(string2)

# pomstr=string1[0:n1-n2]
# print(pomstr)
# novstr=pomstr+string2
# print(novstr)

