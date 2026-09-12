# Longest Common Subsequence

## Problem

Given two strings `text1` and `text2`, return the length of their **longest common subsequence**.

A **subsequence** is a sequence that can be created by deleting some characters without changing the relative order of the remaining characters.

The characters do **not** need to be contiguous.

### Example 1

```text
Input:
text1 = "abcde"
text2 = "ace"

Output:
3
```

### Explanation

The longest common subsequence is:

```text
"ace"
```

Therefore, its length is:

```text
3
```

### Example 2

```text
Input:
text1 = "abc"
text2 = "abc"

Output:
3
```

Both strings are the same, so the longest common subsequence is `"abc"`.

---

## Approach – 2D Dynamic Programming

The solution uses a **2D DP matrix** to compare characters from both strings.

We create:

```python
dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
```

The extra row and column represent the case where one of the strings is empty.

Each position represents:

```text
dp[i][j] = length of the longest common subsequence
           between text1[i:] and text2[j:]
```

We build the matrix from **bottom-right to top-left** because each state depends on values to its right or below.

---

## Solution

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
```

---

## Case 1 – Characters Match

If:

```python
text1[i] == text2[j]
```

we found a character that can be included in the common subsequence.

Therefore:

```python
dp[i][j] = 1 + dp[i + 1][j + 1]
```

The `1` represents the matching character.

We then move forward in **both strings**.

For example:

```text
text1 = "abc"
         ↑

text2 = "adc"
         ↑
```

Both characters are:

```text
a == a
```

So we count `a`:

```text
1 + LCS of "bc" and "dc"
```

---

## Case 2 – Characters Do Not Match

If:

```python
text1[i] != text2[j]
```

we cannot include both characters in the common subsequence.

Therefore, we try two possibilities.

### Skip a character from `text1`

```python
dp[i + 1][j]
```

### Skip a character from `text2`

```python
dp[i][j + 1]
```

Since we want the **longest** common subsequence, we take:

```python
dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
```

---

## Example

Consider:

```text
text1 = "abcde"
text2 = "ace"
```

We compare characters from both strings.

The matching characters are:

```text
text1: a b c d e
       ↑   ↑   ↑

text2: a   c   e
       ↑   ↑   ↑
```

This gives the subsequence:

```text
"ace"
```

with length:

```text
3
```

Therefore:

```text
dp[0][0] = 3
```

---

## Why Use Dynamic Programming?

A brute-force approach would try many different subsequences from both strings.

For example, when two characters do not match, we have two choices:

```text
             (i, j)
             /    \
            /      \
       (i+1, j)   (i, j+1)
```

This creates many repeated subproblems.

Dynamic Programming solves each `(i, j)` state once and stores the result in:

```text
dp[i][j]
```

This avoids recalculating the same problems.

---

## DP Recurrence

The entire solution can be summarized using two rules.

### Characters Match

```text
if text1[i] == text2[j]:

    dp[i][j] = 1 + dp[i + 1][j + 1]
```

### Characters Do Not Match

```text
else:

    dp[i][j] = max(
        dp[i + 1][j],
        dp[i][j + 1]
    )
```

These two cases form the core of the Longest Common Subsequence algorithm.

---

## Why the Extra Row and Column?

The DP matrix is created using:

```python
len(text1) + 1
len(text2) + 1
```

The extra row and column represent an **empty string**.

The longest common subsequence between any string and an empty string is:

```text
0
```

For example:

```text
LCS("abc", "") = 0
LCS("", "ace") = 0
```

These zero values provide the base cases needed when calculating the rest of the matrix.

---

## Subsequence vs Substring

A **substring** must contain consecutive characters.

A **subsequence** does not.

For example:

```text
text = "abcde"
```

`"bcd"` is a substring because the characters are consecutive.

```text
b → c → d
```

`"ace"` is a subsequence because the characters remain in order, even though some characters are skipped.

```text
a → c → e
```

This distinction is important for understanding the problem.

---

## Complexity Analysis

Let:

```text
m = len(text1)
n = len(text2)
```

### Time Complexity

```text
O(m × n)
```

Every combination of positions from `text1` and `text2` is processed once.

### Space Complexity

```text
O(m × n)
```

A 2D DP matrix of size:

```text
(m + 1) × (n + 1)
```

is used to store the results.
