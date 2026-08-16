# Maximum Subarray

## Problem

Given an integer array `nums`, find the **contiguous subarray** with the largest sum and return its sum.

A subarray must contain consecutive elements from the original array.

### Example

```text
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6
```

### Explanation

The contiguous subarray with the maximum sum is:

```text
[4, -1, 2, 1]
```

Its sum is:

```text
4 + (-1) + 2 + 1 = 6
```

Therefore, the maximum subarray sum is `6`.

---

## Approach – Kadane's Algorithm

This solution uses **Kadane's Algorithm** to find the maximum subarray sum in a single pass.

The main idea is to keep track of:

* `current_sum` – the maximum sum of a subarray ending at the current position.
* `max_sum` – the maximum sum found so far.

At every element, we decide whether it is better to:

1. Continue the existing subarray by adding the current number.
2. Start a new subarray from the current number.

This can be represented as:

```python
current_sum = max(num, current_sum + num)
```

Then we update the overall maximum:

```python
max_sum = max(max_sum, current_sum)
```

---

## Solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## Example Walkthrough

Consider:

```text
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

| Current Number | Current Sum | Maximum Sum |
| -------------: | ----------: | ----------: |
|             -2 |          -2 |          -2 |
|              1 |           1 |           1 |
|             -3 |          -2 |           1 |
|              4 |           4 |           4 |
|             -1 |           3 |           4 |
|              2 |           5 |           5 |
|              1 |           6 |           6 |
|             -5 |           1 |           6 |
|              4 |           5 |           6 |

The maximum value reached is:

```text
6
```

which comes from:

```text
[4, -1, 2, 1]
```

---

## Why Start a New Subarray?

Suppose the current running sum becomes negative.

For example:

```text
current_sum = -2
next number = 4
```

We have two choices:

```text
Continue previous subarray:
-2 + 4 = 2

Start new subarray:
4
```

Starting a new subarray gives a larger sum.

This is the key idea behind Kadane's Algorithm: **if the previous sum does not help the current element, discard it and start again from the current element.**

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We traverse the array only once.

### Space Complexity

```text
O(1)
```

Only a few variables are used regardless of the size of the input array.
