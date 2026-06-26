class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # keep nums1 is shorter than nums2
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        N1, N2 = len(nums1), len(nums2)
        isOdd = True if (N1+N2)&1 else False
        left, right = 0, N1      # N1 <= N2

        while left <= right:
            mid1 = (left+right)//2
            mid2 = (N1+N2+1)//2 - mid1
            l1 = float('-inf') if mid1==0 else nums1[mid1-1]
            r1 = float('inf') if mid1==N1 else nums1[mid1]
            l2 = float('-inf') if mid2==0 else nums2[mid2-1]
            r2 = float('inf') if mid2==N2 else nums2[mid2]
            if l1<=r2 and l2<=r1:
                if isOdd:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1, r2))/2.0
            elif l1>r2:
                right = mid1-1
            else:
                left = mid1+1