def racuanje(a, b, znak):
    if(znak == '+'):
        k = int(a) + int(b)
        return k
    if(znak == '-'):
        k = int(a) - int(b)
        return k
    if(znak == '*'):
        k = int(a) * int(b)
        return k

print("Unesite prvu listu: ")
broj1 = input()
print("Unesite drugu listu: ")
broj2 = input()
print("Unesite znak operacije: ")
znak = input()

y = racuanje(broj1, broj2, znak)


print(y)
