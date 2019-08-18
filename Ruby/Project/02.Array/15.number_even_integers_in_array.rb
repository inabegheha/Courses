#NABEGHEHA.COM

def check_array(nums)
  count = 0    
  nums.each do |item|
    if((item % 2) == 0)
    count = count + 1
    end 
  end   
  "Even Number is this Array : " + count.to_s
end
print check_array([3, 4, 5, 6]),"\n"
print check_array([3, 4, 5]),"\n"
print check_array([3, 4]) 