a = []
b = []
c = []
d = []
pet = 5
def sabiranje(a, b):
    n = len(a)
    m = len(b)
    k = 0
    if (n > m):
        for i in range(0, n):
            c.append(pet)
        for i in range(0, m):
            c[i] = int(a[n - i - 1]) + int(b[m - i - 1]) + k
            k = c[i] // 10
            c[i] = c[i] % 10
        for i in range(m,  n):
            c[i] = int(a[n - i - 1]) + k
            k = c[i] // 10
            c[i] = c[i] % 10
        if (k > 0):
            c.append(k)
        for i in range(0, n):
            d.append(c[n - i - 1])
    else:
        for i in range(0, m):
            c.append(pet)
        for i in range(0, n):
            c[i] = int(a[n - i - 1]) + int(b[m - i - 1]) + k
            k = c[i] // 10
            c[i] = c[i] % 10
        for i in range(n,  m):
            c[i] = int(b[m - i - 1]) + k
            k = c[i] // 10
            c[i] = c[i] % 10
        if (k > 0):
            c.append(k)
        for i in range(0, m):
            d.append(c[m - i - 1])
    return d
def mnozenje(a, b):
    n = len(a)
    m = len(b)
    s = 0
    for i in range(0, n):
        c[i] *= a[i] * 10**(n - i - 1)
        for j in range(0, m):
            c[i] *= b[j] * 10**(m - j - 1)
    for i in range(0, n):
        s+= c[i]
    d.append(str(s))
    return d
t = input()
for i in range(0, len(t)):
    a.append(t[i])
p = input()
for j in range(0, len(p)):
    b.append(p[j])
znak = input()
if (znak == '+'):
    d = sabiranje(a, b)
if (znak == '-'):
    c = int(t) - int(p)
if (znak == '*'):
    d = mnozenje(a, b)
print(str(d))
