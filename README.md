# Combinatorial Testing Demo (ACC + PWC + Pytest)

This demo shows how to:

1. Generate **all combinations (ACC)** using `itertools`
2. Generate **pairwise combinations (PWC)** using `allpairspy`
3. Store test cases in a **CSV file**
4. Manually define the **expected outputs (oracle)**
5. Execute tests using **pytest**

---

## Problem

We test the function:

```python
shipping_fee(total_band, premium, international)
```
## Step 1: Generate test inputs

### Part 1: All Combinations Coverage (ACC)
```python
python shipping_fee_acc_testgen.py
```
### Part 2: Pairwise Coverage (PWC)
```python
python shipping_fee_pwc_testgen.py
```

## Step 2: Complete the oracle

Fill the expected column manually using the specification.

⚠️ Important ⚠️ the expected results must come from the specification
not from another implementation

## Step 3: Run tests with pytest
```python
python test_main.py
```