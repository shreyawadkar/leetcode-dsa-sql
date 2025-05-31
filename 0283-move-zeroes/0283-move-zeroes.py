class Solution(object):
    def moveZeroes(self, nums):
        zero_list = []
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                zero_list.append(nums.pop(i))  
            else:
                i += 1  

    
        nums.extend(zero_list)
        return nums
        
        