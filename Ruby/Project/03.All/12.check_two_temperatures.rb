#NABEGHEHA.COM

def temp(temp1, temp2)
    return ( temp1 < 0 && temp2 > 100 ) || ( temp1 > 100 && temp2 < 0 );
end
print temp(110, -1),"\n"
print temp(-1, 110),"\n"
print temp(2, 120)