class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1 = sorted(s)
        char2 = sorted(t)

        if char1 == char2:
            return True
        else:
            return False
        