# 🔢 Integer to Roman (LeetCode #12)

## 🧩 Problem Statement

Given an integer, convert it into a Roman numeral.

Roman numerals are represented using the following symbols:

| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

Roman numerals follow specific rules, including **subtractive notation**:

* IV = 4, IX = 9
* XL = 40, XC = 90
* CD = 400, CM = 900

---

## 💡 Approach

We use a **greedy algorithm**:

1. Store all possible Roman values (including subtractive cases like 900, 400, etc.).
2. Start from the largest value.
3. Keep subtracting the value from the number while appending its Roman symbol.
4. Continue until the number becomes 0.

This ensures we always build the correct Roman numeral from largest to smallest.

---

## 🧠 Algorithm

* Create two arrays:

  * `val[]` → integer values
  * `symbols[]` → corresponding Roman numerals
* Traverse both arrays:

  * While `num >= val[i]`, append symbol and subtract value

---

## 🧾 Code (Python)

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = ""

        for i in range(len(val)):
            while num >= val[i]:
                result += symbols[i]
                num -= val[i]

        return result
```

---

## 📊 Example

**Input:**
`num = 3749`

**Output:**
`"MMMDCCXLIX"`

**Explanation:**

* 3000 → MMM
* 700 → DCC
* 40 → XL
* 9 → IX

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(1)`
  (Since the number of Roman symbols is fixed)

* **Space Complexity:** `O(1)`

---

## 🚀 Key Takeaways

* Greedy approach works perfectly for Roman numeral conversion.
* Always include subtractive cases (`IV`, `IX`, etc.).
* Process from largest to smallest values.

---

## 🏷️ Tags

`Greedy` `String` `Math` `LeetCode`
