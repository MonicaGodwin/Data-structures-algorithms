class Solution:
    def isPalindrome(self, x: int) -> bool:
        changed = str(x)
        left = 0
        right = len(changed) -1
        if changed[left] == changed[right]:
            return True
            left += 1
            right -= 1
        else:
            return False