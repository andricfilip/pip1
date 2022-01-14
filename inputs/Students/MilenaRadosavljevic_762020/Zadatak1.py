def operacija(s):
    if(s[2]=='+'):
        return (int(s[0])+int(s[1]))
    elif(s[2]=='-'):
        return (int(s[0])-int(s[1]))
    elif(s[2]=='*'):
        return (int(s[0])*int(s[1]))
    else:
        return (int(s[0])//int(s[1]))

s1=input()
s2=input()
s3=input()

s=[]

s.insert(0, s1)
s.insert(1, s2)
s.insert(2, s3)
print(operacija(s))

