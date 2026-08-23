class Solution(object):
    def longestConsecutive(self, nums):
        my_set=set(nums)
        longest=0
        for num in my_set:
            if num-1 not in my_set:
                current_num=num
                count=1
            

                while current_num+1 in my_set:
                    current_num+=1
                    count+=1
                longest=max(count,longest)
        if len(my_set)==0:
            return 0
        else:
            return longest        