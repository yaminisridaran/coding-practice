
class Solution(object):
    def search(self, nums, target):
    	left, right = 0, len(nums) - 1

    	while left <= right:
    		mid = left + (right - left) / 2
    		if nums[mid] == target:
    			return mid
    		elif (nums[mid] >= nums[left] and nums[left] <= target < nums[mid]) or \
    		     (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
    		    right = mid - 1
    		else:
    		    left = mid + 1
        return -1


if __name__ == "__main__":
   print(Solution().search([4,5,6,7,0,1,2,3], 6))
