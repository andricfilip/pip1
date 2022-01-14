def sabiranje(br1,br2):
    br1 = int(br1)
    br2 = int(br2)
    resenje = br1+br2
    print(resenje)
def mnozenje(br1,br2):
    br1 = int(br1)
    br2 = int(br2)
    resenje = br1*br2
    print(resenje)
def oduzimanje(br1,br2):
    br1 = int(br1)
    br2 = int(br2)
    if(br1>br2):
        resenje = br1 - br2
        print(resenje)
    else:
        resenje = br2 - br1
        print(resenje)
    



prvibr = str(input())
drugibr = str(input())
operacija = str(input())

i = 0

if(operacija == '*'):
    mnozenje(prvibr,drugibr)
elif(operacija == '+'):
    sabiranje(prvibr,drugibr)
elif(operacija == '-'):
    oduzimanje(prvibr,drugibr)
else:
    print("Unite operacije +,- ili *")
    
    
    
