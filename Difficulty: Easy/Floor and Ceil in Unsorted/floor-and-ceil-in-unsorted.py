class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        c=-1
        f=-1
        n=len(arr)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==x:
                return[arr[mid],arr[mid]]
            elif arr[mid]>=x:
                f=arr[mid]
                high=mid-1
            else:
                c=arr[mid]
                low=mid+1
        return c,f