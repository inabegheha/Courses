#NABEGHEHA.COM

def check_num(a, b, c)
    return ((a + b) == c || (b + c) == a || (c + a) == b)
end

print check_num(9, 12, 21),"\n"
print check_num(0, -5, -5),"\n"
print check_num(-5, 7, 2),"\n"
print check_num(6, 5, 4)