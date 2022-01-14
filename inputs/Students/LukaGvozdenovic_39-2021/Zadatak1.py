def Sabiranje(br1,br2):
    resenje = br1+br2
    return resenje

def Oduzimanje(br1,br2):
    resenje = br1-br2
    return resenje

def Mnozenje(br1,br2):
    resenje = br1*br2
    return resenje


br1 = int(input())
br2 = int(input())
znak = int(input())

if(znak=="+"):
    resenje = Sabiranje(br1,br2)
if(znak=="-"):
    resenje = Oduzimanje(br1,br2)
if(znak=="*"):
    resenje = Mnozenje(br1,br2)

print(resenje)
