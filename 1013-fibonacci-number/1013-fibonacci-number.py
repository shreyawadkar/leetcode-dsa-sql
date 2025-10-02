class Solution(object):
    def fib(self, n):
        def func_fib(n):
            if n <= 1:       
                return n
            i = func_fib(n-1)     
            j = func_fib(n-2)     
            return i + j
            
        return func_fib(n)






        # if n <= 1:       3
        #     return n
        # i = fib(n-1)     2
        # j = fib(n-2)     1
        # return i + j
    
        # if n <= 1:       2
        #     return n
        # i = fib(n-1)     1
        # j = fib(n-2)     0
        # return i + j
    
        # if n <= 1:       1
        #     return n     1
        









    
  