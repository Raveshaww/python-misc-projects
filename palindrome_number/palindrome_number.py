class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = str(x)[::-1]
        if str(x) != reversed:
            return False
        return True