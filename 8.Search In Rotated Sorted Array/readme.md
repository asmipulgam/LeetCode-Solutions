# Search in Rotated Sorted Array

## Problem

Given a sorted integer array `nums` that has been rotated at an unknown pivot, and an integer `target`, return the **index of `target`** if it exists in the array.

If the target does not exist, return `-1`.

The solution should run in **O(log n)** time.

### Example 1

```text
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

Output:
4
```

### Example 2

```text
Input:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

Output:
-1
```

---

## Approach – Modified Binary Search

A normal binary search works on a completely sorted array.

In a rotated sorted array, the entire array is no longer sorted, but an important property still exists:

> At least one half of the array will always be sorted.

For example:

```text
[4, 5, 6, 7, 0, 1, 2]
```

We use binary search to:

1. Find the middle element.
2. Check if the target is the middle element.
3. Determine whether the left or right half is sorted.
4. Check whether the target lies inside the sorted half.
5. Eliminate the half that cannot contain the target.

---

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                return m

            # Left half is sorted
            if nums[l] <= nums[m]:

                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # Right half is sorted
            else:

                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
```

---

## Identifying the Sorted Half

### Left Half is Sorted

We can determine that the left half is sorted using:

```python
if nums[l] <= nums[m]:
```

For example:

```text
[4, 5, 6, 7, 0, 1, 2]
 ↑        ↑
 l        m
```

Here:

```text
nums[l] = 4
nums[m] = 7
```

Since:

```text
4 <= 7
```

the section:

```text
[4, 5, 6, 7]
```

is sorted.

We then check whether the target lies inside this range:

```python
if nums[l] <= target < nums[m]:
    r = m - 1
```

Otherwise, we search the right half:

```python
else:
    l = m + 1
```

---

## Right Half is Sorted

If the left half is not sorted, then the right half must be sorted.

We check whether the target lies inside the sorted right half:

```python
if nums[m] < target <= nums[r]:
    l = m + 1
```

Otherwise, we search the left half:

```python
else:
    r = m - 1
```

---

## Example Walkthrough

Consider:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

Initially:

```text
l = 0
r = 6
m = 3
```

So:

```text
        l        m        r
        ↓        ↓        ↓
       [4, 5, 6, 7, 0, 1, 2]
```

The middle value is:

```text
nums[m] = 7
```

The left half is sorted:

```text
[4, 5, 6, 7]
```

But `0` is not between `4` and `7`, so we eliminate the left half:

```python
l = m + 1
```

Now we search:

```text
[0, 1, 2]
```

The binary search continues until `0` is found at:

```text
index = 4
```

Therefore:

```text
Output: 4
```

---

## Important Conditions

The two main conditions in this solution are:

### Target inside the sorted left half

```python
nums[l] <= target < nums[m]
```

### Target inside the sorted right half

```python
nums[m] < target <= nums[r]
```

These conditions help determine which half of the array can safely be discarded.

---

## Complexity Analysis

### Time Complexity

```text
O(log n)
```

At every iteration, approximately half of the remaining array is eliminated.

### Space Complexity

```text
O(1)
```

Only three pointer variables are used:

```text
l
r
m
```

No additional data structures are required.
