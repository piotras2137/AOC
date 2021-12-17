text = open('data.txt').readlines()
text = [int(i) for i in text]
notmi = 0 
prev = text[0]
for i in text:
    if i>prev:
        notmi+=1
    prev = i

print(notmi)

notmi = 0 
l = len(text)
for i in range(l-3):
    a = text[i] + text[i+1] + text[i+2]
    b = text[i+1] + text[i+2] + text[i+3]
    if b>a:
        notmi+=1

print(notmi)