"""
Matplotlib Basics - Beginner Examples
-------------------------------------
This file contains simple examples of different types of plots using Matplotlib.
"""

import matplotlib.pyplot as plt

# 1. Basic Line Plot
def basic_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y, label="y = 2x", color="blue", marker="o")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Basic Line Plot")
    plt.legend()
    plt.show()

# 2. Scatter Plot
def scatter_plot():
    x = [5, 7, 8, 7, 6, 9, 5, 6, 7, 8]
    y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

    plt.scatter(x, y, color="red", marker="x")
    plt.title("Scatter Plot Example")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

# 3. Bar Chart
def bar_chart():
    categories = ["Apples", "Bananas", "Cherries", "Dates"]
    values = [10, 15, 7, 12]

    plt.bar(categories, values, color="green")
    plt.title("Fruit Count")
    plt.xlabel("Fruits")
    plt.ylabel("Quantity")
    plt.show()

# 4. Histogram
def histogram_example():
    data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

    plt.hist(data, bins=5, color="orange", edgecolor="black")
    plt.title("Histogram Example")
    plt.xlabel("Value Ranges")
    plt.ylabel("Frequency")
    plt.show()

# 5. Multiple Plots (Subplots)
def multiple_plots():
    x = [1, 2, 3, 4, 5]
    y1 = [i for i in x]
    y2 = [i**2 for i in x]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(x, y1, marker="o")
    axs[0].set_title("Linear Plot")

    axs[1].plot(x, y2, marker="s", color="red")
    axs[1].set_title("Quadratic Plot")

    plt.show()

# Run all examples one by one
if __name__ == "__main__":
    basic_line_plot()
    scatter_plot()
    bar_chart()
    histogram_example()
    multiple_plots()
