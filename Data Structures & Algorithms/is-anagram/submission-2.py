class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS, charT = {}, {}

        for S in range(len(s)):
            charS[s[S]] = 1 + charS.get(s[S], 0)
            charT[t[S]] = 1 + charT.get(t[S], 0)

        for T in charS:
            if charS[T] != charT.get(T, 0):
                return False

        return True