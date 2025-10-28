import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

print("="*80)
print("AUFGABE 2: Price vs Minifigures with Marginal Distributions")
print("="*80)

#==============================================================================
# TEIL 1: Grundlegende Analyse
#==============================================================================

print("\n 1️⃣  Basic Statistics:")
print("-" * 50)

# Korrelation berechnen
correlation = lego[['Minifigures', 'USD_MSRP']].corr().iloc[0, 1]
print(f"Correlation between Minifigures and Price: {correlation:.3f}")

print("\nMinifigures Statistics:")
print(lego['Minifigures'].describe())

print("\nPrice (USD_MSRP) Statistics:")
print(lego['USD_MSRP'].describe())

#==============================================================================
# TEIL 2: Joint Plot - Die Hauptvisualisierung
#==============================================================================

print("\n2️⃣ Creating Joint Plot (Main Visualization)...")
print("-" * 50)

# Entferne NaN-Werte
lego_clean = lego[['Minifigures', 'USD_MSRP']].dropna()

# Erstelle Joint Plot mit Seaborn
g = sns.jointplot(data=lego_clean, 
                  x='Minifigures', 
                  y='USD_MSRP', 
                  kind='scatter',        # Hauptplot: Scatter
                  height=10,             # Größe
                  alpha=0.4,             # Transparenz
                  color='steelblue',     # Farbe
                  marginal_kws=dict(bins=40, fill=True, color='coral'))  # Marginal-Plots

g.set_axis_labels('Number of Minifigures', 'Price (USD)', fontsize=13)
g.fig.suptitle('Price vs Minifigures with Marginal Distributions', 
               fontsize=15, fontweight='bold', y=1.02)

# Füge Korrelation als Text hinzu
g.ax_joint.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
                transform=g.ax_joint.transAxes,
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.show()

# Die meisten Minifiguren haben wenige Minifigures (0 - 5) und sind billig (0 - 100$)
# Beide Marginal Distributions sind rechtsschief (right-skewed)
# Die Minifigures-Verteilung zeigt, dass die meisten Lego-Sets 0-5 Minifiguren enthalten, mit einem langen Schwanz zu höheren Werten
# Die Preis-Verteilung zeigt, dass die meisten Sets zwischen 0-50 USD kosten, ebenfalls mit einem langen Schwanz für teure Premium-Sets
# Correlation: 0.514
 