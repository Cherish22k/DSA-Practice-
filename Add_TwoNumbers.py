# Add Two Numbers (LeetCode 2)

## ✍️ Code

```python
# Problem: Add Two Numbers (LeetCode 2)
# Approach: Linked List + Carry Handling
# Time Complexity: O(n)

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

"""
Approach:
- Traverse both linked lists simultaneously
- Add corresponding digits along with carry
- Store result in a new linked list

Why this works:
- Mimics real-life addition digit by digit
- Handles different list lengths and carry efficiently
"""
```
