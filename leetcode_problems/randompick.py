class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.numSize = len(nums)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([i for i,x in enumerate(self.nums) if x == target])
