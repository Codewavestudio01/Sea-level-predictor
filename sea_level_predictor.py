import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def load_data(csv_path: str = "epa-sea-level.csv") -> pd.DataFrame:
    """
    Load the sea level dataset from CSV.
    Uses float_precision='legacy' to mitigate floating point discrepancies.
    Returns a DataFrame with columns including 'Year' and 'CSIRO Adjusted Sea Level'.
    """
    # Using float_precision='legacy' helps with test float consistency in some environments
    df = pd.read_csv(csv_path, float_precision="legacy")
    return df

def draw_plot() -> plt.Axes:
    """
    Produces the scatter + regression plot, saves it to 'sea_level_plot.png'.
    Returns the Axes object (so tests can inspect).
    """
    df = load_data()
    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")

    # First regression: full range
    slope, intercept, r, p, stderr = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    # Create x-values from min Year to 2050
    x_full = np.arange(df["Year"].min(), 2051)
    y_full = intercept + slope * x_full
    ax.plot(x_full, y_full, "r", label="Fit: all data")

    # Second regression: from year 2000
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, r2, p2, stderr2 = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    x2 = np.arange(2000, 2051)
    y2 = intercept2 + slope2 * x2
    ax.plot(x2, y2, "g", label="Fit: from 2000")

    # Labels & title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save and return
    fig.savefig("sea_level_plot.png")
    return ax
