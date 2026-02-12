class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1)%2==0:
            m=int(len(nums1)/2)
            n=m+1
            median=(nums1[m-1]+nums1[n-1])/2
        else:
            median=nums1[int(len(nums1)/2)]
        return median    