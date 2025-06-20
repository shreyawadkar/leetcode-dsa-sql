class Solution(object):
    def rearrangeArray(self, nums):
        a = []
        b = []
        for i in nums:
            if i > 0:
                a.append(i)
            else:
                b.append(i)
        res = []
        for i in range(len(a)):
            res.append(a[i])
            res.append(b[i])
    
        return res
        