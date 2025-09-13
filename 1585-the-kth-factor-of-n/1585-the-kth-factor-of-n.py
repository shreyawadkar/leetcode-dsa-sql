class Solution(object):
    def kthFactor(self, n, k):
        a = []
        for i in range(1, n+1):
            if n % i == 0:
                a.append(i)
        b = k % len(a)
        if k <= len(a):
            return(a[b-1])
        else:
            return -(a[b-1])




        



    


        