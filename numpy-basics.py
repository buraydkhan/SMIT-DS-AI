pip install numpy

# ==============================================================================
# NUMPY BASICS CRASH COURSE
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# 1. CREATING ARRAYS
# ------------------------------------------------------------------------------
print("=== 1. CREATING ARRAYS ===")

# 1D Array (Vector)
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

# 2D Array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# Common Array Creation Helpers
zeros = np.zeros((2, 3))             # 2x3 matrix filled with 0s
ones = np.ones((3, 2))               # 3x2 matrix filled with 1s
full = np.full((2, 2), 7)            # 2x2 matrix filled with 7s
eye = np.eye(3)                      # 3x3 Identity matrix (diagonal 1s)
arange_arr = np.arange(0, 10, 2)     # Like range(0, 10, 2) -> [0, 2, 4, 6, 8]
linspace_arr = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1

print("\nZeros (2x3):\n", zeros)
print("Arange (0 to 10 step 2):", arange_arr)
print("Linspace (0 to 1, 5 points):", linspace_arr)
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. ARRAY ATTRIBUTES
# ------------------------------------------------------------------------------
print("\n=== 2. ARRAY ATTRIBUTES ===")

matrix = np.array([[10, 20, 30], [40, 50, 60]])

print("Matrix:\n", matrix)
print("Shape (rows, cols):", matrix.shape)  # Output: (2, 3)
print("Dimensions (ndim):", matrix.ndim)    # Output: 2
print("Total Elements (size):", matrix.size)# Output: 6
print("Data Type (dtype):", matrix.dtype)   # e.g., int64 or int32
print("-" * 50)


# ------------------------------------------------------------------------------
# 3. INDEXING & SLICING
# ------------------------------------------------------------------------------
print("\n=== 3. INDEXING & SLICING ===")

grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Access single elements: grid[row, col]
print("Element at row 1, col 2:", grid[1, 2])  # Output: 60

# Slicing: grid[row_start:row_end, col_start:col_end]
print("First 2 rows, last 2 columns:\n", grid[0:2, 1:3])

# Boolean Masking / Filtering (Selecting elements based on condition)
numbers = np.array([12, 45, 7, 23, 89, 2])
greater_than_20 = numbers[numbers > 20]

print("\nNumbers > 20:", greater_than_20)  # Output: [45 23 89]
print("-" * 50)


# ------------------------------------------------------------------------------
# 4. ELEMENT-WISE OPERATIONS & BROADCASTING
# ------------------------------------------------------------------------------
print("\n=== 4. OPERATIONS & BROADCASTING ===")

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

# Element-wise math (No loops needed!)
print("x + y:", x + y)       # [11, 22, 33]
print("x * y:", x * y)       # [10, 40, 90]
print("x ** 2:", x ** 2)     # [1, 4, 9]

# Scalar Broadcasting (NumPy applies the scalar '10' to all elements)
print("x * 10:", x * 10)     # [10, 20, 30]
print("-" * 50)


# ------------------------------------------------------------------------------
# 5. AGGREGATIONS & AXES
# ------------------------------------------------------------------------------
print("\n=== 5. AGGREGATIONS & AXES ===")

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Global Sum:", data.sum())          # 21
print("Global Mean:", data.mean())        # 3.5
print("Global Max:", data.max())          # 6

# Axis Operations:
# axis=0 -> Perform operation down columns
# axis=1 -> Perform operation across rows
print("Sum across columns (axis=0):", data.sum(axis=0))  # [5, 7, 9]
print("Sum across rows (axis=1):", data.sum(axis=1))     # [6, 15]
print("-" * 50)


# ------------------------------------------------------------------------------
# 6. RESHAPING & FLATTENING
# ------------------------------------------------------------------------------
print("\n=== 6. RESHAPING & FLATTENING ===")

flat_arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape into 2x3 matrix
reshaped = flat_arr.reshape((2, 3))
print("Reshaped (2x3):\n", reshaped)

# Flatten matrix back into 1D array
flattened = reshaped.flatten()
print("Flattened back to 1D:", flattened)
print("-" * 50)


# ------------------------------------------------------------------------------
# 7. RANDOM NUMBER GENERATION
# ------------------------------------------------------------------------------
print("\n=== 7. RANDOM GENERATION ===")

# Set seed for reproducible results
np.random.seed(42)

# Random floats between 0 and 1
rand_floats = np.random.rand(3)

# Random integers between low (inclusive) and high (exclusive)
rand_ints = np.random.randint(1, 100, size=(2, 3))

print("Random Floats:", rand_floats)
print("Random Integers (2x3):\n", rand_ints)

print("-" * 50)
print("\n=== ALL NUMPY CODE EXECUTED SUCCESSFULLY! ===")
