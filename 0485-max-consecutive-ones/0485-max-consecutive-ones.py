class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_one = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                max_one = max(max_one, count)
            else:
                count = 0
                
        return max_one
        