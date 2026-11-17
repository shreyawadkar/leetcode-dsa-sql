class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        left = 0
        target = Counter(p)
        window = {}
        goal = len(p)
        output = []
        

        for right, char in enumerate(s):
            window[char] = window.get(char,0) + 1

            if right >= goal:
                left_char = s[left]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            if right - left + 1  == goal :
                if window == target:
                    output.append(left)
    
        return output
