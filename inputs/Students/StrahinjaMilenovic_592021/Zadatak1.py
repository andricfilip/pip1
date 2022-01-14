def mnozi(br1str, br2str):
    br1 = int(br1str)
    br2 = int(br2str)
    return str(br1*br2)

def oduzmi(br1str, br2str):
    br1 = int(br1str)
    br2 = int(br2str)
    return str(br1-br2)

def saberi(br1str, br2str):
    br1 = int(br1str)
    br2 = int(br2str)
    return str(br1+br2)
    

    
br1str = input()
br2str = input()
opstr = input()


rezultat = ""
if(opstr == "+"):
    rezultat = saberi(br1str,br2str)
if(opstr == "-"):
    rezultat = oduzmi(br1str,br2str)
if(opstr == "*"):
    rezultat = mnozi(br1str,br2str)

print(rezultat)


