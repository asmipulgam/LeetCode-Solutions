# Missing Number

## Problem

Given an array `nums` containing `n` distinct numbers in the range:

```text
[0, n]
```

return the **only number in the range that is missing from the array**.

### Example 1

```text
Input:
nums = [3, 0, 1]

Output:
2
```

### Explanation

The complete range should be:

```text
[0, 1, 2, 3]
```

The number `2` is missing.

---

## Approach – Sum Difference

The solution uses the difference between:

* The expected numbers from `0` to `n`
* The actual numbers present in the array

Instead of calculating two separate sums, we calculate the difference during a single traversal.

We initialize:

```python
res = len(nums)
```

Then for every index `i`:

```python
res += i - nums[i]
```

At the end, all numbers that exist in both the expected range and the input effectively cancel out, leaving only the missing number.

---

## Solution

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]

        return res
```

---

## Why Start With `len(nums)`?

Suppose:

```text
nums = [3, 0, 1]
```

The length of the array is:

```text
n = 3
```

The expected numbers are:

```text
0, 1, 2, 3
```

However, the indices of the array are only:

```text
0, 1, 2
```

Therefore, we initialize:

```python
res = len(nums)
```

to include the final number `n`.

Then the loop adds:

```text
0 - nums[0]
1 - nums[1]
2 - nums[2]
```

So mathematically, we are calculating:

```text
3 + (0 - 3) + (1 - 0) + (2 - 1)
```

which gives:

```text
3 - 3 + 1 + 1 = 2
```

Therefore:

```text
Missing Number = 2
```

---

## Example Walkthrough

Consider:

```text
nums = [3, 0, 1]
```

Initially:

```text
res = len(nums)
    = 3
```

### Iteration 1

```text
i = 0
nums[i] = 3

res += 0 - 3
res = 3 - 3
res = 0
```

### Iteration 2

```text
i = 1
nums[i] = 0

res += 1 - 0
res = 0 + 1
res = 1
```

### Iteration 3

```text
i = 2
nums[i] = 1

res += 2 - 1
res = 1 + 1
res = 2
```

Final result:

```text
2
```

---

## Mathematical Idea

The solution is effectively calculating:

```text
Sum of expected numbers - Sum of actual numbers
```

For:

```text
nums = [3, 0, 1]
```

the expected numbers are:

```text
0 + 1 + 2 + 3 = 6
```

The actual numbers are:

```text
3 + 0 + 1 = 4
```

Therefore:

```text
6 - 4 = 2
```

The difference is the missing number.

Instead of explicitly calculating both sums, the solution combines the operations:

```python
res += i - nums[i]
```

---

## Alternative Python Syntax

The same solution can also be written using `enumerate()`:

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i, num in enumerate(nums):
            res += i - num

        return res
```

Here:

```text
i   → current index
num → current value
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed exactly once.

### Space Complexity

```text
O(1)
```

Only a single result variable and loop variable are used. No additional data structure is required.
