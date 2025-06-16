class Solution(object):
    def majorityElement(self, nums):
        element = defaultdict(list)
        for i in nums:
            element[i].append(i)

        big_key = None
        big_len = 0

        for key,i in element.items():
            if len(i) > big_len:
                big_len = len(i)
                big_key = key
        return(big_key)
# count = 0
#     candidate = None

#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)

#     return candidate
        
        