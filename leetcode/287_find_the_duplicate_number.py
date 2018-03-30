class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = 0
        slow = 0
        
        # Refer to this article for the proof
        # https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
                
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast:
                return slow
