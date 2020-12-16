"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # search through nums list fo a pivot index
    # go through each item in nums
    for i in range(len(nums)):
        # check if current inxes (i) is the pivot index
        left_subarray = nums[0:i] # Will go up to i, but not include it (it's inclusive)
        right_subarray = nums[i+1:] 
        # print(left_subarray, right_subarray)
        # get sum of left subarray
        left_sum = sum(left_subarray)
        # get sum of right subarray
        right_sum = sum(right_subarray)
        # check if they are equal
        if left_sum == right_sum:
            # if equal, return I
            return i
        
    return -1
    
print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))