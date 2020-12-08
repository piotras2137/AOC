a=open('data.dat').read().split("\n")[:-1]#otwarcie pliku i rozbicie go na linijki
luggage=set()#zrobienie tego {}
for x in a:#dla kazdego x w a 
    z=x.split(' ')#wrucenie do z splita x " "
    bag=(z[0]+z[1],)#zrobienie samych kolorow z toreb
    if len(z)%4==0:#jezeli rozmiar z jest wiekszy od 4 to 
        for i in range(4,len(z),4):#dla kazdego elementu z 
            bag+=(int(z[i]),z[i+1]+z[i+2])#dodanie do baga  liczb z tego elementu
    else: bag+=(0,)#dodanie do baga 0 
    luggage.add(bag)#dodanie baga do bagarzu 


colors=set({'shinygold'})

n=10#ustawienie n na 10 w celu mi nie znanym
while n>0:#jak n wieksze od 0 
    added=False#nachuj to ?
    for x in luggage:#dla x w luggage
        for carrier in x[1:]:# dla carriera w x [od 1 do ]
            if carrier in colors:#jezeli carrier znajduje sie w colorsach to
                colors.add(x[0])#dodaje do colorsow x[0]
    n-=1#zmniejszenie n o 1 

#ta funkcja dotyczy drugiego 
def contains(bag):
    sum=1
    for x in luggage:
        if x[0]==bag and len(x)>2:
            for i in range(1,len(x),2):
                sum+=x[i]*contains(x[i+1])
    return sum

colors.remove('shinygold')
print('part1',len(colors))
print('part2', contains('shinygold')-1)
