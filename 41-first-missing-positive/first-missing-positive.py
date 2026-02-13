class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        for i in range(1,len(nums)+2):
            if i in nums:
                continue
            else:
                return i       

