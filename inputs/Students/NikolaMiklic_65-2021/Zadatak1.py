def Sabiranje(a,b):
    return a+b
def Oduzimanje(a,b):
    return a-b
def Mnozenje(a,b):
    return a*b



a = input()
b = input()
str = input()
a1 = len(a)
b1 = len(b)
if str == '+':
    c = Sabiranje(int(a),int(b))
if str == '-':
    c = Oduzimanje(int(a),int(b))
if str == '*':
    c = Mnozenje(int(a),int(b))
    




print(c)


