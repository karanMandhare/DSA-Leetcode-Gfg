class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low=0
        high=n-1
        found=False
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                found=True
                break
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[mid]<=nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return found