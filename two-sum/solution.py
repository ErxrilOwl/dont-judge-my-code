class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            rem = target - num
            
            remIndex = -1

            try:
                remIndex = nums.index(rem)

                if remIndex != i:
                    return [i, remIndex]
            except Exception as e:
                pass

        return []