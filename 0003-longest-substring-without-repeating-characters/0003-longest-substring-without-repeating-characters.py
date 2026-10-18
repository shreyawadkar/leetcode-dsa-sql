class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        last_seen = {}
        max_count = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_count = max(max_count, right-left+1)

        return max_count

        