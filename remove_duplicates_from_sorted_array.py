class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
    
        new_nums = sorted(list(set(nums)))
        
        nums[:] = new_nums
        
        return len(new_nums)
