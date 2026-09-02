# Reverse Bits

## Problem

Given a **32-bit unsigned integer** `n`, reverse its binary bits and return the resulting integer.

### Example

```text
Input:
00000010100101000001111010011100

Reversed:
00111001011110000010100101000000

Output:
964176192
```

The goal is to take every bit from its original position and place it in the corresponding reversed position.

---

## Approach – Bit Manipulation

Since the input is a **32-bit integer**, we process exactly 32 bits.

We create a result variable:

```python
res = 0
```

Then, for every bit position `i`, we:

1. Extract the bit at position `i`.
2. Move that bit to its reversed position.
3. Add the bit to the result using bitwise OR.

---

## Solution

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
```

---

## Step 1 – Extract the Current Bit

To get the bit at position `i`, we use:

```python
bit = (n >> i) & 1
```

First:

```python
n >> i
```

shifts the desired bit to the rightmost position.

Then:

```python
& 1
```

extracts only that bit.

For example:

```text
n = 10110
```

If:

```text
i = 2
```

then:

```text
10110 >> 2 = 00101
```

Now:

```text
  00101
& 00001
-------
  00001
```

Therefore:

```text
bit = 1
```

So the expression:

```python
(n >> i) & 1
```

can be remembered as:

> Get the bit at position `i`.

---

## Step 2 – Find the Reversed Position

The bit positions of a 32-bit integer range from:

```text
0 to 31
```

When reversing the bits:

```text
Original Position    Reversed Position

0                    31
1                    30
2                    29
3                    28
...                  ...
30                   1
31                   0
```

Therefore, the reversed position can be calculated using:

```python
31 - i
```

---

## Step 3 – Move the Bit

Once the current bit has been extracted, we shift it to its reversed position:

```python
bit << (31 - i)
```

For example, the bit at position `0` moves to:

```text
31 - 0 = 31
```

The bit at position `1` moves to:

```text
31 - 1 = 30
```

And so on.

---

## Step 4 – Add the Bit to the Result

We use the bitwise OR operator:

```python
res = res | (bit << (31 - i))
```

The `|` operator allows us to set the appropriate bit in `res` without affecting the bits that have already been added.

For example:

```text
Current result:
10000000

New bit:
00100000

OR:
  10000000
| 00100000
----------
  10100000
```

This allows the reversed number to be built one bit at a time.

---

## Simplified Example

Consider a smaller **4-bit number**:

```text
n = 1101
```

Reversing it gives:

```text
1101 → 1011
```

The original bit positions are:

```text
Position:   3  2  1  0
            ↓  ↓  ↓  ↓
Bits:       1  1  0  1
```

When reversed:

```text
Position 0 → Position 3
Position 1 → Position 2
Position 2 → Position 1
Position 3 → Position 0
```

The result becomes:

```text
1011
```

The 32-bit solution performs exactly the same process, but across all 32 positions.

---

## Important Bit Operations

### Right Shift

```python
n >> i
```

Moves the bits to the right so the desired bit reaches the rightmost position.

### Bitwise AND

```python
(n >> i) & 1
```

Extracts the rightmost bit.

### Left Shift

```python
bit << (31 - i)
```

Moves the extracted bit to its reversed position.

### Bitwise OR

```python
res | shifted_bit
```

Places the shifted bit into the result.

---

## Complexity Analysis

### Time Complexity

```text
O(1)
```

The algorithm always performs exactly **32 iterations**, regardless of the input value.

Since 32 is a fixed constant, the time complexity is `O(1)`.

More generally, for an integer containing `b` bits, the complexity would be `O(b)`.

### Space Complexity

```text
O(1)
```

Only a few variables are used, and no additional data structures are required.
