# Two Sum – Three Approaches

This repository contains three different Python solutions for the classic **Two Sum** problem. The goal is to compare different approaches and understand how choosing the right data structure can improve time complexity.

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices of two numbers** such that they add up to `target`.

### Example

```python
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

**Explanation:**
`nums[0] + nums[1] = 2 + 7 = 9`

---

## Solutions

### 1. Brute Force

The brute-force approach checks every possible pair using nested loops.

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []
```

**Complexity:**

* Time: `O(n²)`
* Space: `O(1)`

This solution is simple and easy to understand, but becomes inefficient as the input size increases.

---

### 2. Sorting + Binary Search

In this approach, the numbers are stored along with their original indices and then sorted.

For each number, we calculate its complement:

```text
complement = target - current_number
```

Binary search is then used to look for the complement in the sorted array.

The original indices are preserved because sorting changes the positions of the elements.

**Complexity:**

* Time: `O(n log n)`
* Space: `O(n)` when storing `(value, original_index)` pairs

This approach improves upon brute force by replacing the linear search for the complement with binary search.

---

### 3. Hash Map – Optimal Solution

The optimal approach uses a Python dictionary as a **hash map**.

As we iterate through the array, we calculate:

```python
complement = target - num
```

We check whether the complement has already been stored in the dictionary.

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
```

The dictionary stores:

```text
number → index
```

For example:

```python
{
    2: 0,
    7: 1
}
```

Dictionary lookups take `O(1)` average time, allowing us to solve the problem in a single pass.

**Complexity:**

* Time: `O(n)`
* Space: `O(n)`

---

## Complexity Comparison

| Approach                | Time Complexity | Space Complexity |
| ----------------------- | --------------- | ---------------- |
| Brute Force             | `O(n²)`         | `O(1)`           |
| Sorting + Binary Search | `O(n log n)`    | `O(n)`           |
| Hash Map                | `O(n)`          | `O(n)`           |

