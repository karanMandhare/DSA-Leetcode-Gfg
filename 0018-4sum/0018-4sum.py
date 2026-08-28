class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        nums.sort()
        result=set()
        for i in range(0,n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==[nums[j-1]]:
                    continue
                                
                k=j+1
                l=n-1
                while k<l:
                    temp=nums[i]+nums[j]+nums[k]+nums[l]
                    if temp<target:
                        k+=1
                    elif temp>target:
                        l-=1
                    else:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
        return [list(r) for r in result]


                    







        