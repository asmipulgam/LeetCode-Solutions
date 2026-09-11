# Longest Increasing Subsequence

## Problem

Given an integer array `nums`, return the length of the **longest strictly increasing subsequence**.

A subsequence is created by deleting some or no elements from the array while maintaining the relative order of the remaining elements.

The elements in the subsequence do **not** need to be contiguous.

### Example

```text
Input:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

Output:
4
```

### Explanation

One possible longest increasing subsequence is:

```text
[2, 3, 7, 101]
```

Its length is:

```text
4
```

Therefore, the answer is `4`.

---

## Approach – Dynamic Programming

The solution uses **Dynamic Programming** to calculate the longest increasing subsequence starting from every position.

We create a DP array:

```python
LIS = [1] * len(nums)
```

where:

```text
LIS[i] = length of the longest increasing subsequence
         starting at index i
```

Every element starts with a value of `1` because a single number by itself is always an increasing subsequence of length `1`.

---

## Solution

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)
```

---

## Why Traverse from Right to Left?

For every `nums[i]`, we want to know which elements **after it** can be included in an increasing subsequence.

Therefore, we calculate the answers from right to left:

```python
for i in range(len(nums) - 1, -1, -1):
```

For each `i`, we examine all elements after it:

```python
for j in range(i + 1, len(nums)):
```

If:

```python
nums[i] < nums[j]
```

then `nums[j]` can come after `nums[i]` in an increasing subsequence.

---

## DP Formula

The main recurrence relation is:

```python
LIS[i] = max(LIS[i], 1 + LIS[j])
```

when:

```python
nums[i] < nums[j]
```

The `1` represents the current element `nums[i]`, while `LIS[j]` represents the longest increasing subsequence already calculated starting from `nums[j]`.

---

## Example Walkthrough

Consider:

```text
nums = [1, 2, 4, 3]
```

Initially:

```text
nums = [1, 2, 4, 3]
LIS  = [1, 1, 1, 1]
```

### Starting from `3`

There are no elements after `3`, so:

```text
LIS = [1, 1, 1, 1]
```

### Processing `4`

There are no larger elements after `4`, so:

```text
LIS = [1, 1, 1, 1]
```

### Processing `2`

Both `4` and `3` are greater than `2`.

Possible subsequences include:

```text
[2, 4]
[2, 3]
```

Therefore:

```text
LIS[1] = 2
```

Now:

```text
LIS = [1, 2, 1, 1]
```

### Processing `1`

Since:

```text
1 < 2
```

we can use the subsequence already calculated starting from `2`:

```text
1 + LIS[1]
= 1 + 2
= 3
```

Therefore:

```text
LIS = [3, 2, 1, 1]
```

The maximum value is:

```text
3
```

So the longest increasing subsequence has length `3`.

Possible answers include:

```text
[1, 2, 4]
```

or:

```text
[1, 2, 3]
```

---

## Why Use `max()`?

There may be several larger numbers after the current element.

For example:

```text
nums = [1, 5, 2, 3, 4]
```

Starting from `1`, we could form:

```text
[1, 5]
```

with length `2`.

But we could also form:

```text
[1, 2, 3, 4]
```

with length `4`.

Therefore, we use:

```python
LIS[i] = max(LIS[i], 1 + LIS[j])
```

to keep the longest possible subsequence.

---

## Subsequence vs Subarray

A **subarray** must contain consecutive elements.

A **subsequence** does not.

For example:

```text
nums = [1, 10, 2, 3, 4]
```

The sequence:

```text
[1, 2, 3, 4]
```

is a valid subsequence even though `10` was skipped.

This distinction is important when solving the Longest Increasing Subsequence problem.

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

For every element, we examine the elements that come after it using two nested loops.

### Space Complexity

```text
O(n)
```

The `LIS` array stores one value for every element in `nums`.
