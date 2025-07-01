class Solution(object):
    def subarraySum(self, nums, k):
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # For subarrays that start from index 0

        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] += 1

        return count
    

        # if k in nums:
        #     a +=1 
        # for i in range(len(nums) - 1):
        #     if nums[i] + nums[i + 1] == k:
        #         a += 1
        #     if i + 2 < len(nums):  
        #         if nums[i] + nums[i + 1] + nums[i + 2] == k:
        #             a += 1
        # return a


        # for j in range(i + 1, len(nums)):
            #     if nums[i] + nums[j] == k: