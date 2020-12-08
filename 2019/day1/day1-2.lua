function calculatefuel(mass )
    return math.floor(mass/3)-2
end

function bigcalc(mass)
    sm=mass
    sum=0
    while sm>=0 do  
        sm=calculatefuel(sm)
        if sm>=0 then 
        sum=sum+sm
        end
    end
    return sum
end

sum=0

for line in io.lines("data.txt") do
    i=0+line
    sum=sum+bigcalc(i)
end


print(sum)