import pandas as pd #data reading, writing, manipulating....
import matplotlib.pyplot as plt #basic plotting library
import seaborn as sns #basic plotting library

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

fig, axes = plt.subplots(2,2, figsize=(15,5))

sns.lineplot(data=lego, x='Year', y='Minifigures', ax=axes[0,0], errorbar=None)
sns.scatterplot(data=lego[["Year","Minifigures"]].groupby('Year').mean()["Minifigures"], color='red', ax=axes[0,0])
axes[0,0].set_xlabel("Year")
axes[0,0].set_ylabel("Minifigures")
axes[0,0].set_title("Minifigures / year")

sns.scatterplot(data=lego, x='Year', y='USD_MSRP', ax=axes[0,1])
axes[0,1].set_xlabel("Year")
axes[0,1].set_ylabel("Minifigures")
axes[0,1].set_title("Minifigures / year")



top5_packaging = lego['Packaging'].value_counts().head(5).index
lego_pack = lego[lego['Packaging'].isin(top5_packaging)]

# Plot 1: Packaging vs Minifigures
sns.boxplot(data=lego, x='Packaging', y='Minifigures', ax=axes[1, 0])
axes[1, 0].set_title("Minifigures by Packaging Type (Top 5)")
axes[1, 0].set_xlabel("Packaging Type")
axes[1, 0].set_ylabel("Number of Minifigures")
axes[1, 0].tick_params(axis='x', rotation=20)

# Plot 2: Packaging vs Pieces
sns.boxplot(data=lego, x='Packaging', y='Pieces', ax=axes[1, 1])
axes[1, 1].set_title("Pieces by Packaging Type (Top 5)")
axes[1, 1].set_xlabel("Packaging Type")
axes[1, 1].set_ylabel("Number of Pieces")
axes[1, 1].tick_params(axis='x', rotation=20)

plt.tight_layout()
plt.show()



