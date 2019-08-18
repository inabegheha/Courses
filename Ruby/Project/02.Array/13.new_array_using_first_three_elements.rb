#NABEGHEHA.COM

def check_array(nums)
    front = []
	if nums.length >= 3
		front[0] = nums[0]
		front[1] = nums[1]
		front[2] = nums[2]
	elsif nums.length == 2
		front[0] = nums[0]
		front[1] = nums[1]
	else nums.length == 1
	    front[0] = nums[0]
	end
	front
end

print check_array([1, 3, 4, 5]),"\n"
print check_array([1, 2, 3]),"\n"
print check_array([1,2]),"\n"
print check_array([1]),"\n"