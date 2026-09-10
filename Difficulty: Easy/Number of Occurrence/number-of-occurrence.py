class Solution:
    def lowerbound(self, arr, target):
        n = len(arr)
        lb = n
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upperbound(self, arr, target):
        n = len(arr)
        ub = n
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def countFreq(self, arr, target):
        llb = self.lowerbound(arr, target)
        uub = self.upperbound(arr, target)

        if llb == len(arr) or arr[llb] != target:
            return 0
        return uub - llb
