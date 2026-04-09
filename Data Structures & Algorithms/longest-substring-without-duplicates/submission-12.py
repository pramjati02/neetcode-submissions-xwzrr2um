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
                count = 0
                while count <= len(s[0:index]):
                    if s[index-1] not in st:
                        st += s[index-1]
                    else:
                        break
                    index = index - 1
                    
                    

            if index == len(s)-1:
                d[st] = len(st)
                break

        return max(d.values())