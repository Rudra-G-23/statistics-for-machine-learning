
```mermaid
    flowchart TD
    RV[Random Var] --> PD[Prob Dist]

    PD --> DRV[Disc RV]
    PD --> CRV[Cont RV]

    DRV --> PMF
    PMF --> CDF_D[CDF]

    CRV --> PDF
    PDF --> CDF_C[CDF]

    PDF --> DE[Density Est]
    DE --> PDE[Parametric DE]
    DE --> NPDE[Non-Parametric DE]
    NPDE --> KDE
    NPDE --> HE[histogram Estimation]
    NPDE --> GMM[Gaussian mixture models GMMs]
```


```mermaid
flowchart TB

    A[Variables] --> B[Algebraic Variables]
    A --> C[Random Variables]

    B --> B1[Fixed but Unknown Values]
    B1 --> B2[Used in Deterministic Equations]

    C --> C1[Discrete Random Variables]
    C --> C2[Continuous Random Variables]

    C --> D[Probability Distributions]

    D --> D1[Discrete Probability Distributions]
    D --> D2[Continuous Probability Distributions]

    D1 --> E[Probability Mass Function]
    E --> E1[Assigns Probability to Each Discrete Outcome]
    E --> E2[Sum of All Probabilities Equals One]

    E --> F[Cumulative Distribution Function for Discrete Random Variables]
    F --> F1[Probability that Random Variable is Less Than or Equal to a Value]

    D2 --> G[Probability Density Function]
    G --> G1[Describes Probability Density Over a Continuous Range]
    G --> G2[Area Under the Curve Equals One]

    G --> H[Cumulative Distribution Function for Continuous Random Variables]
    H --> H1[Integral of Probability Density Function from Minus Infinity to a Value]

    D --> I[Density Estimation]

    I --> I1[Parametric Density Estimation]
    I1 --> I1a[Assumes a Known Distribution Family]
    I1 --> I1b[Estimates Parameters Such as Mean and Variance]

    I --> I2[Non Parametric Density Estimation]
    I2 --> I2a[No Assumption About Distribution Shape]

    I2a --> J[Kernel Density Estimation]
    J --> J1[Uses Kernels to Smooth Data Points]
    J --> J2[Bandwidth Controls Smoothness]

    C --> K[Real World Applications]
    K --> K1[Risk Modeling]
    K --> K2[Prediction Systems]
    K --> K3[Machine Learning Models]
```

# 1. Variables (clear the confusion first)

## 1.1 Algebraic Variables

### What

A symbol representing a **fixed but unknown value**.

$$
x = 5,\quad y = 2x + 3
$$

### Why

Used in **equations**, not uncertainty.

### Example

If:

$$
x = 10
\Rightarrow y = 2(10) + 3 = 23
$$

👉 No randomness.

---

## 1.2 Random Variables (MOST IMPORTANT)

### What

A **function** that maps outcomes of a random experiment to numbers.


$$ X: \Omega \rightarrow \mathbb{R}$$

### Why needed

Real world is **uncertain**:

* dice
* stock prices
* rainfall
* clicks on ads

Random variable converts **uncertainty → numbers**.

---

### Example (Die 🎲)

Sample space:

$$ \Omega = {1,2,3,4,5,6} $$

Random variable:

$$
X = \text{number shown on die}
$$

---

## 1.3 Probability Variables ❌ (common mistake)

There is **no official concept** called *probability variable*.

Correct terms:

* **random variable**
* **probability distribution**

Probability is a **function**, not a variable.

---

# 2. Probability Distribution

## What

A rule that assigns **probability to values of a random variable**.

---

## Why we need it

**Problem without distribution:**

* Cannot quantify uncertainty
* Cannot compute expectation, risk, likelihood

**Distribution solves:**

* how likely each outcome is

---

## What it solves in data science

* model randomness
* build likelihoods
* estimate parameters
* train ML models

---

# 3. Types of Random Variables

## 3.1 Discrete Random Variable

### What

Takes **countable values**.

$$
X \in {x_1, x_2, x_3, \dots}
$$

### Examples

* die outcome
* number of customers
* number of defects

---

## 3.2 Continuous Random Variable

### What

Takes values from an **interval**.

$$
X \in [a,b]
$$

### Examples

* height
* time
* temperature

---

