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
                l = li2[i:i+len(s1)]
                s2s = 0
                for i in range(len(s1)):
                    s2s += ord(l[i])
                ord_s2["".join(sorted(l))] = s2s
        
        print(ord_s2)

        if s1s in ord_s2.values() and s1 in ord_s2.keys():
            return True
        return False

