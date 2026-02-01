# 1. Quantile & Percentile

## Why they exist

**Problem with mean/median:**
They give only *one point*. They don’t tell **how data is spread**.

Quantiles split data into **equal parts**.

---

## Definitions (Math)

### Quantile

The value below which a **given fraction** of data lies.

$$
Q_p = \text{value at proportion } p
$$

Examples:


* $$( Q_{0.25} ) → 1st quartile$$
* $$( Q_{0.50} ) → median$$
* $$( Q_{0.75} ) → 3rd quartile$$

---

### Percentile

Same idea, but in **percentage**.

$$
P_k = Q_{k/100}
$$

---

## Simple Real-World Example

Marks of students:

```
[30, 40, 50, 60, 70, 80, 90]
```

* 50th percentile = 60
  → 50% students scored ≤ 60

---

## Advanced Real-World Example

Salary distribution in a company:

* 90th percentile salary = ₹1,20,000
  → Top 10% earn **more than this**

Used in:

* salary benchmarking
* performance cutoffs

---

## Python Code

```python
import numpy as np

data = np.array([30, 40, 50, 60, 70, 80, 90])

np.quantile(data, 0.25)   # Q1
np.quantile(data, 0.5)    # Median
np.percentile(data, 90)   # 90th percentile
```

---

# 2. Five Number Summary

## Why it exists

Raw data hides:

* outliers
* spread
* skewness

Five-number summary gives **full picture**.

---

## Definition

$$
\text{Five Number Summary} = { \min, Q_1, \text{median}, Q_3, \max }
$$

---

## Example

Data:

```
[10, 20, 30, 40, 100]
```

| Statistic | Value |
| --------- | ----- |
| Min       | 10    |
| Q1        | 20    |
| Median    | 30    |
| Q3        | 40    |
| Max       | 100   |

Outlier clearly visible.

---

## Python Code

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40, 100])
s.describe()
```

---

# 3. Box Plot

## Why it exists

Tables don’t show:

* outliers
* skewness
* spread visually

Box plot solves this.

---

## Box Plot Structure

* Box → Q1 to Q3
* Line inside → Median
* Whiskers → non-outlier range
* Dots → outliers

---

## Python Code (Single Box Plot)

```python
import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 100]
plt.boxplot(data)
plt.show()
```

---

## Side-by-Side Box Plot (Comparison)

### Real World

Compare **salary across departments**.

```python
dept_A = [30, 40, 50, 60]
dept_B = [25, 35, 45, 100]

plt.boxplot([dept_A, dept_B], labels=['A', 'B'])
plt.show()
```

---

# 4. Scatter Plot

## Why it exists

To see **relationship** between two numerical variables.

---

## Example

Height vs Weight.

```python
x = [150, 160, 170, 180]
y = [50, 60, 70, 80]

plt.scatter(x, y)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
```

---

# 5. Covariance

## Why it exists

We want to know **how two variables move together**.

---

## Formula (LaTeX)

$$
\text{Cov}(X,Y) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
$$

---

## Meaning Table

| Covariance | Meaning            |
| ---------- | ------------------ |
| +ve        | Move together      |
| −ve        | Move opposite      |
| 0          | No linear relation |

---

## Simple Example

| X (Hours) | Y (Marks) |
| --------- | --------- |
| 1         | 40        |
| 2         | 50        |
| 3         | 60        |

Covariance → **positive**

---

## Python Code

```python
import numpy as np

x = [1, 2, 3]
y = [40, 50, 60]

np.cov(x, y)
```

---

## Limitation of Covariance

* Units depend on data
* Cannot compare datasets

→ leads to **correlation**

---

# 6. Correlation

## Why it exists

Standardized measure of relationship.

---

## Formula (Pearson)

$$
\rho = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

---

## Strength Table

| Correlation | Interpretation   |
| ----------- | ---------------- |
| +1          | Perfect positive |
| 0.7         | Strong           |
| 0.3         | Weak             |
| 0           | No relation      |
| −0.7        | Strong negative  |
| −1          | Perfect negative |

---

## Python Code

```python
np.corrcoef(x, y)
```

---

# 7. Correlation vs Causation (VERY IMPORTANT)

## Why confusion happens

Correlation only means **association**, not cause.

---

## Real Example

* Ice cream sales ↑
* Road accidents ↑

Correlation exists
❌ Ice cream does NOT cause accidents
✔ Summer causes both

---

## Data Science Rule

> Correlation is a **signal**, not proof.

Need:

* experiments
* domain logic
* controlled variables

---

## Final Mental Model 🧠

* Quantile → position
* Box plot → distribution
* Scatter → relationship
* Covariance → direction
* Correlation → strength
* Causation → real impact
