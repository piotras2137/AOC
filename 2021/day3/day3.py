from os import waitpid


data = [i.strip('\n') for i in open('data.txt').readlines()]

zeros = [ 0 for i in range(len(data[0]))] 
ones =  [ 0 for i in range(len(data[0]))] 

for i in data:
    for j in range(len(i)):
        if i[j]=='0':
            zeros[j]+=1
        else:
            ones[j]+=1

gamma = ''
epsion = '' 

for i in range(len(zeros)):
    if zeros[i]>ones[i]:
        gamma+='0'
        epsion+='1'
    else:
        gamma+='1'
        epsion+='0'
print(int(gamma,2),'\n',int(epsion,2),'\n',int(gamma,2)*int(epsion,2))
