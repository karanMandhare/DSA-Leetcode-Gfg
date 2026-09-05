class Solution(object):
    def searchRange(self, nums, target):
        def lowerbound(nums,target):
            n=len(nums)
            lb=n
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb

        def upperbound(nums,target):
            n=len(nums)
            ub=n
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>target:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            return ub
        lower=lowerbound(nums,target)
        if lower==len(nums) or nums[lower]!=target:
            return[-1,-1]
        else:
            upper=upperbound(nums,target)

            return[lower,upper-1]


        