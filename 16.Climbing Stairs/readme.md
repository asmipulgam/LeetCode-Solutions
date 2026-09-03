# Climbing Stairs

## Problem

You are climbing a staircase with `n` steps.

Each time, you can climb either:

* `1` step
* `2` steps

Return the number of **distinct ways** you can reach the top.

### Example 1

```text
Input:
n = 2

Output:
2
```

There are two possible ways:

```text
1 + 1
2
```

### Example 2

```text
Input:
n = 3

Output:
3
```

The possible ways are:

```text
1 + 1 + 1
1 + 2
2 + 1
```

---

## Approach – Dynamic Programming

The key observation is that to reach step `n`, the final move must come from either:

```text
Step n - 1  → take 1 step
Step n - 2  → take 2 steps
```

Therefore, the number of ways to reach step `n` is:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

This creates the same pattern as the **Fibonacci sequence**.

For example:

```text
n = 1 → 1 way
n = 2 → 2 ways
n = 3 → 3 ways
n = 4 → 5 ways
n = 5 → 8 ways
```

---

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
```

---

## Understanding `one` and `two`

Instead of creating an entire DP array, we only keep track of the previous two values.

```python
one = 1
two = 1
```

These variables represent the number of ways needed for the two previous states.

At each iteration:

```python
temp = one
one = one + two
two = temp
```

The new value is calculated by adding the previous two values.

This follows the recurrence:

```text
current = previous + previous_previous
```

---

## Example Walkthrough

Consider:

```text
n = 5
```

Initially:

```text
one = 1
two = 1
```

The values change as follows:

| Iteration | `one` | `two` |
| --------: | ----: | ----: |
|     Start |     1 |     1 |
|         1 |     2 |     1 |
|         2 |     3 |     2 |
|         3 |     5 |     3 |
|         4 |     8 |     5 |

Therefore:

```text
Output = 8
```

There are `8` different ways to reach the top of a staircase with `5` steps.

---

## Why Does This Work?

To reach any step, there are only two possibilities for the final move.

For example, to reach step `5`:

```text
                Step 5
               /      \
          +1 step      +2 steps
             /            \
         Step 4          Step 3
```

So:

```text
ways(5) = ways(4) + ways(3)
```

If:

```text
ways(4) = 5
ways(3) = 3
```

then:

```text
ways(5) = 5 + 3
        = 8
```

This same relationship applies to every step.

---

## DP Array Alternative

The same idea can also be implemented using a DP array:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
```

The recurrence is:

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

The optimized solution avoids storing the entire array because only the previous two values are needed.

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

We calculate the result by iterating through the staircase once.

### Space Complexity

```text
O(1)
```

The optimized solution only uses a few variables regardless of the value of `n`.
