#NABEGHEHA.COM

def check_array(a, b)
    sum = (a[0]+a[1]+a[2]) - (b[0]+b[1]+b[2])
	if(sum >= 0)
		a
	else
		b
	end
end
print check_array([1, 3, 5], [2, 4, 4]),"\n"
print check_array([11, 3, 5], [21, 0, -4]),"\n" 