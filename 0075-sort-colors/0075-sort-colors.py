class Solution(object):
    def sortColors(self, nums):
        unique_list = defaultdict(list)
        for i in nums:
            unique_list[i].append(i)
        
        nums[:] = []
        for j in sorted(unique_list.keys()):
            nums.extend(unique_list[j])