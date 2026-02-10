class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num=set(nums)
        for i in nums:
            rev=int(str(i)[::-1])
            num.add(rev)
        
        return len(num)


        