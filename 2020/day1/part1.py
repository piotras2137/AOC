
filename="adidat.txt"
file=open(filename,"r")
read=file.readlines()
gl=[]

for i in range(0, len(read)-1, 1):
    gl.append(int(read[i][:-1]))
gl.append(int(read[len(read)-1]))

setbreak=False

for first in gl:
    for second in gl:
        if first+second==2020:
            print(first, " ", second, " ", first*second)
            setbreak=True
        
    if setbreak==True:
        break