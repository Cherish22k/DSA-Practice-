## 🏆 Best Time to Buy and Sell Stock

### 📌 Problem Statement

You are given an array `prices` where `prices[i]` represents the stock price on the `i-th` day.

You need to maximize your profit by choosing:

* One day to **buy**
* A later day to **sell**

Return the **maximum profit** possible. If no profit can be made, return `0`.

---

## 🧠 Approach 1: Brute Force

### 💡 Idea

* Try every possible pair of days
* Buy on day `i` and sell on day `j` (where `j > i`)
* Track the maximum profit

### 💻 Code

```python
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit
```

### ⏱️ Complexity

* **Time Complexity:** O(n²)
* **Space Complexity:** O(1)

### ❌ Drawback

* Very slow for large inputs (can cause TLE)

---

## ⚡ Approach 2: Optimal Solution

### 💡 Idea

* Keep track of the **minimum price so far**
* At each step, calculate potential profit
* Update maximum profit

### 💻 Code

```python
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
```

### ⏱️ Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## 🔍 Comparison

| Approach    | Time Complexity | Space Complexity | Notes              |
| ----------- | --------------- | ---------------- | ------------------ |
| Brute Force | O(n²)           | O(1)             | Slow, not scalable |
| Optimal     | O(n)            | O(1)             | Efficient ✅        |

---

#Diffculty:
Medium
    
---

✨ This problem is a great example of how optimizing from brute force to an efficient approach can significantly improve performance.
