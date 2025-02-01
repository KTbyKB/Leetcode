#3151. Special Array I
def isArraySpecial(self, nums: List[int]) -> bool:
    for i in range(len(nums)-1):
        f = nums[i] & 1
        s = nums[i+1] & 1
        if f ^ s == 0:
            return False
    return True
