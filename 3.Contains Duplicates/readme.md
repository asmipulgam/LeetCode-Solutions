# Contains Duplicate

## Problem

Given an integer array `nums`, return `True` if any value appears **at least twice** in the array. Return `False` if every element is distinct.

### Example 1

```text
Input: nums = [1, 2, 3, 1]
Output: True
```

`1` appears more than once, so the array contains a duplicate.

### Example 2

```text
Input: nums = [1, 2, 3, 4]
Output: False
```

Every element is unique.

---

## Approaches

This folder contains three different approaches to solving the **Contains Duplicate** problem:

1. Brute Force
2. Sorting
3. Hash Set

The goal is to compare how different approaches affect the time and space complexity.

---

## 1. Brute Force

The brute-force approach compares every element with the elements that come after it.

If two equal elements are found, we return `True`. If no duplicate is found after checking all pairs, we return `False`.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
```

### Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

This approach does not require additional data structures, but it becomes inefficient for large arrays.

---

## 2. Sorting

If we sort the array first, duplicate values will appear next to each other.

We can then iterate through the sorted array and compare adjacent elements.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False
```

### Complexity

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** Depends on the sorting implementation

The sorting step takes `O(n log n)` time, while checking adjacent elements takes `O(n)` time.

---

## 3. Hash Set

The hash set approach keeps track of the numbers that have already been seen.

For each number:

* Check whether it already exists in the set.
* If it exists, a duplicate has been found.
* Otherwise, add it to the set.

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

### Complexity

* **Time Complexity:** `O(n)` average
* **Space Complexity:** `O(n)`

The hash set provides `O(1)` average-time lookup and insertion, allowing the array to be processed in a single pass.

---

## Complexity Comparison

| Approach    | Time Complexity | Space Complexity                  |
| ----------- | --------------- | --------------------------------- |
| Brute Force | `O(n²)`         | `O(1)`                            |
| Sorting     | `O(n log n)`    | Depends on sorting implementation |
| Hash Set    | `O(n)` average  | `O(n)`                            |
