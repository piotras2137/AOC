import math
def turntodata(table):
    x=0
    y=0

    result=[]
    for val in table:
        if(val[0]=="U"):
            x=0
            y=int(val[1:])
        elif(val[0]=="D"):
            x=0
            y=-int(val[1:])
        elif(val[0]=="L"):
            x=-int(val[1:])
            y=0
        elif(val[0]=="R"):
            x=int(val[1:])
            y=0
        result.append([x,y])

    return result


file=open("data3.txt", "r")
fl=file.readline()
sl=file.readline()


fs=fl.split(",")
ss=sl.split(",")

ft=turntodata(fs)
st=turntodata(ss)
print(ft)
