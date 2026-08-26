# Number of 1 Bits

## Problem

Given a positive integer `n`, return the number of **set bits** in its binary representation.

A **set bit** is a bit whose value is `1`.

This is also known as the **Hamming Weight** of the number.

### Example

```text
Input:
n = 11

Binary representation:
1011

Output:
3
```

### Explanation

The binary representation of `11` is:

```text
1011
```

It contains three `1` bits, so the answer is:

```text
3
```

---

## Approach – Bit Manipulation

The solution uses a useful bit manipulation technique:

```python
n = n & (n - 1)
```

This operation removes the **rightmost set bit (`1`)** from `n`.

We repeatedly remove one set bit and increment a counter until `n` becomes `0`.

---

## Solution

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count
```

---

## How `n & (n - 1)` Works

Consider:

```text
n = 11
```

Its binary representation is:

```text
1011
```

Subtracting `1` gives:

```text
n     = 1011
n - 1 = 1010
```

Now perform a bitwise AND:

```text
  1011
& 1010
------
  1010
```

The rightmost `1` has been removed.

Therefore:

```text
1011 → 1010
```

Each time we perform this operation, exactly one set bit is removed.

---

## Example Walkthrough

For:

```text
n = 11
```

### Iteration 1

```text
n     = 1011
n - 1 = 1010

1011 & 1010 = 1010

count = 1
```

### Iteration 2

```text
n     = 1010
n - 1 = 1001

1010 & 1001 = 1000

count = 2
```

### Iteration 3

```text
n     = 1000
n - 1 = 0111

1000 & 0111 = 0000

count = 3
```

Now:

```text
n = 0
```

so the loop stops.

The final answer is:

```text
3
```

---

## Why Does This Work?

Subtracting `1` from a binary number changes:

* The rightmost `1` into `0`
* All bits after that `1` into `1`

For example:

```text
n     = 1011000
n - 1 = 1010111
```

Performing AND:

```text
  1011000
& 1010111
---------
  1010000
```

removes the rightmost set bit.

Therefore:

```text
n & (n - 1)
```

can be remembered as:

> Remove the rightmost `1` bit.

---

## Alternative Approach – Check Each Bit

Another approach is to check the rightmost bit using:

```python
n & 1
```

and then shift the number to the right:

```python
n >>= 1
```

### Solution

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count
```

Here:

```text
n & 1
```

checks whether the rightmost bit is `1`, while:

```text
n >> 1
```

shifts the bits one position to the right.

---

## Complexity Analysis

### `n & (n - 1)` Approach

If there are `k` set bits, the loop executes `k` times because each iteration removes exactly one `1`.

**Time Complexity:**

```text
O(k)
```

where `k` is the number of set bits.

For a fixed-width integer, this is also bounded by the number of bits.

**Space Complexity:**

```text
O(1)
```

No additional data structures are required.
