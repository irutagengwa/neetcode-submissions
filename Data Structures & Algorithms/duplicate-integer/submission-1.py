class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we have to list for the orginal and for the set
        length_list = len(nums)
        length_set = len(set(nums))
        # compare the length to see if there duplicates 
        if length_list != length_set:
            return True
        return False