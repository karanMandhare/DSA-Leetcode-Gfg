class Solution(object):
    def missingNumber(self, nums):
        sum1=0
        sum2=0
        for i in range(0,len(nums)+1):
            sum1=sum1+i
        for i in nums:
            sum2=sum2+i
        return sum1-sum2