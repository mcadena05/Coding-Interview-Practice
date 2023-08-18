class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] +=1
                
        key_lt = list(num_dict.keys())
        val_lt = list(num_dict.values())
        
        for i in range(len(num_dict)):
            if val_lt[i]==1:
                return key_lt[i]
        
     