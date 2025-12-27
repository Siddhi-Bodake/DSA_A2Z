#Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.
#A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.

class Solution:
    def selection_sort(self,nums):
        n = len(nums)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i] , nums[min_index] = nums[min_index], nums[i]
        return nums
    
sol=Solution()
arr=[64, 25, 12, 22, 11]
print("sorted array : ", sol.selection_sort(arr))
