class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the strings 
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        #check if there equal to each other, if so innput true 
        if s_sorted == t_sorted:
            return True
        # if no input false 
        return False
        