#11 Container With Most Water

def maxArea(self, height: List[int]) -> int:
    mx = 0
    low = 0
    high = len(height)-1
    while(low < high):
        mx = max(mx, (min(height[low], height[high])*(high-low)))
        if height[low] < height[high]:
            low +=1
        else:
            high -= 1
    return mx
