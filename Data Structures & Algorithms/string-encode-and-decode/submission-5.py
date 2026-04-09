class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        s = ""
        for st in strs:
            print(st)
            sizes.append(str(len(st)))
        for size in sizes:
            s += size
            s += ","
        s += "#"
        for st in strs:
            s += st
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        size = ""
        len_sizes = 0
        for el in s:
            len_sizes += 1
            if el == ",":
                sizes.append(size)
                size = ""
            elif el == "#":
                break
            else:
                size += el
                #sizes.append(size)
            
        s = list(s)[len_sizes:len(s)]
        print(s, sizes)

        n = 0
        t = []
        for size in sizes:
            st = s[n:n+int(size)]
            print(st)
            st = "".join(st)
            t.append(st)
            n += int(size)

        return t
