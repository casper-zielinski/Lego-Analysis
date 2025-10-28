# Lego Dataset Analysis

This project contains data analysis and visualization exercises using a LEGO sets dataset. The analysis explores relationships between various LEGO set attributes such as price, number of pieces, minifigures, packaging types, and release years.

## Dataset

The `legosets.csv` file contains information about LEGO sets including:
- Item_Number: Unique identifier for each set
- Name: Set name
- Year: Release year
- Theme & Subtheme: Product categories
- Pieces: Number of pieces in the set
- Minifigures: Number of minifigures included
- Pricing: USD_MSRP, GBP_MSRP, CAD_MSRP, EUR_MSRP
- Packaging: Type of packaging
- Availability: Retail availability status

## Exercise Questions

The analysis addresses the following questions using appropriate visualizations:

1. **Has the number of minifigures included in the set increased each year?**
   - Does your observation hold for the median as well?
   - Are there outliers?

2. **How does the price in USD relate to the number of minifigures?**
   - What do the marginal distributions look like?

3. **Consider the Pairplot:**
   - What can you do to adjust the diagonal plots?
   - Play around with it and try to use different methods!

4. **Does the variable Packaging have an influence on the number of figures or pieces?**
   - Consider the five most common packaging types excluding the unknown type.

## Files

### Exercise2.py
Analyzes the relationship between price and number of minifigures.

**Key Features:**
- Calculates correlation between Minifigures and USD_MSRP
- Creates a joint plot showing:
  - Scatter plot of Price vs Minifigures
  - Marginal distributions (histograms) for both variables
- Displays basic statistics

**Key Findings:**
- Correlation: 0.514 (moderate positive correlation)
- Most LEGO sets contain 0-5 minifigures
- Most sets are priced between 0-50 USD
- Both distributions are right-skewed (long tail towards higher values)

### Exercise3.py
Creates a pairplot to explore relationships between multiple variables.

**Key Features:**
- Analyzes multiple variables: USD_MSRP, Minifigures, Pieces, Year_Range
- Uses color-coding (hue) based on Year_Range
- Shows diagonal plots with histograms
- Shows off-diagonal plots with scatter plots

**Visualization:**
- PairGrid with custom diagonal (histplot) and off-diagonal (scatterplot) mappings
- Plasma color palette for year ranges

## Requirements

```
pandas
matplotlib
seaborn
```

Install dependencies:
```bash
pip install pandas matplotlib seaborn
```

## Usage

Run each exercise file individually:

```bash
python Exercise2.py
```

```bash
python Exercise3.py
```

Each script will display the corresponding visualizations in separate windows.

## Analysis Insights

### Price vs Minifigures (Exercise 2)
- There is a moderate positive correlation (0.514) between the number of minifigures and price
- The relationship is not perfectly linear, suggesting other factors influence pricing
- Both variables show right-skewed distributions, indicating most sets are at the lower end with some premium outliers

### Multivariate Relationships (Exercise 3)
- The pairplot allows exploration of relationships between four key variables
- Year_Range coloring helps identify temporal trends
- Diagonal histograms show the distribution of each individual variable
- Off-diagonal scatter plots reveal pairwise relationships

## Notes

- The dataset contains some NA values which are handled by dropping them in the analysis
- Visualizations use Seaborn's built-in styling for consistent and professional appearance
- Color palettes (steelblue, coral, plasma) are chosen for clear visual distinction