def saberi(a, b):
    a.reverse()
    b.reverse()

    if(len(a) > len(b)):
        t = a
        a = b
        b = t

    ans = []
    ost = 0
    for i in range(0, len(a)):
        ans.append((a[i] + b[i] + ost) % 10)
        ost = (a[i] + b[i] + ost) // 10

    for i in range(len(a), len(b)):
        ans.append((b[i] + ost) % 10)
        ost = (b[i] + ost) // 10

    if(ost != 0):
        ans.append(ost)
        
    ans.reverse()
    return ans

def oduzmi(a, b):
    a.reverse()
    b.reverse()

    if(len(a) < len(b)):
        t = a
        a = b
        b = t

    ans = []
    ost = 0

    for i in range(0, len(b)):
        if((a[i] + ost) < b[i]):
            ans.append(10 + a[i] + ost - b[i])
            ost = -1
        else:
            ans.append(a[i] + ost - b[i])
            ost = 0

    for i in range(len(b), len(a)):
        if((a[i] + ost) < 0):
            ans.append(10 + ost)
            ost = -1
        elif((a[i] + ost) < a[i]):
            ans.append(a[i] + ost)
            ost = 0
        else:
            ans.append(a[i])

    ans.reverse()
    return ans

def mnozi(a, b): # list(map(int, list('0' * 2)))
    a.reverse()
    b.reverse()

    if(len(a) > len(b)):
        t = a
        a = b
        b = t

    ans = []
    for i in range(0, len(a)):
        tmp = []
        ost = 0
        for j in range(0, len(b)):
            tmp.append((a[i] * b[j] + ost) % 10)
            ost = (a[i] * b[j] + ost) // 10
        tmp = list(map(int, list('0' * i))) + tmp
        ans.reverse()
        tmp.reverse()
        ans = saberi(ans, tmp)
        ans.reverse()

    if(ost != 0):
        ans.append(ost)

    ans.reverse()
    return ans

def izracunaj(a, b, oper):
    a = list(map(int, a))
    b = list(map(int, b))
    tmp = []
    if(oper == "+"):
        tmp = saberi(a, b)
    elif(oper == "-"):
        tmp = oduzmi(a, b)
    elif(oper == "*"):
        tmp = mnozi(a, b)

    flag = True
    ans = ""
    for i in tmp:
        if(i == 0 and flag):
            continue
        else:
            flag = False
        ans = ans + str(i)
    return ans
    
a = input()
b = input()
oper =input()

print(izracunaj(a, b, oper))
