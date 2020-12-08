
filename="data.txt"
file=open(filename,"r")
read=file.readlines()
gl=[]

for i in range(0, len(read)-1, 1):
    gl.append(int(read[i][:-1]))
gl.append(int(read[len(read)-1]))

setbreak=False

for first in gl:
    for second in gl:
        for third in gl:
            if first+second+third==2020:
                print(first, " ", second," ",third ," ", first*second*third)
                setbreak=True
        if setbreak==True:
            break
        
    if setbreak==True:
        break
        