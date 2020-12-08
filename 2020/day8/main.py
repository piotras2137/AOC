def part1():
    read=open("data.dat","r").readlines()
    vals=[i.strip("\n").split(" ") for i in read ]
    for i in range(0, len(vals)):
        vals[i][1]=int(vals[i][1].strip("+"))
        vals[i].append(0)
    akumlator=0
    i=0
    while i<len(vals):
        print(i," ", vals[i])
        if vals[i][2]==1:
            break

        vals[i][2]+=1

        if vals[i][0]=="acc":
            akumlator+=vals[i][1]
        
        if vals[i][0]=="jmp":
            i+=vals[i][1]-1
        i+=1
    print(akumlator)

part1()