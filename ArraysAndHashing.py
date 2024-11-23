
#Contains Duplicate
class Solution:
    def hasDuplicate(self, nums:list[int]) -> bool:

        nums = [1,2,3,3]
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
            return False
        