class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_negative = False
        # Check whether the number is positive or negative
        if x < 0:
            # If negative, convert into a positive number and make a note to 
            # convert it back into a negative number
            x *= -1
            is_negative = True

        # Convert into str
        x = str(x)

        # Reverse str
        x = self.reverse_string(x)

        # Convert into int
        x = int(x)
        # If x is larger than the max size for a signed integer then return zero
        if x > ((2 << 30) - 1):
            return 0
        # Else, return reversed int
        else:
            if is_negative:
                x *= -1
            return x

    def reverse_string(self, string):
        """Reverse a string"""
        new_string = ""
        for char in string:
            new_string = char + new_string
        return new_string

# Leading zeros
# Input: 1 000 000 000
# Output: 1
# 
# Negative numbers
# Input: -1 000 000 000
# Output: -1
