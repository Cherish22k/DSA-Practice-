# Valid Parentheses

## Problem
Given a string containing '()[]{}', determine if it is valid.

## Approach
- Use a stack
- Push opening brackets
- Pop when matching closing bracket appears

## Complexity
- Time: O(n)
- Space: O(n)2


#Code
class Solution:
    def isValid(self, s):
        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
