#NABEGHEHA.COM

x,y,z = 2,5,4
if x >= y and x >= z
     puts "x = #{x} is greatest."
elsif y >= z and y >= x 
     puts "y = #{y} is greatest."
else 
     puts "z = #{z} is greatest."
end

# OR

def greater(*args)
    return args.to_a.max
end
    
puts greater(3,7,5)