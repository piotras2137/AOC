def part1():
    suma=0
    filename="data.dat"
    file=open(filename,"r")
    rl=file.readlines()
    for line in rl:
        linesplit=line.split(" ")
        numsplit=linesplit[0].split("-")
        cmin=int(numsplit[0])
        cmax=int(numsplit[1])
        if (linesplit[2].count(linesplit[1][0])>=cmin and linesplit[2].count(linesplit[1][0])<=cmax):
            suma+=1

    return suma


def part2():
    suma=0
    filename="data.dat"
    file=open(filename,"r")
    rl=file.readlines()
    for line in rl:
        linesplit=line.split(" ")
        numsplit=linesplit[0].split("-")
        cmin=int(numsplit[0])
        cmax=int(numsplit[1])
        if ((linesplit[2][cmin-1]==linesplit[1][0] and linesplit[2][cmax-1]!=linesplit[1][0]) or (linesplit[2][cmin-1]!=linesplit[1][0] and linesplit[2][cmax-1]==linesplit[1][0])):
            suma+=1
    return suma


print(part1())
print(part2())