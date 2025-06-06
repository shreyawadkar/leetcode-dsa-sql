class Solution(object):
    def singleNumber(self, nums):
        elements = defaultdict(list)
        seen = set()

        for i in nums:
            if i not in seen:
                seen.add(i)
            elements[i].append(i)

        for j in elements:
            if len(elements[j]) == 1:
                return j

