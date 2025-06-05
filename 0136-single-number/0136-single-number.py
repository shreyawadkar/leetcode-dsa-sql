class Solution(object):
    def singleNumber(self, nums):
        element_lists = defaultdict(list)  # To store elements by value
        unique_count = 0  # Count of unique elements
        seen = set()  # To track new elements

        for i in nums:
            if i not in seen:
                seen.add(i)
                unique_count += 1
            element_lists[i].append(i)

    # Now find the element whose list length is 1
        for key in element_lists:
            if len(element_lists[key]) == 1:
                return key

        return None
        