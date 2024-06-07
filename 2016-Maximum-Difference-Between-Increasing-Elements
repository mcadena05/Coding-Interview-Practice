def maximumDifference(self, nums: List[int]) -> int:
        difference = -1

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    difference = max(nums[j] - nums[i], difference)
                    print(difference)
        
        return difference 