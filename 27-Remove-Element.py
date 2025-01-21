def removeElement(self, nums: List[int], val: int) -> int:
    n = 0
    swap = 0

    for i, v in enumerate(nums):
        if v != val:
            # swap with right
            t = nums[swap]
            nums[swap] = nums[i]
            nums[i] = t

            swap += 1
            n += 1
        
        return n