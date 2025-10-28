import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

fig, axes = plt.subplots(2,2, figsize=(20,6))

sns.lineplot(data=lego, x='Year', y='Minifigures', ax=axes[0,0], errorbar=None)
sns.scatterplot(data=lego[["Year","Minifigures"]].groupby('Year').mean()["Minifigures"], color='red', ax=axes[0,0])
axes[0,0].set_xlabel("Year")
axes[0,0].set_ylabel("Minifigures")
axes[0,0].set_title("Minifigures / year")
axes[0,0].tick_params(axis='x', labelsize=8)

sns.scatterplot(data=lego, x='Year', y='USD_MSRP', ax=axes[0,1])
axes[0,1].set_xlabel("Year")
axes[0,1].set_ylabel("Minifigures")
axes[0,1].set_title("Minifigures / year")

top5_packaging = lego['Packaging'].value_counts().head(5).index
lego_pack = lego[lego['Packaging'].isin(top5_packaging)]

sns.boxplot(data=lego, x='Packaging', y='Minifigures', ax=axes[1, 0])
axes[1, 0].set_title("Minifigures by Packaging Type (Top 5)")
axes[1, 0].set_xlabel("Packaging Type")
axes[1, 0].set_ylabel("Number of Minifigures")
axes[1, 0].tick_params(axis='x', rotation=20)
axes[1, 0].tick_params(axis='x', rotation=20, labelsize=7)

sns.boxplot(data=lego, x='Packaging', y='Pieces', ax=axes[1, 1])
axes[1, 1].set_title("Pieces by Packaging Type (Top 5)")
axes[1, 1].set_xlabel("Packaging Type")
axes[1, 1].set_ylabel("Number of Pieces")
axes[1, 1].tick_params(axis='x', rotation=20)
axes[1, 1].tick_params(axis='x', rotation=20, labelsize=7)

plt.tight_layout()
plt.show()

''''
Exercise 1 (Top Left): Lineplot with red scatter points showing yearly mean
Shows whether minifigures per set increased over time, identifies outliers above the trend line

Exercise 4 (Bottom Row): Boxplots comparing top 5 packaging types
Left plot shows minifigures distribution, right plot shows pieces distribution
The box shows median (center line) and quartiles (box edges), outliers appear as individual points
This reveals if packaging type influences the size and complexity of LEGO sets
'''



