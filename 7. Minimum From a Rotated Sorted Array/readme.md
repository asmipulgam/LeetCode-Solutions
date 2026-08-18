# Find Minimum in Rotated Sorted Array

## Problem

Given a sorted array of unique integers that has been rotated, find and return the **minimum element** in the array.

The solution should run in **O(log n)** time.

### Example 1

```text
Input: nums = [3, 4, 5, 1, 2]

Output: 1
```

### Example 2

```text
Input: nums = [4, 5, 6, 7, 0, 1, 2]

Output: 0
```

### Example 3

```text
Input: nums = [11, 13, 15, 17]

Output: 11
```

---

## Approach – Binary Search

Since the original array is sorted, we can use **Binary Search** to find the minimum element efficiently.

Instead of searching for a specific target, we compare the middle element with the **rightmost element** to determine which half contains the minimum.

We maintain two pointers:

* `l` – left boundary
* `r` – right boundary

Then calculate:

```python
mid = (l + r) // 2
```

---

## How It Works

If:

```python
nums[mid] > nums[r]
```

the minimum must be on the **right side** of `mid`.

Therefore:

```python
l = mid + 1
```

Otherwise:

```python
nums[mid] < nums[r]
```

the minimum is either at `mid` or somewhere to its left.

Therefore:

```python
r = mid
```

Notice that we use:

```python
r = mid
```

instead of:

```python
r = mid - 1
```

because `mid` itself could be the minimum element.

---

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
```

---

## Example Walkthrough

Consider:

```text
nums = [4, 5, 6, 7, 0, 1, 2]
```

Initially:

```text
l = 0
r = 6
```

### Step 1

```text
mid = 3

nums[mid] = 7
nums[r]   = 2
```

Since:

```text
7 > 2
```

the minimum must be to the right:

```text
l = mid + 1 = 4
```

Now:

```text
            l
            ↓
[4, 5, 6, 7, 0, 1, 2]
                  ↑
                  r
```

### Step 2

```text
l = 4
r = 6
mid = 5

nums[mid] = 1
nums[r]   = 2
```

Since:

```text
1 < 2
```

the minimum could be at `mid` or to its left:

```text
r = mid = 5
```

### Step 3

```text
l = 4
r = 5
mid = 4

nums[mid] = 0
nums[r]   = 1
```

Since:

```text
0 < 1
```

we set:

```text
r = mid = 4
```

Now:

```text
l = r = 4
```

Therefore:

```text
nums[4] = 0
```

So the answer is:

```text
0
```

---

## Why Binary Search?

A simple approach would be to iterate through every element and keep track of the minimum:

```python
minimum = nums[0]

for num in nums:
    minimum = min(minimum, num)
```

However, this takes:

```text
O(n)
```

Because the array is sorted and rotated, we can take advantage of its structure and use binary search.

Binary search eliminates approximately half of the remaining search space during each iteration.

---

## Complexity Analysis

### Time Complexity

```text
O(log n)
```

At each step, binary search reduces the search space by approximately half.

### Space Complexity

```text
O(1)
```

Only the `l`, `r`, and `mid` variables are required.
