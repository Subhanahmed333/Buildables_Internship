import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, color='blue', s=20)

    # Create first line of best fit using all data
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create x values from first year in dataset to 2050
    years_extended = np.arange(df['Year'].min(), 2051)
    line_all = slope_all * years_extended + intercept_all
    ax.plot(years_extended, line_all, 'red', linewidth=2, label='Best fit line (1880-2013)')

    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create x values from 2000 to 2050
    years_recent_extended = np.arange(2000, 2051)
    line_recent = slope_recent * years_recent_extended + intercept_recent
    ax.plot(years_recent_extended, line_recent, 'green', linewidth=2, label='Best fit line (2000-2013)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Set reasonable axis limits
    ax.set_xlim(df['Year'].min(), 2050)
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT CHANGE)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
