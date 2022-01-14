prvi = input("")
drugi = input("")
znak = input("")

drugi1 = []
prvi1 = []
rezultat = []


prvi_int = list(prvi)
drugi_int = list(drugi)

if(len(prvi_int) > len(drugi_int)):
    for i in range(len(prvi_int)-len(drugi_int)):
        drugi1.append("0")
    drugi1 = drugi1 + drugi_int
    prvi1 = prvi_int
elif(len(drugi_int) > len(prvi_int)):
    for i in range(len(drugi_int)-len(prvi_int)):
        prvi1.append("0")
    prvi1 = prvi1 + prvi_int
    drugi1 = drugi_int
else:
    prvi1 = prvi_int
    drugi1 = drugi_int

if(znak == "+"):
    for i in range(len(prvi1)-1,-1,-1):
        if(int(prvi1[i]) + int(drugi1[i]) < 10):
            rezultat.append(int(prvi1[i]) + int(drugi1[i]))
        else:
            prenos = (int(prvi1[i]) + int(drugi1[i])) // 10
            trenut = (int(prvi1[i]) + int(drugi1[i])) % 10
            rezultat.append(trenut)
            prvi1[i-1] = prenos + int(prvi1[i-1])
    j = len(rezultat)-1
    i=0
    while(i<=j):
        temp = rezultat[j]
        rezultat[j] = rezultat[i]
        rezultat[i] = temp
        j -= 1
        i += 1
    print(rezultat)
elif(znak == "-"):
    for i in range(len(prvi1)-1,-1,-1):
        if(int(prvi1[i]) + int(drugi1[i]) > 0):
            rezultat.append(int(prvi1[i]) - int(drugi1[i]))
        else:
            prenos = -(int(prvi1[i]) - int(drugi1[i]))
            trenut = 0
            rezultat.append(trenut)
    j = len(rezultat)-1
    i=0
    while(i<=j):
        temp = rezultat[j]
        rezultat[j] = rezultat[i]
        rezultat[i] = temp
        j -= 1
        i += 1
    print(rezultat)
elif(znak == "*"):
    print(rezultat)
