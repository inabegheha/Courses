#NABEGHEHA.COM

def check_array(nums)
    temp = nums[0]
	nums[0] = nums[nums.length - 1]
	nums[nums.length - 1] = temp
	nums
end
print check_array([1]),"\n"
print check_array([1, 3]),"\n"
print check_array([1, 3, 5]),"\n"
print check_array([11, 3, 5, 21])