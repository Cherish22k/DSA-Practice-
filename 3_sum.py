# 🔢 3Sum (LeetCode #15)

## 🧩 Problem Statement

Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

⚠️ The solution must **not contain duplicate triplets**.

---

## 💡 Approach (Two Pointer + Sorting)

We use an **optimized approach** instead of brute force:

1. **Sort the array**
2. Fix one element (`nums[i]`)
3. Use **two pointers** (`left`, `right`) to find pairs such that:

   ```
   nums[i] + nums[left] + nums[right] = 0
   ```
4. Move pointers based on sum:

   * If sum < 0 → move `left++`
   * If sum > 0 → move `right--`
   * If sum == 0 → store result and skip duplicates

---

## 🧠 Algorithm

* Sort the array
* Loop through each element:

  * Skip duplicates for `i`
  * Initialize two pointers
  * Use while loop to find valid pairs
  * Skip duplicate values for `left` and `right`

---

## 🧾 Code (Python)

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

---

## 📊 Example

**Input:**

```
nums = [-1,0,1,2,-1,-4]
```

**Output:**

```
[[-1, -1, 2], [-1, 0, 1]]
```

**Explanation:**

* (-1) + (-1) + 2 = 0
* (-1) + 0 + 1 = 0

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n²)`
  (Outer loop + two pointer traversal)

* **Space Complexity:** `O(1)`
  (Ignoring output storage)

---

#Difficulty:
Medium


## 🚀 Key Takeaways

* Sorting helps reduce complexity from `O(n³)` → `O(n²)`
* Two-pointer technique is essential for array problems
* Always handle **duplicates carefully**
* Classic problem for interviews 🔥

---

## 🏷️ Tags

`Array` `Two Pointers` `Sorting` `Greedy` `LeetCode`
