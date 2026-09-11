class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if the list has one digit we just return zero 
        if not nums:
            return 0

        counter = 1
        largest = 1
        nums.sort()

        for i in range(len(nums)):
            #skip duplicates
            if nums[i] == nums[i-1]:
                continue 
            elif nums[i] == nums[i-1] + 1:
                counter += 1
            else:
                counter = 1
            if counter > largest:
                largest = counter
        
        return largest