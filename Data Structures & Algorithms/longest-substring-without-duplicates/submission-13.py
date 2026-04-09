class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        d = {}
        l = 0
        out = 0

        for i in range(len(s)):
            if s[i] in d:
                l = max(l, d[s[i]]+1)
            d[s[i]] = i
            out = max(out, i-l+1)
        
        return out