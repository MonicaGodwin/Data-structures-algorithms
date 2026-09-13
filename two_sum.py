class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            for num1 in range(num + 1, len(nums)):
                if nums[num] + nums[num1] == target:
                    return [num, num1]
