class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        l=0
        ml=0
        for i in range(len(s)):
            if s[i] in m:
                l=max(l,m[s[i]]+1)
            m[s[i]]=i
            ml=max(ml,i-l+1)
        return ml