
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Check sign
        if i < n:
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1

        # Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

sol=Solution()
a="-123"
print(sol.myAtoi(a))