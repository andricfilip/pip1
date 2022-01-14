def sabiranje(a,b):
    n = int(a) + int(b)
    return n
def oduzimanje(a,b):
    n = int(a) - int(b)
    return n
def mnozenje(a,b):
    n = int(a) * int(b)
    return n

print("Unesi ceo broj ")
broj1 = int(input())
print("Unesi ceo broj ")
broj2 = int(input())
print("Unesi znak ")
znak = input()
if (znak == "+"):
    print(broj1 + broj2)
elif(znak == "-"):
    print(broj1 - broj2)
else:
    print(broj1 * broj2)
    



