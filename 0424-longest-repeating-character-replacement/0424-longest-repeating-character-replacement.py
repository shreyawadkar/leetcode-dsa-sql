class Solution(object):
    def characterReplacement(self, s, k):

        left = 0
        count = [0] * 26
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1

            max_freq = max(max_freq, count[index])

            while (right - left + 1) - max_freq > k:
                left_index = ord(s[left]) - ord('A')
                count[left_index] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        

        return max_len