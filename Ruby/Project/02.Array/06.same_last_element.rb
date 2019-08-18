#NABEGHEHA.COM

def check_array(a, b)
    (a[0] == b[0] || a[a.length-1] == b[b.length-1])
end
print check_array([1, 2, 5], [7, 5]),"\n" 
print check_array([1, 2, 3], [7, 3, 2]),"\n" 
print check_array([1, 2, 4], [1, 4]) 