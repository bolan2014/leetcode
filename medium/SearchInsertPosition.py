class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums.append(target)
        #nums.sort()
        #return nums.index(target)
        
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
