from os import rename


def partuno():
    lines=open("data.dat","r").readlines()
    lines=[int(i.strip("\n")) for i in lines]
    pmt=lines[:25]
    #lines=lines[25:]
    #print(pmt[24]," ",lines[0])
    for i in range(25,len(lines)):

        git=False
        for j in range(i-25,i):
            for k in range(i-25,i):
                if lines[i]==(lines[k]+lines[j]):
                    git=True
        if git==False:
            print(i," ",lines[i])
            break

partuno()