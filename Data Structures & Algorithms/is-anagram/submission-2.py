class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        d = {}
        for letter in s:
            if not letter in d:
                d[letter] = 1
            else:
                d[letter] += 1
                
        for letter in t:
            if letter in d:
                d[letter] -= 1
            else:
                return False 
        """
        for value in d.values():
            if value != 0:
                return False
        return True
        """
        return not any(d.values())
        
            
        
        

        #return 

