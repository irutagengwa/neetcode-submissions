class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        # assigns two values position to i and then value to n 
        for i, n in enumerate(nums):
            # what do we need with out current value of n to reach the target 
            difference = target - n
            # is it part of map bcs if so we can just return the values right now 
            if difference in values:
                return [values[difference], i]

            #if not then lets add n to the list of values 
            values[n] = i