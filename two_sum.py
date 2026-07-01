# Problem: Two Sum (LeetCode 1)
# Approach: HashMap
# Time Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

      """
Approach:
- Use hashmap to store visited elements
- Check complement in one pass

Why this works:
- Reduces time complexity from O(n^2) to O(n)
"""
