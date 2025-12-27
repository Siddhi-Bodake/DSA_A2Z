class Solution:
    def bubble_sort(self,nums):
        n = len(nums)
        for i in range(n-1,-1,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
sol=Solution()
arr=[2,1,4,3,7,6]
print("sorted array : ", sol.bubble_sort(arr))