class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #empty dictionary to store the anagrams in a list 
        anagram = {}
        
        # we are going to loop throught the list of its values 
        for word in strs:
            #how were going to find anagram matches is if sorted its the same thing 
            #this sortes the word the combines it away from a list to one word 
            key = "".join(sorted(word))
            
            #check if the anagram is in our dic if not make one
            if key not in anagram:
                anagram[key] = []
            
            # append the word to the value based of its key 
            anagram[key].append(word)

        # finall we return the values of the dictinary as a list             
        return list(anagram.values())