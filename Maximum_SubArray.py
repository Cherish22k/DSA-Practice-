
## 📌 Problem Statement

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

---

## 🧠 Approach: Kadane’s Algorithm

We iterate through the array while keeping track of:

* `current_sum` → Maximum sum ending at current index
* `max_sum` → Maximum sum found so far

At each step:

* Either extend the current subarray
* Or start a new subarray from current element

---

## 💻 Python Solution

```python
class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## 📊 Example

**Input:**

```
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

**Output:**

```
6
```

**Explanation:**
Subarray `[4, -1, 2, 1]` has the maximum sum = 6

---

## ⏱ Complexity Analysis

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

##Difficulty 
Easy


## 🚀 Key Learnings

* Greedy approach
* Importance of dropping negative sums
* Foundation for dynamic programming problems

---

## ⭐ Tags

`Array` `Dynamic Programming` `Greedy`

---

✨ Keep practicing and building consistency!
