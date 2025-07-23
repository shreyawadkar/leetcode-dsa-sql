class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        m1 = min(n, len(nums1))
    
    
        for _ in range(m1):
            nums1.pop()
        
        
        for j in nums2:
            nums1.append(j)
            
        nums1.sort()
            




