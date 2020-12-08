filename="data2.txt"

file=open(filename, "r")

rs=file.read()
fs=rs.split(",")
il=[]

for i in fs:
    il.append(int(i))

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

print(il)