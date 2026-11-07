class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1.sort()
        result = set()

        for num in nums2:

            low = 0
            high = len(nums1) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums1[mid] == num:
                    result.add(num)
                    break
                elif nums1[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1

        return list(result)

    