def part1():
    file=open("data4.dat")
    read=file.readlines()
    psc=0
    cid=False
    suma=0
    for line in read:
        if line=="\n":
            if suma==8:
                psc+=1
            elif suma==7 and cid==False:
                psc+=1
            suma=0
            cid=False
            continue

        if len(line)>1:
            line=line[:-1]
        split=line.split(" ")
        suma+=len(split)
        for j in split:
            ss=j.split(":")
            if ss[0]=="cid":
                cid=True

    print(psc)

def ds():
    slownik={"byr":False,
    "iyr":False,
    "eyr":False,
    "hgt":False,
    "hcl":False,
    "ecl":False,
    "pid":False,
    "cid":True}
    return slownik

def part2():
    suma=0
    file=open("data4.dat")
    read=file.readlines()
    slownik=ds()
    for line in read:

        
        if line=="\n":
            wrong=False
            print(slownik)
            for word in slownik:
                if slownik[word]==False:
                    wrong=True

            if wrong==False:
                suma+=1

            slownik=ds()
            continue


        if len(line)>1:
            line=line[:-1]

        split=line.split(" ")

        for j in split:
            ms=j.split(":")
            if ms[0]=="cid":
                slownik["cid"]=True
            if ms[0]=="byr":
                if int(ms[1])>=1920 and int(ms[1])<=2002:
                    slownik["byr"]=True
            if ms[0]=="iyr":
                if int(ms[1])>=2010 and int(ms[1])<=2020:
                    slownik["iyr"]=True
            if ms[0]=="eyr":
                if int(ms[1])>=2020 and int(ms[1])<=2030:
                    slownik["eyr"]=True
            if ms[0]=="hgt":
                if ms[1][-2:]=="cm":
                    if len(ms[1])>4:
                        if int(ms[1][:-2])>=150 and int(ms[1][:-2])<=193:
                            slownik["hgt"]=True

                if ms[1][-2:]=="in":
                    if len(ms[1])>3:
                        if int(ms[1][:-2])>=59 and int(ms[1][:-2])<=76:
                            slownik["hgt"]=True

            if ms[0]=="hcl":
                if ms[1][0]=="#" and len(ms[1])==7:
                    hcl="0123456789abcdef"
                    tak=True
                    for mss in ms[1][1:]:
                        if mss in hcl:
                            tak=True
                        else:
                            tak=False

                    if tak==True:
                        slownik["hcl"]=True

            if ms[0]=="ecl":
                ecltable=["amb","blu","brn","gry","grn","hzl","oth"]
                for ecl in ecltable:
                    if ms[1]==ecl:
                        slownik["ecl"]=True
                        break
            if ms[0]=="pid":
                if len(ms[1])==9:
                    slownik["pid"]=True

    print(suma)


#part1()
part2()

#byr - birth year
#iyr - issue year
#eyr - expiration year
#hgt - height 
#hcl - hairc color
#ecl - eye color
#pid - passport id
#cid - country id <- tego może nie być