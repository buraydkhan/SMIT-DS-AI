pip install matplotlib numpy

# ==============================================================================
# MATPLOTLIB BASICS CRASH COURSE
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np

# Apply a clean default style (optional, but looks great)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# ------------------------------------------------------------------------------
# 1. BASIC LINE PLOT (Functional API)
# ------------------------------------------------------------------------------
print("=== 1. BASIC LINE PLOT ===")

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="blue", linestyle="--", linewidth=2, label="Sin(x)")

plt.title("Basic Sine Wave", fontsize=14)
plt.xlabel("X Axis (Time)")
plt.ylabel("Y Axis (Amplitude)")
plt.legend(loc="upper right")
plt.grid(True)

print("Displaying Line Plot... (Close plot window to continue)")
plt.show()
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. SCATTER PLOT & BAR CHART
# ------------------------------------------------------------------------------
print("\n=== 2. SCATTER PLOT & BAR CHART ===")

# Figure with 2 Subplots side-by-side using Object-Oriented API
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Subplot 1: Scatter Plot
np.random.seed(42)
x_scatter = np.random.rand(30)
y_scatter = np.random.rand(30)
colors = np.random.rand(30)
sizes = 1000 * np.random.rand(30)

ax1.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap="viridis")
ax1.set_title("Scatter Plot (Variable Sizes & Colors)")
ax1.set_xlabel("Feature X")
ax1.set_ylabel("Feature Y")

# Subplot 2: Bar Chart
categories = ["Apples", "Bananas", "Cherries", "Dates"]
values = [40, 25, 60, 15]

ax2.bar(categories, values, color=["red", "yellow", "darkred", "brown"])
ax2.set_title("Category Values")
ax2.set_ylabel("Quantity")

plt.tight_layout()  # Automatically adjusts subplot parameters to prevent overlapping
print("Displaying Scatter & Bar Plots... (Close plot window to continue)")
plt.show()
print("-" * 50)


# ------------------------------------------------------------------------------
# 3. HISTOGRAM & BOX PLOT (Distribution Visualizations)
# ------------------------------------------------------------------------------
print("\n=== 3. HISTOGRAM & BOX PLOT ===")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Subplot 1: Histogram
data = np.random.normal(loc=100, scale=15, size=1000)  # Normal distribution

ax1.hist(data, bins=30, color="teal", edgecolor="black", alpha=0.7)
ax1.set_title("Histogram (Distribution of Data)")
ax1.set_xlabel("Value Range")
ax1.set_ylabel("Frequency")

# Subplot 2: Box Plot (Outliers & Quartiles)
data_group1 = np.random.normal(100, 10, 200)
data_group2 = np.random.normal(80, 20, 200)

ax2.boxplot([data_group1, data_group2], tick_labels=["Group A", "Group B"])
ax2.set_title("Box Plot (Comparing Distributions)")
ax2.set_ylabel("Values")

plt.tight_layout()
print("Displaying Histogram & Box Plot... (Close plot window to continue)")
plt.show()
print("-" * 50)


# ------------------------------------------------------------------------------
# 4. MULTIPLE LINES & ANNOTATIONS
# ------------------------------------------------------------------------------
print("\n=== 4. MULTIPLE LINES & ANNOTATIONS ===")

x = np.linspace(0, 10, 100)

plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label="Sin(x)", color="navy")
plt.plot(x, np.cos(x), label="Cos(x)", color="darkorange", linestyle=":")

# Annotate a specific point on the graph
plt.annotate(
    "Peak of Sin(x)", 
    xy=(np.pi/2, 1.0), 
    xytext=(np.pi/2 + 1, 1.2),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6)
)

plt.ylim(-1.5, 1.5)
plt.title("Trigonometric Functions with Annotation")
plt.legend()

print("Displaying Annotated Plot... (Close plot window to continue)")
plt.show()
print("-" * 50)


# ------------------------------------------------------------------------------
# 5. SAVING PLOTS TO DISK
# ------------------------------------------------------------------------------
print("\n=== 5. SAVING PLOTS ===")

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker="o", color="green")
ax.set_title("Saved Plot Example")

# Save as PNG image (dpi specifies image quality)
output_filename = "my_first_plot.png"
plt.savefig(output_filename, dpi=300, bbox_inches="tight")
plt.close(fig)  # Close the plot figure without displaying it

print(f"Successfully saved image as '{output_filename}' in your working directory!")

print("-" * 50)
print("\n=== ALL MATPLOTLIB CODE EXECUTED SUCCESSFULLY! ===")
