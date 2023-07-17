# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Define contenders dictionary
        contenders_dict = {}

        # For loop through array
        for i in range(len(nums)):

            # Define complement
            complement = target - nums[i]

            # If complement in contenders_dict
            if complement in contenders_dict:

                # Return complement's index in dict and index from array
                return [contenders_dict[complement], i]

            # If complement is not in contenders_dict
            else:

                # Append nums[i]:i to contenders_dict
                contenders_dict[nums[i]] = i

        # Return empty list if no solution found
        return []

# Note: "array" and "list" interchangeable for Python

# The time complexity of this algorithm is O(n), where n is the number of elements in the input list nums.

# This is because we're doing a single pass through the list (nums), and for each element, we're performing a constant time operation: looking up an item in a dictionary. Since dictionary operations such as insert and lookup have a time complexity of O(1) on average in Python, the overall time complexity of the function is O(n).

# In other words, as the number of elements in the input list increases linearly, the time it takes for this function to run will also increase linearly.

# The space complexity of the algorithm is also O(n) because in the worst case scenario, where no two numbers in the list add up to the target, we would end up storing every number from the list in the dictionary.
        
