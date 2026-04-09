class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        fl = ""

        for char in s:
            if char.isalnum():               # keep only letters and numbers
                fl += char.lower()

        print(fl)

        # reversing string
        fl_reversed = fl[::-1] # [start:stop:step], -1 for step means go from right to left

        return fl_reversed == fl
        


        """
        s = s.strip("!%,&.*-+?'`:").replace(" ", "").replace("'", "").replace(",", "").replace(":", "").lower()

        print(s)

        s_reversed = s[::-1] # [start:stop:step], -1 for step means go from right to left

        print(s_reversed)
        
        if s == s_reversed:
            return True 
        return False 
        """