class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for num in nums:
            if num not in duplicate_dict:
                duplicate_dict[num]= 1
            else:
                duplicate_dict[num] +=1
        for value in duplicate_dict.values():
            if value != 1:
                return True
        
        return False
    




    nums_set = set(nums)
         
         if len(nums) > len(nums_set):
            return True
         else:
            return False