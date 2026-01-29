from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0    # total palindrome length
        odd = False   # flag to track if there is any odd count

        for count in freq.values():
            if count % 2 == 0:
                length += count       # use all letters if even
            else:
                length += count - 1  # use the largest even number
                odd = True            # remember we have an odd letter

        if odd:
            length += 1  # we can place one odd letter in the middle

        return length
