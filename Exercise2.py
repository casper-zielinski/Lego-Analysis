import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

print("="*80)
print("EXERCISE 2: Price vs Minifigures with Marginal Distributions")
print("="*80)

#==============================================================================
# PART 1: Basic Analysis
#==============================================================================

print("\n 1️⃣  Basic Statistics:")
print("-" * 50)

# Calculate correlation
correlation = lego[['Minifigures', 'USD_MSRP']].corr().iloc[0, 1]
print(f"Correlation between Minifigures and Price: {correlation:.3f}")

print("\nMinifigures Statistics:")
print(lego['Minifigures'].describe())

print("\nPrice (USD_MSRP) Statistics:")
print(lego['USD_MSRP'].describe())

#==============================================================================
# PART 2: Joint Plot - Main Visualization
#==============================================================================

print("\n2️⃣ Creating Joint Plot (Main Visualization)...")
print("-" * 50)

# Remove NaN values
lego_clean = lego[['Minifigures', 'USD_MSRP']].dropna()

# Create Joint Plot with Seaborn
g = sns.jointplot(data=lego_clean,
                  x='Minifigures',
                  y='USD_MSRP',
                  kind='scatter',        # Main plot: Scatter
                  height=7,              # Size
                  alpha=0.4,             # Transparency
                  color='steelblue',     # Color
                  marginal_kws=dict(bins=40, fill=True, color='coral'))

g.set_axis_labels('Number of Minifigures', 'Price (USD)', fontsize=13)
g.fig.suptitle('Price vs Minifigures with Marginal Distributions',
               fontsize=10, fontweight='bold', y=1.02)

# Add correlation as text
g.ax_joint.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
                transform=g.ax_joint.transAxes,
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.show()

# Most sets have few minifigures (0-5) and are cheap (0-100$)
# Both marginal distributions are right-skewed
# The minifigures distribution shows that most LEGO sets contain 0-5 minifigures, with a long tail towards higher values
# The price distribution shows that most sets cost between 0-50 USD, also with a long tail for expensive premium sets
# Correlation: 0.514
 