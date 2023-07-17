# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Sort the given array
        nums.sort()

        # Loop through the given sorted array
        for i in range(len(nums) - 1):

            # Check if the current value and the next value match 
            if nums[i] == nums[i+1]:

                # Return true
                return True

        # Return false
        return False

# The time complexity of the provided containsDuplicate function can be analyzed as follows:

# Sorting the array: The line nums.sort() sorts the given array in ascending order. The time complexity of a standard sorting algorithm, such as merge sort or quicksort (which is typically used in Python's built-in sort() method), is O(n log n), where n is the length of the array.

# Looping through the sorted array: The for loop iterates through the sorted array once, from the first element to the second-to-last element. The time complexity of this loop is O(n), where n is the length of the array.

# Overall, the dominant factor in the time complexity is the sorting step, which has a complexity of O(n log n). Therefore, the time complexity of the containsDuplicate function is O(n log n).

# Note: If the array is already sorted before calling the function, the time complexity will reduce to O(n) as the sorting step will not be required. However, in the general case where the array is unsorted, the time complexity is O(n log n) due to the sorting operation.
