#NABEGHEHA.COM

def check_array(nums)
    (nums.length >= 1 && nums[0] ==  nums[nums.length-1])
end
print check_array([1, 2, 7]),"\n"
print check_array([3, 1, 2, 3]),"\n"
print check_array([14, 7, 1, 2, 3])