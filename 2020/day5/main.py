s=open('data5.dat').readlines()
m={'F':'0','B':'1','R':'1','L':'0'}
print(max(int("".join(map(m.__getitem__,line[:10])),2)for line in s)) # Part 1