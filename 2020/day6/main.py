def part1():
    letters=[]
    read=open("data6.dat").readlines()
    suma=0
    bigsum=0
    for line in read:
        if line=="\n":
            print(letters)
            bigsum+=len(letters)
            suma=0
            letters=[]
            continue

        if line[-1]=="\n":
            line=line[:-1]

        if len(letters)==0:
            for i in line:
                letters.append(i)
            continue

        for letter in letters:
            if letter not in line or letter=="\n":
                letters.remove(letter)
    bigsum+=len(letters)
    print(letters)
    print(bigsum)

part1()