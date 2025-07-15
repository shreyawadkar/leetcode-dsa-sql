class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)  
        result = [] 
        uniqueelements = defaultdict(int)

        for num in nums:  
            uniqueelements[num] += 1
  
        percent = n / 3

        for key, value in uniqueelements.items():
            if value > percent:
                result.append(key)
        return result  
        
        