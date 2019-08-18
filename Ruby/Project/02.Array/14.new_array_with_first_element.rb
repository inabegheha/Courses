#NABEGHEHA.COM

def check_array(a, b)
    front = []
    if(a.length > 0 && b.length > 0)
        front[0] = a[0]
		front[1] = b[0]
    elsif (a.length > 0)
        front[0] = a[0]
    elsif (b.length > 0)
        front[0] = b[0]
    end
    front
end

print check_array([3, 4, 5, 6], [7, 3, 4]),"\n"
print check_array([3, 4, 5], [6, 7, 3, 4, 7]),"\n"
print check_array([3, 4], []) 