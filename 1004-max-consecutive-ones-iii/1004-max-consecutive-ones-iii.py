class Solution(object):
    def longestOnes(self, nums, k):
        if nums.count(0) == k:
            return len(nums)
        left = 0
        zero = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero +=1 

            while zero > k:
                if nums[left] == 0:
                    zero -= 1

                left+=1

            max_len = max(max_len, right-left+1)
        return max_len
        