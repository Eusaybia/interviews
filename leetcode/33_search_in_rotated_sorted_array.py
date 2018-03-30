class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Identify the pivot using binary search
        # Find the smallest value in the array
        lo = 0
        hi = len(nums) - 1
        pivot = 0

        while lo < hi:
            mid = (lo + hi) // 2
            print(lo, mid, hi)
            
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        # The smaller of the elements will be the pivot
        pivot = lo
            
        # Find the target using binary search that accounts for the pivot
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            real_mid = (mid + pivot) % len(nums)

            if target == nums[real_mid]:
                return real_mid
            elif target > nums[real_mid]:
                lo = mid + 1
            elif target < nums[real_mid]:
                hi = mid - 1

        return -1

s = Solution()
arr = [3, 4, 5, 6, 7, 1, 2]
target = 5
print(s.search(arr, target))
