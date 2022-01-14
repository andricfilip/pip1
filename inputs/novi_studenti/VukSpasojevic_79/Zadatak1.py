def Sabiranje(n, n1):
    #if znak=='+':
    return n+n1
    
def Oduzimanje(n, n1):
    #if znak=='-':
    return n-n1

def Mnozenje(n, n1):
    #if znak=='*':
    return n*n1


n=input()
n1=input()
znak=input()

if(znak=='+'):
    print(Sabiranje(int(n),int(n1)))

if(znak=='-'):
    print(Oduzimanje(int(n),int(n1)))

if(znak=='*'):
    print(Mnozenje(int(n),int(n1)))



    
