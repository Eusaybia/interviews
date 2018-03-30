class Solution(object):
    # Original solution, very verbose
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Need to standardise input order
            # we want the longer number to always be on top
                # e.g. 12345
                #       2324
        if len(str(b)) > len(str(a)):
            a, b = b, a
            
        # Determine sign
        a_sign, b_sign = 1, 1
        if a < 0:
            a_sign = -1 
            a *= -1
        if b < 0:
            b_sign = -1
            b *= -1
            
        # Count the number of digits in the longer number
        digits = len(str(a))

        num = 0
        carry = 0
        # Need to isolate each number
            # e.g. x = 12345
            # For 0th signifiance digit (5)
                # floor(x / 10^0) % 10 = 5
            # For 1st signifiance digit (4)
                # floor(x / 10^1) % 10 = 1234 % 10 = 4
        for i in range(0, digits):
            a_digit = (a / 10 ** i) % 10
            b_digit = (b / 10 ** i) % 10
            result = a_digit * a_sign + b_digit * b_sign + carry

            # Need to consider concept of carry
            # if digits sum > 9, the set carry to 1
            # upon summation always add carry and always reset to zero

            carry = 0
            if result > 9:
                result = result % 10
                carry = 1
            num += result * (10 ** i)

        return num

        # What about negative integers?
        # Create test cases
            # One positive one negative
        # 999, 999

