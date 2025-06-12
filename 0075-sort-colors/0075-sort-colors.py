class Solution(object):
    def sortColors(self, nums):
        groups = defaultdict(list)
        for num in nums:
            groups[num].append(num)
        
        nums[:] = []
        for key in sorted(groups.keys()):
            nums.extend(groups[key])