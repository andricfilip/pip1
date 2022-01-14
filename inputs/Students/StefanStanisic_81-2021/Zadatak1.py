def Sabiranje(s1,s2):
    n1=len(s1)
    n2=len(s2)
    s1=list(s1)
    s2=list(s2)
    
    s=""
    for i in range(n1-1,-1,-1):
        s[i]=s1[i]+s2[i]
        
            
        
        
    return s
    
s1=input()
s2=input()
s3=input()
n1=len(s1)
n2=len(s2)
if s3=="+":
    print(Sabiranje(s1,s2))
elif s3=="-":
    print(Oduzimanje(s1,s2))
elif s3=="*":
    print(Mnozenje(s1,s2))
else:
    print("nije uneta odgovarajuca operacija")
    


    
        
        
