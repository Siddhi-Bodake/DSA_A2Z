class Solution:
    def insertion_sort(self,nums):
        n = len(nums)
        for i in range(1,n):
            key = nums[i]
            j = i-1
            while j>=0 and nums[j]>key:
                nums[j+1] =nums[j]
                j -= 1
            nums[j+1] = key
        return nums
    
sol=Solution()
arr=[12, 11, 13, 5, 6]
print("sorted array : ", sol.insertion_sort(arr))