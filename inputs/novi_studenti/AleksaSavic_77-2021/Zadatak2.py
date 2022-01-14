txt = input()
n = int(input())

u = []

for x in range (n):
    s = input()
    u.append(s)
    y = 0
    txt2 = txt
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

for i in range (len(u)):
    s = u[i];
    y = 0
    txt2 = txt
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

for i in range (len(u)):
    s = u[i];
    y = 0
    txt2 = txt
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

for i in range (len(u)):
    s = u[i];
    y = 0
    txt2 = txt
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

for i in range (len(u)):
    s = u[i];
    y = 0
    txt2 = txt
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

    y = 0
    for i in range(len(txt)):
        if(txt[i] == s[0]):
            if(txt[i:i+len(s)] == s):
                txt2 = txt2[0:i-y] + txt2[i+len(s)-y:len(txt)]
                y += len(s)
    txt = txt2

print(txt)
