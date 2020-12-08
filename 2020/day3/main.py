def part1():
    file=open("data.dat","r")
    read=file.readlines()
    drzewa=0
    mapa=[]
    for i in range(0,len(read)-1,1):
        ml=""
        for j in range(0,50,1):
            ml+=read[i][:-1]

        mapa.append(ml)
    ml=""
    for i in range(0,50,1):
        ml+=read[-1]
    mapa.append(ml)
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=3
        cy+=1
    print(drzewa)

def part2():
    file=open("data.dat","r")
    read=file.readlines()
    drzewa=0
    wynik=1
    mapa=[]
    for i in range(0,len(read)-1,1):
        ml=""
        for j in range(0,100,1):
            ml+=read[i][:-1]

        mapa.append(ml)
    ml=""
    for i in range(0,100,1):
        ml+=read[-1]
    mapa.append(ml)
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=1
        cy+=1
    print("1 1 ",drzewa)
    wynik*=drzewa
    drzewa=0
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=3
        cy+=1
    print("3 1 ",drzewa)
    wynik*=drzewa
    drzewa=0
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=5
        cy+=1
    print("5 1 ",drzewa)
    wynik*=drzewa
    drzewa=0
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=7
        cy+=1
    print("7 1 ",drzewa)
    wynik*=drzewa
    drzewa=0
    cx=0
    cy=0
    while(cy<len(mapa)):
        if mapa[cy][cx]=="#":
            drzewa+=1
        
        cx+=1
        cy+=2
    print("1 2 ",drzewa)
    wynik*=drzewa
    print(wynik)

#part1()
part2()