class Solution:
    # This approach is O(n) time complexity and O(n) space complexity
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Create a dict
        d = {}

        # For each element in nums
        for num in nums:
            # If element inside dict, then remove that element from the dict
            if num in d:
                del d[num]
            # If element not inside dict, then add that element to the dict
            else:
                d[num] = 0

        # The remaining element in the dict is the "single number"
        l = list(d.keys())
        single_number = l.pop()
        return single_number

    # This approach is O(n) time complexity and O(1) space complexity
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (2 * sum(set(nums))) - sum(nums)
