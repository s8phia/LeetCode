class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = list(s)
        char_t = list(t)

        sorted_char_s = sorted(char_s)
        sorted_char_t = sorted(char_t)

        return sorted_char_s == sorted_char_t
        