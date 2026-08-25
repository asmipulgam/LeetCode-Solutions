# Container With Most Water

## Problem

Given an integer array `height`, where `height[i]` represents the height of a vertical line at index `i`, find two lines that together with the x-axis form a container that holds the **maximum amount of water**.

Return the maximum amount of water the container can store.

### Example

```text
Input:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Output:
49
```

### Explanation

The maximum amount of water is formed by the lines at indices `1` and `8`.

```text
height[1] = 8
height[8] = 7

Width = 8 - 1 = 7
Height = min(8, 7) = 7

Area = Width × Height
     = 7 × 7
     = 49
```

Therefore:

```text
Output = 49
```

---

## Approach – Two Pointers

The optimal solution uses the **Two Pointer** technique.

We initialize two pointers:

```python
l = 0
r = len(height) - 1
```

* `l` starts at the beginning of the array.
* `r` starts at the end of the array.

For every pair of lines, we calculate the amount of water they can contain.

---

## Calculating the Area

The width of the container is the distance between the two pointers:

```python
width = r - l
```

The height of the container is determined by the **shorter line**:

```python
h = min(height[l], height[r])
```

Therefore, the area is:

```python
area = (r - l) * min(height[l], height[r])
```

We keep track of the largest area found:

```python
maximum = max(maximum, area)
```

---

## Why Use the Shorter Height?

The amount of water a container can hold is limited by its **shorter side**.

For example:

```text
Left height  = 8
Right height = 7
```

The container can only hold water up to height `7`.

Therefore:

```text
Container Height = min(8, 7)
                 = 7
```

---

## Moving the Pointers

After calculating the current area, we move the pointer pointing to the **shorter line**.

If:

```python
height[l] < height[r]
```

move the left pointer:

```python
l += 1
```

Otherwise:

```python
r -= 1
```

### Why Move the Shorter Line?

The shorter line limits the current container's height.

Moving the taller line inward would:

* decrease the width
* keep the same shorter line
* therefore, never improve the area

By moving the shorter line, we have a chance of finding a taller line that could produce a larger area.

---

## Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])

            maximum = max(maximum, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maximum
```

---

## Example Walkthrough

Consider:

```text
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Initially:

```text
 l                       r
 ↓                       ↓
[1, 8, 6, 2, 5, 4, 8, 3, 7]
```

The width is:

```text
8 - 0 = 8
```

The height is:

```text
min(1, 7) = 1
```

So:

```text
Area = 8 × 1 = 8
```

Since the left line is shorter, move `l` to the right.

Now:

```text
    l                    r
    ↓                    ↓
[1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Calculate the new area:

```text
Width  = 8 - 1 = 7
Height = min(8, 7) = 7

Area = 7 × 7
     = 49
```

The maximum area becomes:

```text
49
```

The algorithm continues moving the pointers inward until they meet.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each pointer moves through the array at most once.

Instead of checking every possible pair, we eliminate one line during each iteration.

### Space Complexity

```text
O(1)
```

Only a few variables are used:

```text
l
r
area
maximum
```

No additional data structure is required.
