class Solution(object):
    def singleNumber(self, nums):
        element_lists = defaultdict(list)  
        unique_count = 0  
        seen = set()  

        for i in nums:
            if i not in seen:
                seen.add(i)
                unique_count += 1
            element_lists[i].append(i)

    
        for key in element_lists:
            if len(element_lists[key]) == 1:
                return key

        
        