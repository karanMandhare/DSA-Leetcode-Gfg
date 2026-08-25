class Solution:
    def twoSum(self,arr, target):
        
        n=len(arr)
        my_hash=set()
        for i in range(0,n):
            temp=target-arr[i]

            if temp in my_hash:
                
                return[temp,arr[i]]
            else:
                my_hash.add(arr[i])
        return[]