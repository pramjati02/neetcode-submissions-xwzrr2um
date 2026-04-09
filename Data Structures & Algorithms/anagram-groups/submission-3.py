class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        scopy = {}

        for s in strs:
            sorted_str = sorted(s) # will generate a list of the sorted string
            sorted_str = "".join(sorted_str)
            if not sorted_str in scopy:
                scopy[sorted_str] = [s]
            else:
                scopy[sorted_str].append(s)
        
        l = list(scopy.values())
        return l

            
            