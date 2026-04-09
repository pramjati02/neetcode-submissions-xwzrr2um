class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        d = {}
        st = ""

        for index, n in enumerate(s):
            print(st)
            if not n in st:
                st += n
            else:
                d[st] = len(st)
                st = ""
                st += n
                while not s[index-1] in st:
                    st += s[index-1]
                    index = index - 1
                    
                    

            if index == len(s)-1:
                d[st] = len(st)
                break

        return max(d.values())