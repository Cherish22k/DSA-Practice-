## 🧩 Remove Duplicates from Sorted List

### 📌 Problem Statement

Given the head of a **sorted linked list**, delete all duplicates such that each element appears only once.

Return the linked list in sorted order.

---

## 💡 Approach

Since the list is already sorted, duplicate elements will always appear next to each other.

We traverse the list and:

* Compare current node with the next node
* If they are equal → remove the next node
* Otherwise → move forward

---

## 💻 Code

```python
class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
```

---

## ⏱️ Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 🧠 Key Takeaway

Sorting helps simplify duplicate removal because duplicates are always adjacent.

✨ Efficient single-pass solution using pointer manipulation.
