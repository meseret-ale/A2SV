class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                j += 1
                i += 1
        return len(nums)
