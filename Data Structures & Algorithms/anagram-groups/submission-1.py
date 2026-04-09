class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for index, string in enumerate(strs):
            s_str = "".join(sorted(string))
            #print(s_str)
            if s_str in str_dict:
                str_dict[s_str].append(string)
            else:
                str_dict[s_str] = [string] 
        #print(str_dict)
        """
        f_list = []
        for key,value in str_dict.items():
            f_list.append(value)
        """

        return list(str_dict.values())

