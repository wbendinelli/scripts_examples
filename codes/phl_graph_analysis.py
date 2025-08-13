"""Visualize post-harvest loss data.

This module is intentionally split into three functions so each step can be
copied independently for teaching purposes.
Data source: https://www.sciencedirect.com/science/article/pii/S235255091930123X
"""

from __future__ import annotations

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# --- Part 1: Load ---------------------------------------------------------
def load_data(path: str) -> pd.DataFrame:
    """Load the CSV dataset containing post-harvest loss information."""
    return pd.read_csv(path)


# --- Part 2: Prepare ------------------------------------------------------
def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Compute auxiliary columns used in the visualization."""
    df = df.copy()
    df["log_income"] = np.log(df["income"])
    return df


# --- Part 3: Plot ---------------------------------------------------------
def plot_and_save(df: pd.DataFrame, output_path: str) -> None:
    """Create scatter/regression plot and save it to a file."""
    sns.set(rc={"figure.figsize": (20, 15)})
    sns.set_style("whitegrid", {"axes.grid": True})

    fig, ax = plt.subplots()

    sns.regplot(x="log_income", y="phl", data=df, x_estimator=np.mean, ax=ax)
    sns.scatterplot(
        x="log_income",
        y="phl",
        hue="income_group",
        size="country_gdp",
        sizes=(40, 600),
        legend="brief",
        data=df,
        ax=ax,
    )

    sns.despine(left=True, bottom=True)
    ax.set_title(
        "Average food loss of grains (2000-2011) versus gross domestic per capita (2011)",
        fontsize=20,
    )
    ax.set_ylabel("Average post-harvest loss (in percentage)", fontsize=16)
    ax.set_xlabel("Natural logarithm of countries GDP per capita", fontsize=16)

    for line in range(df.shape[0]):
        ax.text(
            df.log_income[line] + 0.05,
            df.phl[line] - 0.05,
            df.country_name[line],
            horizontalalignment="left",
            size="medium",
            color="black",
        )

    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), ncol=1, title="Legend")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Saved visualization to {output_path}")


def main() -> None:
    """Run the full analysis from loading to plotting."""
    data = load_data("data/graph_post_harvest_loss.csv")
    data = prepare_data(data)
    plot_and_save(data, "phl_scatter.png")


if __name__ == "__main__":
    main()
