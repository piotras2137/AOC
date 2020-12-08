filename="data2.txt"

file=open(filename, "r")

rs=file.read()
fs=rs.split(",")
il=[]
cs=[]
for i in fs:
    il.append(int(i))
    cs.append(int(i))


i=0

found=False

for x in range(0,100,1):
    if found==True:
        break

    for j in range(0,100,1):
        if found==True:
            break
        else:
            for i in range(0, len(il), 1):
                il[i]=cs[i]
            il[1]=x
            il[2]=j
        i=0
        while i<len(il):
            moved=False
            if il[i]==1:
                il[il[i+3]]=il[il[i+1]]+il[il[i+2]]
                moved=True
            elif il[i]==2:
                il[il[i+3]]=il[il[i+1]]*il[il[i+2]]
                moved=True
            elif il[i]==99:
                break

            if moved==True:
                i+=4
            else:
                i+=1

        if il[0]==19690720:
            found=True
        print(x, " ", j )

print(il)