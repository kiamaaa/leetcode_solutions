class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        used = [False] * len(baskets)
        unplaced = 0
        for f in fruits:
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= f:
                    used[j] = True
                    break
            else:
                unplaced += 1
        return unplaced
        
     


        

        