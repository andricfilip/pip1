def sabiranje(a , b):
    c = int(a) + int(b)
    return c
def mnozenje(a , b):
    d = int(a) * int(b)
    return d 
def oduzimanje (a , b):
    g = int(a) - int(b)
    return g


print("Unesi neki broj: ")
prvi = int(input())
print("Unesi neki broj: ")
drugi = int(input())
print("Unesi operaciju: ")
operacija = input()
if operacija == "+" :
    print(prvi + drugi)
elif operacija == "-" :
    print(prvi - drugi)
elif operacija == "*" :
    print(prvi * drugi)
else:
    print("Greska")

