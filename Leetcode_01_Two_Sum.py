#1. Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = dict()
    n = len(nums)
    for i in range(n):
        t = target - nums[i]
        if t in d:
            return sorted([i,d[t]])
        d[nums[i]]= i

