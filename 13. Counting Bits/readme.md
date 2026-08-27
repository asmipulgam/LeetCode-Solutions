# Counting Bits

## Problem

Given an integer `n`, return an array `ans` of length `n + 1` where:

```text
ans[i]
```

represents the number of `1` bits in the binary representation of `i`.

### Example

```text
Input:
n = 5

Output:
[0, 1, 1, 2, 1, 2]
```

### Explanation

```text
Number    Binary    Number of 1 Bits
0         0         0
1         1         1
2         10        1
3         11        2
4         100       1
5         101       2
```

Therefore:

```text
[0, 1, 1, 2, 1, 2]
```

---

## Approach – Dynamic Programming

Instead of calculating the number of `1` bits for every number independently, we can use previously calculated results.

We create a DP array:

```python
dp = [0] * (n + 1)
```

where:

```text
dp[i] = number of 1 bits in i
```

We also maintain an `offset` that represents the largest power of `2` less than or equal to the current number.

```python
offset = 1
```

---

## Powers of Two

Powers of two have exactly one set bit:

```text
1  = 1
2  = 10
4  = 100
8  = 1000
16 = 10000
```

So whenever we reach a new power of two, we update the offset:

```python
if offset * 2 == i:
    offset = i
```

For example:

```text
i:       1  2  3  4  5  6  7  8
offset:  1  2  2  4  4  4  4  8
```

---

## DP Formula

The main formula used in the solution is:

```python
dp[i] = 1 + dp[i - offset]
```

The `1` represents the set bit contributed by the current power of two.

The remaining part:

```text
i - offset
```

has already been calculated earlier and is available in the DP array.

For example, consider:

```text
i = 5
```

The largest power of two less than or equal to `5` is:

```text
offset = 4
```

Therefore:

```text
dp[5] = 1 + dp[5 - 4]
      = 1 + dp[1]
      = 1 + 1
      = 2
```

In binary:

```text
5 = 101
```

which contains two `1` bits.

---

## Solution

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):

            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp
```

---

## Example Walkthrough

For:

```text
n = 5
```

Initially:

```text
dp = [0, 0, 0, 0, 0, 0]
offset = 1
```

### `i = 1`

```text
dp[1] = 1 + dp[1 - 1]
      = 1 + dp[0]
      = 1
```

```text
dp = [0, 1, 0, 0, 0, 0]
```

### `i = 2`

`2` is a new power of two, so:

```text
offset = 2
```

Then:

```text
dp[2] = 1 + dp[2 - 2]
      = 1 + dp[0]
      = 1
```

```text
dp = [0, 1, 1, 0, 0, 0]
```

### `i = 3`

```text
dp[3] = 1 + dp[3 - 2]
      = 1 + dp[1]
      = 2
```

```text
dp = [0, 1, 1, 2, 0, 0]
```

### `i = 4`

`4` is another power of two:

```text
offset = 4
```

Then:

```text
dp[4] = 1 + dp[4 - 4]
      = 1 + dp[0]
      = 1
```

```text
dp = [0, 1, 1, 2, 1, 0]
```

### `i = 5`

```text
dp[5] = 1 + dp[5 - 4]
      = 1 + dp[1]
      = 2
```

Final result:

```text
[0, 1, 1, 2, 1, 2]
```

---

## Pattern

The DP values repeat after every power of two, with one additional set bit.

For example:

```text
dp[4] = 1 + dp[0]
dp[5] = 1 + dp[1]
dp[6] = 1 + dp[2]
dp[7] = 1 + dp[3]
```

At the next power of two:

```text
dp[8]  = 1 + dp[0]
dp[9]  = 1 + dp[1]
dp[10] = 1 + dp[2]
...
```

This repeating pattern allows us to reuse previously calculated results.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Every number from `1` to `n` is processed exactly once.

### Space Complexity

```text
O(n)
```

The `dp` array stores the number of set bits for every integer from `0` to `n`.

If the returned output array is not counted as auxiliary space, the additional working space is `O(1)`.