# 4. Probability Distribution Functions (Big Picture)

```mermaid
flowchart TD
A[Random Variable] --> B{Type?}
B -->|Discrete| C[PMF]
B -->|Continuous| D[PDF]
C --> E[CDF]
D --> F[CDF]
```

---

# 5. Probability Mass Function (PMF)

## What

Gives probability for **each discrete value**.

$$
P(X = x)
$$

---

## Why PMF exists

Discrete outcomes have **exact probabilities**.

---

## Die Example 🎲

### Outcomes (Set Format)

$$
\Omega = {1,2,3,4,5,6}
$$

Random variable:

$$
X = \text{die value}
$$

PMF:

$$
P(X = x) =
\begin{cases}
\frac{1}{6}, & x \in {1,2,3,4,5,6} \
0, & \text{otherwise}
\end{cases}
$$

---

### PMF Table

| x | P(X=x) |
| - | ------ |
| 1 | 1/6    |
| 2 | 1/6    |
| 3 | 1/6    |
| 4 | 1/6    |
| 5 | 1/6    |
| 6 | 1/6    |

---

### Python (PMF)

```python
import numpy as np

x = np.arange(1,7)
pmf = np.ones(6) / 6
```

---

# 6. CDF of PMF

## What

Probability that random variable is **≤ x**.

$$
F(x) = P(X \le x)
$$

---

## Die Example

[
F(3) = P(X \le 3) = \frac{3}{6} = 0.5
]

---

### CDF Table

| x | F(x) |
| - | ---- |
| 1 | 1/6  |
| 2 | 2/6  |
| 3 | 3/6  |
| 4 | 4/6  |
| 5 | 5/6  |
| 6 | 1    |

---

### Python (CDF)

```python
cdf = np.cumsum(pmf)
```

---

# 7. Probability Density Function (PDF)

## What

Describes **density** of probability for continuous variables.

$$
f(x)
$$

⚠️ Important:
$$
P(X = x) = 0
$$

Only **intervals** have probability.

---

## Why PDF exists

Continuous values are **infinite**, cannot assign exact probabilities.

---

## Example: Height

$$
P(170 \le X \le 175) = \int_{170}^{175} f(x),dx
$$

---

### Normal Distribution (Example PDF)

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

---

### Python (PDF)

```python
from scipy.stats import norm

x = np.linspace(150, 190, 100)
pdf = norm.pdf(x, loc=170, scale=10)
```

---

# 8. CDF of PDF

## Definition

$$
F(x) = P(X \le x) = \int_{-\infty}^{x} f(t),dt
$$

---

### Python

```python
cdf = norm.cdf(x, loc=170, scale=10)
```

---

# 9. Density Estimation

## What

Estimate unknown **PDF** from data.

---

## Why we need it

**Real problem:**

* we don’t know true distribution
* data comes from unknown process

Density estimation helps:

* anomaly detection
* clustering
* generative models

---

# 10. Types of Density Estimation

## 10.1 Parametric Density Estimation

### Idea

Assume a distribution family.

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

Estimate parameters:
$$
\hat{\mu}, \hat{\sigma}
$$

---

### Example

Assume heights are normal.

```python
mu_hat = np.mean(data)
sigma_hat = np.std(data)
```

---

## 10.2 Non-Parametric Density Estimation

### Why

Assumption may be wrong.

No fixed shape.

---

### Kernel Density Estimation (KDE)

$$
\hat{f}(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x - x_i}{h}\right)
$$

* (K) → kernel (Gaussian)
* (h) → bandwidth (smoothness)

---

### Python (KDE)

```python
from sklearn.neighbors import KernelDensity

kde = KernelDensity(kernel='gaussian', bandwidth=1.0)
kde.fit(data.reshape(-1,1))
```

---

# 11. Big Mental Map 🧠

```mermaid
flowchart LR
A[Random Variable] --> B[Distribution]
B --> C[PMF - Discrete]
B --> D[PDF - Continuous]
C --> E[CDF]
D --> F[CDF]
B --> G[Density Estimation]
G --> H[Parametric]
G --> I[KDE]
```

---

## Final Intuition (Data Science View)

* Random Variable → uncertainty in numbers
* PMF → exact probabilities
* PDF → probability density
* CDF → accumulation of probability
* Density Estimation → learn distribution from data

