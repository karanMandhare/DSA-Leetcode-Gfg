class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        total=0
        max_total=float("-inf")
        for i in range(0,n):
            total=total+nums[i]
            max_total=max(total,max_total)
            if total<0:
                total=0
        return max_total         