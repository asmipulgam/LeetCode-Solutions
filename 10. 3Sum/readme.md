# 3Sum

## Problem

Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that:

```text
nums[i] + nums[j] + nums[k] = 0
```

The solution must not contain duplicate triplets.

### Example

```text
Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]
```

### Explanation

The two unique triplets whose sum equals `0` are:

```text
-1 + -1 + 2 = 0
-1 +  0 + 1 = 0
```

---

## Approach – Sorting + Two Pointers

The solution first **sorts the array**.

```python
nums.sort()
```

For example:

```text
Before sorting:
[-1, 0, 1, 2, -1, -4]

After sorting:
[-4, -1, -1, 0, 1, 2]
```

We then iterate through the array and treat each `nums[i]` as the first number of a possible triplet.

For the remaining two numbers, we use the **Two Pointer** technique.

```python
l = i + 1
r = len(nums) - 1
```

The pointers represent:

* `i` → first number
* `l` → second number
* `r` → third number

We calculate:

```python
total = nums[i] + nums[l] + nums[r]
```

---

## Moving the Pointers

### If the sum is too small

```python
if total < 0:
    l += 1
```

Since the array is sorted, moving `l` to the right gives us a larger number and increases the sum.

### If the sum is too large

```python
elif total > 0:
    r -= 1
```

Moving `r` to the left gives us a smaller number and decreases the sum.

### If the sum equals zero

```python
else:
    res.append([nums[i], nums[l], nums[r]])
```

We found a valid triplet.

Then both pointers are moved:

```python
l += 1
r -= 1
```

---

## Solution

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
```

---

## Handling Duplicates

One of the important parts of the 3Sum problem is ensuring that the result contains only **unique triplets**.

### Duplicate `i` Values

After sorting, duplicate values are next to each other.

For example:

```text
[-4, -1, -1, 0, 1, 2]
      ↑   ↑
```

If we already processed the first `-1`, we do not need to process another `-1` as the first element.

Therefore:

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

### Duplicate Left Pointer Values

After finding a valid triplet, we also skip duplicate values at the left pointer:

```python
while l < r and nums[l] == nums[l - 1]:
    l += 1
```

This prevents the same triplet from being added multiple times.

---

## Example Walkthrough

Consider:

```text
nums = [-1, 0, 1, 2, -1, -4]
```

After sorting:

```text
[-4, -1, -1, 0, 1, 2]
```

When:

```text
i = 1
nums[i] = -1
```

the pointers start at:

```text
       i   l        r
       ↓   ↓        ↓
[-4, -1, -1, 0, 1, 2]
```

Calculate:

```text
-1 + -1 + 2 = 0
```

So we add:

```text
[-1, -1, 2]
```

Then the pointers move inward.

Eventually:

```text
-1 + 0 + 1 = 0
```

So we also add:

```text
[-1, 0, 1]
```

Final result:

```text
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

Sorting takes:

```text
O(n log n)
```

The outer loop runs `n` times, and for each position the two pointers can scan through the remaining array:

```text
O(n) × O(n) = O(n²)
```

Therefore, the overall time complexity is:

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

Ignoring the space required for the output and the implementation-dependent space used by sorting, the two-pointer algorithm uses only a few variables.
