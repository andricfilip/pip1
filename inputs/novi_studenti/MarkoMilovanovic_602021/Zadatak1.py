


s1 = input()
s1 = "0"+s1
broj1 = []
for ch in s1:
    broj1.append(int(ch))
s2 = input()
s2 = "0"+s2
broj2 = []
for ch in s2:
    broj2.append(int(ch))

operacija = input()
lenght = len(broj2)
if len(broj1) < len(broj2):
    lenght = len(broj1)

    
if operacija == '+':
    for i in range(lenght):

        if int(broj1[-i]) >= 10:
            broj1[-(i+1)] = broj1[-(i+1)]+1
            broj1[-i] = broj1[-i] - 10
            
            
        rez = int(broj1[-i]) + int(broj2[-i])
        if rez >= 10:
            broj1[-(i+1)] = broj1[-(i+1)]+1
            rez -= 10
            broj1[-i] = rez
            
    rezultat = ""
    n = 0
    if broj1[0] == '0':
        n = 1
    for i in range(n,len(broj1)):
        rezultat += str(broj1[i])
    print(rez)
        

    
#if operacija == '-':
    #
#if operacija == '*':
    #
