function calculatefuel(mass )
    return math.floor(mass/3)-2

end

x=0
sum=0



for line in io.lines("data.txt") do 
    sum=sum+calculatefuel(line)
end


print(sum)