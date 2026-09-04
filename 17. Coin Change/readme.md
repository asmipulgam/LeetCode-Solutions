# Coin Change

## Problem

Given an integer array `coins` representing different coin denominations and an integer `amount`, return the **minimum number of coins** required to make up that amount.

You can use each coin denomination an unlimited number of times.

If the amount cannot be made using the given coins, return `-1`.

### Example 1

```text
Input:
coins = [1, 2, 5]
amount = 11

Output:
3
```

### Explanation

The minimum number of coins needed is:

```text
5 + 5 + 1 = 11
```

Therefore:

```text
3 coins
```

### Example 2

```text
Input:
coins = [2]
amount = 3

Output:
-1
```

It is impossible to make an amount of `3` using only coins of denomination `2`.

---

## Approach – Dynamic Programming

The solution uses **bottom-up Dynamic Programming**.

We create a DP array where:

```text
dp[a] = minimum number of coins required to make amount a
```

Instead of solving the original amount directly, we first solve smaller amounts and use those results to calculate larger amounts.

---

## Initialize the DP Array

We create:

```python
dp = [amount + 1] * (amount + 1)
```

The array contains an entry for every amount from:

```text
0 to amount
```

For example, if:

```text
amount = 5
```

the DP array has six positions:

```text
Index:  0  1  2  3  4  5
```

We initialize every value to:

```python
amount + 1
```

which acts as an impossible or infinity value.

---

## Base Case

To make an amount of `0`, we need zero coins:

```python
dp[0] = 0
```

So initially, for `amount = 5`:

```text
dp = [0, 6, 6, 6, 6, 6]
```

---

## DP Formula

For every amount `a`, we try every available coin.

If the coin can be used:

```python
if a - coin >= 0:
```

then the remaining amount is:

```text
a - coin
```

Since we have already calculated the minimum number of coins required for that smaller amount, we can use:

```python
1 + dp[a - coin]
```

The `1` represents the current coin being used.

We then choose the minimum:

```python
dp[a] = min(dp[a], 1 + dp[a - coin])
```

This is the main recurrence relation used in the solution.

---

## Solution

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1
```

---

## Example Walkthrough

Consider:

```text
coins = [1, 2, 5]
amount = 5
```

Initially:

```text
dp = [0, 6, 6, 6, 6, 6]
```

### Amount = 1

Using coin `1`:

```text
dp[1] = 1 + dp[0]
      = 1
```

DP becomes:

```text
[0, 1, 6, 6, 6, 6]
```

### Amount = 2

Using coin `1`:

```text
1 + dp[1] = 2
```

Using coin `2`:

```text
1 + dp[0] = 1
```

Take the minimum:

```text
dp[2] = 1
```

DP becomes:

```text
[0, 1, 1, 6, 6, 6]
```

### Amount = 3

Using coin `1`:

```text
1 + dp[2] = 2
```

Using coin `2`:

```text
1 + dp[1] = 2
```

Therefore:

```text
dp[3] = 2
```

DP becomes:

```text
[0, 1, 1, 2, 6, 6]
```

### Amount = 4

Using coin `1`:

```text
1 + dp[3] = 3
```

Using coin `2`:

```text
1 + dp[2] = 2
```

Therefore:

```text
dp[4] = 2
```

DP becomes:

```text
[0, 1, 1, 2, 2, 6]
```

### Amount = 5

Using coin `1`:

```text
1 + dp[4] = 3
```

Using coin `2`:

```text
1 + dp[3] = 3
```

Using coin `5`:

```text
1 + dp[0] = 1
```

Therefore:

```text
dp[5] = 1
```

Final DP array:

```text
Amount:  0  1  2  3  4  5
dp:      0  1  1  2  2  1
```

---

## Handling an Impossible Amount

Consider:

```text
coins = [2]
amount = 3
```

There is no combination of `2`-value coins that can produce `3`.

Therefore, `dp[3]` remains at its initial placeholder value:

```text
amount + 1
```

We check this at the end:

```python
return dp[amount] if dp[amount] != amount + 1 else -1
```

If no valid solution was found, we return:

```text
-1
```

---

## Complexity Analysis

Let:

```text
A = amount
C = number of coin denominations
```

### Time Complexity

```text
O(A × C)
```

For every amount from `1` to `A`, we check every available coin.

### Space Complexity

```text
O(A)
```

We create a DP array containing `amount + 1` elements.
