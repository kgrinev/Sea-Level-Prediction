import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.scatter(x, y)
    
    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
    plt.plot(x.append(pd.Series([2050]), ignore_index=True), intercept+slope*x.append(pd.Series([2050]), ignore_index=True), '-g')
    
    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    x_2000 = df_2000["Year"]
    y_2000 = df_2000["CSIRO Adjusted Sea Level"]
    slope_2000, intercept_2000, rvalue_2000, pvalue_2000, stderr_2000 = linregress(x_2000, y_2000)
    plt.plot(x_2000.append(pd.Series([2050]), ignore_index=True), intercept_2000+slope_2000*x_2000.append(pd.Series([2050]), ignore_index=True), '-r')
    
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()