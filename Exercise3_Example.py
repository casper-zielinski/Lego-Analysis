import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

lego['Year_Range'] = pd.cut(lego['Year'], 
                            bins=[1940, 1980, 2000, 2010, 2020, 2030],
                            labels=['1940-1980', '1980-2000', '2000-2010', '2010-2020', '2020+'])

pairpl = sns.PairGrid(data=lego[["USD_MSRP", "Minifigures", "Pieces", "Year_Range"]], hue="Year_Range", palette="plasma", height=3)
pairpl.map_diag(sns.histplot)
pairpl.map_offdiag(sns.scatterplot)
pairpl.add_legend(title="year")
plt.show()

''''
Example of Pairplot
Diagonal is variable with itself (useless in scatterplot, useful with histogram)
You can see if they are left-skewed, normal or right-skewed, meaning whether most sets are cheap vs. expensive, or small and large
'''