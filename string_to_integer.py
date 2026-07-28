class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //= 10

            if x == reverse:
                print("it is paalandrome")
            else:
                print("not pallandrome")

Sol=Solution()
x=int(input("enter the any no"))
print(Sol.isPalindrome(x))
