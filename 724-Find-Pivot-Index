def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        all_sum = sum(nums)
               
        for i, num in enumerate(nums):
            if left_sum ==  (all_sum- left_sum- num):
                return i
            left_sum += num
        return -1