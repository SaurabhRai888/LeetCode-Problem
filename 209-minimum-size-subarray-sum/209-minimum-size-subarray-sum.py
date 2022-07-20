class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        i, j = -1, 0
        mini = sys.maxsize
        while j < len(nums):
            if nums[j] < target:
                j += 1
                continue
            while nums[j] - nums[i + 1] >= target:
                i += 1
            if nums[j] >= target and j - i < mini:
                mini = j - i
            j += 1
        return mini if mini != sys.maxsize else 0