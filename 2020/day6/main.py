import collections
    
def part1():
    read=open("data.dat","r").read().split("\n\n")
    suma=0
    for i in read:
        table=i.split("\n")
        letters=[letter for letter in table[0]]
        for word in range(1,len(table)):
            if table[word]=="":
                continue
            for letter in table[word]:
                if letter not in letters:
                    letters.append(letter)
        suma+=len(letters)
    return suma

def part2():
    read=open("data.dat","r").read().split("\n\n")
    suma=0
    for i in read:
        table=i.split("\n")
        letters=[letter for letter in table[0]]
        newletters=[]
        for word in range(1,len(table)):
            if table[word]=="":
                continue
            for letter in table[word]:
                if letter in letters:
                    newletters.append(letter)
            print(newletters)
            letters=newletters
            newletters=[]
        suma+=len(letters)
    return suma

def both():
    read=open("data.dat","r").read().split("\n\n")
    suma=0
    for i in read:
        table=i.split("\n")
        letters=[letter for letter in table[0]]
        for word in range(1,len(table)):
            if table[word]=="":
                continue
            for letter in table[word]:
                if letter not in letters:
                    letters.append(letter)
        suma+=len(letters)
    print(suma)
    suma=0
    for i in read:
        table=i.split("\n")
        letters=[letter for letter in table[0]]
        newletters=[]
        for word in range(1,len(table)):
            if table[word]=="":
                continue
            for letter in table[word]:
                if letter in letters:
                    newletters.append(letter)
            print(newletters)
            letters=newletters
            newletters=[]
        suma+=len(letters)
    print(suma)


def notmine():
    with open("data.dat") as f:
        l = f.read()[:-1].split("\n\n")
    print(sum(x != "\n" for c in map(collections.Counter, l) for x in c))
    print(sum(c[x] > c.get("\n", 0) for c in map(collections.Counter, l) for x in c))


wynik=part1()
print(wynik)
notmine()