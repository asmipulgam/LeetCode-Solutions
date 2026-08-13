# Best Time to Buy and Sell Stock 📈

## Problem

Given an array `prices` where `prices[i]` represents the price of a stock on the `i-th` day, find the **maximum profit** that can be achieved by choosing one day to buy the stock and a later day to sell it.

If no profit can be made, return `0`.

### Example

```text
Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5
```

### Explanation

Buy the stock when the price is `1` and sell it later when the price is `6`.

```text
Profit = Selling Price - Buying Price
       = 6 - 1
       = 5
```

## Approach – Two Pointers

The solution uses two pointers:

* `l` represents the **buying day**.
* `r` represents the **selling day**.

We start with:

```python
l, r = 0, 1
```

If the price at `r` is greater than the price at `l`, we calculate the profit:

```python
profit = prices[r] - prices[l]
```

and update the maximum profit.

If the price at `r` is lower than the price at `l`, we have found a better buying price, so we move the left pointer:

```python
l = r
```

The right pointer continues moving through the array until all prices have been checked.

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maximum = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maximum = max(maximum, profit)
            else:
                l = r

            r += 1

        return maximum
```

## Complexity Analysis

### Time Complexity

```text
O(n)
```

The array is traversed once using the right pointer.

### Space Complexity

```text
O(1)
```

Only a few variables are used, so no additional data structure is required.

## Key Takeaway

The key idea is to keep track of the **lowest buying price seen so far** while checking how much profit could be made by selling at each later price.

Whenever a lower price is found, it becomes the new buying price.

This allows the maximum profit to be found in a single pass through the array.
