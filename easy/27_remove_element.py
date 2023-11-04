class Solution(object):
    def removeElement(self, nums, val):
        
        index = []

        nums2 = list(nums)

        for i in range(len(nums2)):

            if nums2[i] == val:
                index.append(i)

        for i in index:

            nums.remove(nums2[i])

        

        return len(nums)



        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        