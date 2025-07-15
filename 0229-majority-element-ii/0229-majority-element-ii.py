class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        n = len(nums)  
        uniqueelements = defaultdict(int)

        for num in nums:  # Step 2: Count occurrences
            uniqueelements[num] += 1

        result = []  # Step 3: Store elements occurring >30%
        threshold = n / 3

        for key, value in uniqueelements.items():
            if value > threshold:
                result.append(key)

        return result  
        
        # uniqueelements = defaultdict(int)  

        # for num in nums:
        #     uniqueelements[num] += 1 

        # return dict(uniqueelements)