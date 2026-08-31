class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)

        for i in range(n):
            is_unique = True

            for j in range(n):
                if i != j and s[i] == s[j]:
                    is_unique = False
                    break
            if is_unique:
                return i

        return -1