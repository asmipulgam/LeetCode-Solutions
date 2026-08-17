# Maximum Product Subarray

## Problem

Given an integer array `nums`, find a **contiguous subarray** that has the largest product and return that product.

### Example 1

```text
Input: nums = [2, 3, -2, 4]

Output: 6
```

### Explanation

The subarray:

```text
[2, 3]
```

has the largest product:

```text
2 × 3 = 6
```

### Example 2

```text
Input: nums = [-2, 0, -1]

Output: 0
```

---

## Approach – Track Current Maximum and Minimum

Unlike the **Maximum Subarray** problem, we need to keep track of both the **maximum product** and the **minimum product** ending at the current position.

This is necessary because multiplying two negative numbers produces a positive number:

```text
negative × negative = positive
```

Therefore, a very small negative product can become the largest positive product when multiplied by another negative number.

We maintain:

* `curmax` – maximum product ending at the current position
* `curmin` – minimum product ending at the current position
* `res` – maximum product found so far

For every number, we consider three possibilities:

```text
Current number

Previous maximum × current number

Previous minimum × current number
```

Then:

```python
curmax = max(num, old_max * num, old_min * num)

curmin = min(num, old_max * num, old_min * num)
```

---

## Solution

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1, 1

        for i in nums:
            if i == 0:
                curmin, curmax = 1, 1
                continue

            temp = curmax * i

            curmax = max(curmax * i, curmin * i, i)
            curmin = min(temp, curmin * i, i)

            res = max(res, curmax)

        return res
```

---

## Why Track `curmin`?

Consider:

```text
nums = [-2, 3, -4]
```

The product of the entire subarray is:

```text
-2 × 3 × -4 = 24
```

After processing `-2` and `3`, we have a negative minimum product.

When we encounter `-4`, that negative minimum becomes a large positive value:

```text
-6 × -4 = 24
```

If we only tracked the maximum product, we could lose this possibility.

This is why both `curmax` and `curmin` are required.

---

## Handling Zero

A `0` breaks the current product sequence.

For example:

```text
[2, 3, 0, 4, 5]
       ↑
```

A subarray cannot continue multiplying across the `0` without its product becoming `0`.

Therefore, when a zero is encountered, the current maximum and minimum are reset:

```python
if i == 0:
    curmin, curmax = 1, 1
    continue
```

The initial:

```python
res = max(nums)
```

ensures that `0` is still considered as a possible answer.

---

## Example Walkthrough

Consider:

```text
nums = [2, 3, -2, 4]
```

| Number | `curmax` | `curmin` | `res` |
| -----: | -------: | -------: | ----: |
|      2 |        2 |        2 |     4 |
|      3 |        6 |        3 |     6 |
|     -2 |       -2 |      -12 |     6 |
|      4 |        4 |      -48 |     6 |

Final result:

```text
6
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed only once.

### Space Complexity

```text
O(1)
```

Only a few variables are used regardless of the size of the input array.
