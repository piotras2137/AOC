data = [i.strip('\n') for i in open('data.txt').readlines()]
depth = 0
horizontal = 0
for i in data:
    x = i.split(' ')
    if x[0] == 'down':
        depth+=int(x[1])
    elif x[0] == 'up':
        depth-=int(x[1])
    elif x[0] == 'forward':
        horizontal+=int(x[1])

print(horizontal*depth)

depth = 0
horizontal = 0
aim = 0 
for i in data:
    x = i.split(' ')
    if x[0] == 'down':
        aim += int(x[1])
    elif x[0] == 'up':
        aim -= int(x[1])
    elif x[0] == 'forward':
        horizontal += int(x[1])
        depth += aim*int(x[1])

print(horizontal*depth)

