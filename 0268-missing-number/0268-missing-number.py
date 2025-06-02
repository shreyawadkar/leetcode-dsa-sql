class Solution(object):
    def missingNumber(self, nums):
        b = len(nums)
        c = []
        for i in range (0,b+1):
            c.append(i)
        for j in c:
            if j in nums:
                continue
            else:
                return j
        