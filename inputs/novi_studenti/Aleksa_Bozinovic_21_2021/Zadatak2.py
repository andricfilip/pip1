text = input()
N = int(input())
words = []

for i in range(N):
    words.append(input())

while (True):
    bEmpty = True

    for word in words:
        if (word in text):
            bEmpty = False
            text = text.replace(word, "")

    if (bEmpty):
        break

print(text)
