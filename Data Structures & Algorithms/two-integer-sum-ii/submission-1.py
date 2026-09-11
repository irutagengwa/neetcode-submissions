class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # and empty list to store the values 
        values = {}
        # loop through the values of the list collect the index and value 
        for i , n in enumerate(numbers):
            difference = target - n 
            if difference in values and values[difference] < i:
                return [values[difference] + 1, i + 1]
            values[n] = i 