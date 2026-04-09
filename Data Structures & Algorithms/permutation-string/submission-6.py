class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #li1 = list(s1)
        li2 = list(s2)

        s1 = "".join(sorted(s1))
        print(s1)
        s1s = 0
        for c in s1:
            s1s += ord(c)
        print(s1s)
        
        ord_s2 = {}
        stop = len(li2)-len(s1)+1
        for i in range(len(li2)):
            if i == stop:
                break
            else:
                l = "".join(sorted(li2[i:i+len(s1)]))
                if l == s1:
                    return True
        return False

