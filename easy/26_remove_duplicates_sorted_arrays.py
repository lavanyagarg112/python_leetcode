class Solution(object):
    def removeDuplicates(self, nums):
        count = 0

        for i in range(len(nums)):

            if i == 0 or nums[i] != prev:
                prev = nums[i]
                nums[count] = nums[i]
                count = count + 1


        return count
                



        