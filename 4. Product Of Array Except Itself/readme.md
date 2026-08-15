# Product of Array Except Self

## Problem

Given an integer array `nums`, return an array `res` where:

```text
res[i]
```

is equal to the **product of all elements in `nums` except `nums[i]`**.

The solution should run in **O(n) time** without using division.

### Example

```text
Input: nums = [1, 2, 3, 4]

Output: [24, 12, 8, 6]
```

### Explanation

```text
res[0] = 2 × 3 × 4 = 24
res[1] = 1 × 3 × 4 = 12
res[2] = 1 × 2 × 4 = 8
res[3] = 1 × 2 × 3 = 6
```

---

## Approach – Prefix and Postfix Products

The solution uses **prefix** and **postfix** products.

For every position `i`:

```text
res[i] = product of elements before i × product of elements after i
```

Instead of creating separate prefix and postfix arrays, we directly store the results in the output array.

---

## Step 1: Initialize the Result Array

```python
res = [1] * len(nums)
```

For:

```text
nums = [1, 2, 3, 4]
```

we initially have:

```text
res = [1, 1, 1, 1]
```

---

## Step 2: Calculate Prefix Products

The `prefix` variable stores the product of all elements **before the current index**.

```python
prefix = 1

for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
```

For:

```text
nums = [1, 2, 3, 4]
```

the result after the prefix pass is:

```text
res = [1, 1, 2, 6]
```

This represents:

```text
Index 0 → no elements before it       → 1
Index 1 → 1                           → 1
Index 2 → 1 × 2                       → 2
Index 3 → 1 × 2 × 3                   → 6
```

---

## Step 3: Calculate Postfix Products

Next, we traverse the array from **right to left**.

The `postfix` variable stores the product of all elements **after the current index**.

```python
postfix = 1

for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]
```

During this pass, the existing prefix product is multiplied by the postfix product:

```text
result = prefix × postfix
```

The final result becomes:

```text
[24, 12, 8, 6]
```

---

## Solution

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
```

---

## Example Walkthrough

For:

```text
nums = [1, 2, 3, 4]
```

### Prefix Pass

```text
res = [1, 1, 2, 6]
```

### Postfix Pass

```text
res = [24, 12, 8, 6]
```

Therefore:

```text
Output = [24, 12, 8, 6]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed twice:

* Once from left to right for prefix products.
* Once from right to left for postfix products.

Therefore:

```text
O(n) + O(n) = O(n)
```

### Space Complexity

```text
O(1)
```

The solution uses only `prefix` and `postfix` as additional variables.

The output array `res` is not counted as extra space when analyzing the auxiliary space complexity.
