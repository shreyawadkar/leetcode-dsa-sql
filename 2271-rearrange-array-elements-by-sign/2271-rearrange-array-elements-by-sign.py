class Solution(object):
    def rearrangeArray(self, nums):
        # a = []
        # b = []
        # for i in nums:
        #     if i > 0:
        #         a.append(i)
        #     else:
        #         b.append(i)
        # res = []
        # for i in range(len(a)):
        #     res.append(a[i])
        #     res.append(b[i])
    
        # return res

        
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res

        