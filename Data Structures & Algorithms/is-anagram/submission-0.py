class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        if len(s_dict) != len(t_dict):
            return False

        for k in s_dict.keys():
            if s_dict[k] != t_dict[k]:
                return False
        
        return True