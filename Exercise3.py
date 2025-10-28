import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

lego = pd.read_csv(filepath_or_buffer="legosets.csv")

pairpl = sns.PairGrid(data=lego[["USD_MSRP", "Minifigures", "Pieces", "Availability"]], hue="Availability", palette="viridis", height=3)
pairpl.map_diag(sns.histplot)
pairpl.map_offdiag(sns.scatterplot)
pairpl.add_legend(title="Availability")
plt.show()