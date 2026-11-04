class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            sqrt_of_x = mid * mid
            if  sqrt_of_x == x :
                return mid
            elif sqrt_of_x < x:
                low = mid + 1
            else:
                high = mid - 1    
        return high        
                
            

        