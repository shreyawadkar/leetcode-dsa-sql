class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
