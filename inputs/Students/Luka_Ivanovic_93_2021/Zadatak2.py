string1=input("")
n=int(input())
a=[]
for i in range(n):
    string2=input("")
    a=a+[string2]
    while(string1.count(string2)!=0):
        string1=string1.replace(string2,"")
print(string1)

