class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.strip("!%,&.*-+?'`:").replace(" ", "").replace("'", "").replace(",", "").replace(":", "").lower()

        print(s)

        s_reversed = s[::-1] # [start:stop:step], -1 for step means go from right to left

        print(s_reversed)

        if s == s_reversed:
            return True 
        return False 