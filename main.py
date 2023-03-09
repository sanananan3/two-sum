def twoSum(self, nums: List[int], target: int) -> List[int]:

	nums = List(map(int, input().split()))
	target= int(input('target = '))
	
	for i in range(0, len(nums)):
	    for j in range(i+1, len(nums)):
		    if nums[i] + nums[j] == target:
		      return [i, j]


	
	return
