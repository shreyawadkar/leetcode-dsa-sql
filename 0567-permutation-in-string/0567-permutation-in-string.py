class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        left = 0
        target = Counter(s1)
        window = {}
        goal = len(s1)

        for right, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            if right >= goal:
                window[s2[left]] -= 1
                
                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if right - left + 1 == goal:
                if window == target:
                    return True
        
        return False