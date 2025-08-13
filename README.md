# Post-Harvest Loss DataViz Lesson

This repository contains a small data visualization exercise using the
`graph_post_harvest_loss.csv` dataset (converted from the original Excel file).
The script in `codes/phl_graph_analysis.py` is split into three clear parts so
each step can be copied separately: load the data, prepare new columns and plot
the relationship between income and post-harvest loss.

The data is sourced from the article available at:
https://www.sciencedirect.com/science/article/pii/S235255091930123X

## Getting started

1. Install the required libraries:
   ```bash
   pip install pandas numpy seaborn matplotlib
   ```
2. Run the visualization script:
   ```bash
   python codes/phl_graph_analysis.py
   ```
3. The plot will be saved to `phl_scatter.png` in the repository root.

The core usage in Python looks like:
```python
from codes.phl_graph_analysis import load_data, prepare_data, plot_and_save

df = load_data("data/graph_post_harvest_loss.csv")
df = prepare_data(df)
plot_and_save(df, "phl_scatter.png")
```

Feel free to modify the script to experiment with different visualizations
and learn more about data visualization techniques with Python.
