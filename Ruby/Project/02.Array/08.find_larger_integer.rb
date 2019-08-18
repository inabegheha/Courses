#NABEGHEHA.COM

def check_array(nums)
    maxVal = []
   	maxVal[0] = nums[0]
	if(nums[2] >= maxVal[0])
		maxVal[0] = nums[2]
	maxVal[1] = maxVal[0]
	maxVal[2] = maxVal[0]
	end
	maxVal
end
print check_array([1, 2, 5]),"\n" 
print check_array([1, 2, 3]),"\n" 
print check_array([1, 2, 4]) 