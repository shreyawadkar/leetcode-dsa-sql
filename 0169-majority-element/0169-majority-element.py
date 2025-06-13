class Solution(object):
    def majorityElement(self, nums):
        element = defaultdict(list)
        for i in nums:
            element[i].append(i)

        
        max_key = None
        max_len = 0
        for key, group in element.items():
            if len(group) > max_len:
                max_key = key
                max_len = len(group)

        return(max_key)