# Two Sum II – Input Array Is Sorted

## Problem

Given a **1-indexed sorted array** of integers `numbers`, find two numbers that add up to a given `target`.

Return the indices of the two numbers as:

```text
[index1, index2]
```

where:

```text
1 <= index1 < index2 <= numbers.length
```

The input array is already sorted in **non-decreasing order**.

### Example

```text
Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]
```

### Explanation

```text
2 + 7 = 9
```

The numbers `2` and `7` are located at positions `1` and `2`.

Since the problem uses **1-based indexing**, the answer is:

```text
[1, 2]
```

---

## Approaches

This folder contains two approaches:

1. Brute Force
2. Two Pointers

---

## 1. Brute Force

The brute-force approach checks every possible pair until two numbers are found whose sum equals the target.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
```

We return:

```python
[i + 1, j + 1]
```

instead of:

```python
[i, j]
```

because the problem requires **1-indexed positions**.

### Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

---

## 2. Two Pointers

Since the input array is already sorted, we can solve the problem more efficiently using **two pointers**.

We initialize:

```python
l = 0
r = len(numbers) - 1
```

The left pointer starts at the smallest number and the right pointer starts at the largest number.

For each pair, calculate:

```python
current_sum = numbers[l] + numbers[r]
```

There are three possibilities.

### Sum Equals Target

If:

```python
current_sum == target
```

we have found the answer.

Since the problem uses 1-based indexing:

```python
return [l + 1, r + 1]
```

### Sum Is Too Large

If:

```python
current_sum > target
```

we need a smaller sum.

Because the array is sorted, we move the right pointer to the left:

```python
r -= 1
```

### Sum Is Too Small

If:

```python
current_sum < target
```

we need a larger sum.

Therefore, we move the left pointer to the right:

```python
l += 1
```

---

## Two Pointer Solution

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]

            elif current_sum > target:
                r -= 1

            else:
                l += 1
```

---

## Example Walkthrough

Consider:

```text
numbers = [2, 7, 11, 15]
target = 9
```

Initially:

```text
 l          r
 ↓          ↓
[2, 7, 11, 15]
```

Calculate:

```text
2 + 15 = 17
```

Since:

```text
17 > 9
```

the sum is too large, so move `r` left.

```text
 l      r
 ↓      ↓
[2, 7, 11, 15]
```

Now:

```text
2 + 11 = 13
```

Again:

```text
13 > 9
```

Move `r` left again.

```text
 l   r
 ↓   ↓
[2, 7, 11, 15]
```

Now:

```text
2 + 7 = 9
```

The target has been found.

The Python indices are:

```text
l = 0
r = 1
```

Since the problem requires 1-based indexing:

```text
[0 + 1, 1 + 1]
```

Therefore:

```text
Output: [1, 2]
```

---

## Complexity Comparison

| Approach     | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Brute Force  | `O(n²)`         | `O(1)`           |
| Two Pointers | `O(n)`          | `O(1)`           |


