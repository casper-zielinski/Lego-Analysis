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

# Beispiel von Paiplot 
# Diagonale ist Variable mit sich selbst (in Scatterplot nutzlos, mit Histogram nützlich)
# man kann sehen ob sie linksschief,normal oder rechtsschief ist, also ob die meisten Sets günstig vs. teuer sind, oder klein und groß