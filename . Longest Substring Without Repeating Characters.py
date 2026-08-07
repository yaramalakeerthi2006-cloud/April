class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        right=0
        maxlen=0
        d={}
        while(right<n):
            if(s[right] in d and d[s[right]]>=left):
                left=d[s[right]]+1
            d[s[right]]=right
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
