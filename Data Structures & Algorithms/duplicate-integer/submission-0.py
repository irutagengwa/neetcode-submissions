class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # we are first going to creat and empty list 
        items = []
        # loop thorough the filled list and ask if its in out empty list 
        for number in nums:
            # if the number in the list is in out empy list its a duplicate so return false
            if number in items:
                return True
            # else append to the empty list 
            else:
                items.append(number)
        return False