file = open('data.dat', 'r')
numbers = [ int(number)  for number in file ]
for first in numbers:
    for second in numbers:
        if first + second == 2020:
            print ('part 1 ', first * second)
        for third in numbers:
            if first + second + third == 2020:
                print('part 2 ', first * second * third)