from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        t_count = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(t_count)

        left = 0
        min_len = float("inf")
        result = [-1, -1]

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            while have == need:

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = [left, right]

                window[s[left]] -= 1

                if (
                    s[left] in t_count
                    and window[s[left]] < t_count[s[left]]
                ):
                    have -= 1

                left += 1

        l, r = result

        return s[l:r + 1] if min_len != float("inf") else ""