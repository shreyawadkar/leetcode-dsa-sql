class Solution(object):
    def rearrangeArray(self, nums):
        a = []
        b = []
        for i in nums:
            if i > 0:
                a.append(i)
            else:
                b.append(i)
        c = []
        for i in range(len(nums)):
            if i % 2 == 0:
                c.append(a[i // 2])
            else:
                c.append(b[i // 2])

        return(c)
        