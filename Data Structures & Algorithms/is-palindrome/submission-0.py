import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # we have to make all the chracters lower & remove non-alpha charcters & store that value
        foward = re.sub(r'[^a-zA-Z0-9]',"",s).lower()

        # then reverse the string 
        backword = "".join(reversed(foward))


        # see if there equal to each other 
        return foward == backword