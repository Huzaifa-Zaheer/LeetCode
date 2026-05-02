class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26
        for i in s:
            chars[ord(i) - 97] += 1
        for i in t:
            chars[ord(i) - 97] -= 1
        for cnt in chars:
            if cnt != 0:
                return False
        return True