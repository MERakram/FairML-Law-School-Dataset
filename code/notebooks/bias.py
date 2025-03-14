import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os


def visualize_law_school_bias():
    """
    Loads the Law School dataset and visualizes bias in bar exam passage rates by race.
    Uses a custom teal color palette for consistent presentation aesthetics.
    """
    # Define the custom color palette
    custom_palette = ["#b2d8d8", "#66b2b2", "#008080", "#006666", "#004c4c"]

    # Set visual style and apply custom colors
    sns.set_style("whitegrid")
    plt.rcParams.update(
        {
            "font.size": 12,
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "figure.titlesize": 16,
        }
    )

    # Create results directory if it doesn't exist
    os.makedirs("../results", exist_ok=True)

    # Load the dataset
    print("Loading Law School dataset...")
    try:
        df = pd.read_csv("../../data/law_school_clean.csv")
        print(
            f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns"
        )
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Print column names for reference
    print("\nColumns in the dataset:", df.columns.tolist())

    # Check if needed columns exist
    required_cols = ["race", "pass_bar"]
    if not all(col in df.columns for col in required_cols):
        print(f"Error: Dataset missing required columns: {required_cols}")
        return

    # Map race values for better readability if needed
    if df["race"].dtype == "object":
        print("Race is already a string category")
    else:
        # If race is encoded as numbers, map back to labels
        df["race_label"] = df["race"].map({1: "White", 0: "Non-White"})

    # Use the appropriate column name
    race_col = "race_label" if "race_label" in df.columns else "race"

    # Calculate pass rates by race
    pass_rates = df.groupby(race_col)["pass_bar"].mean().reset_index()
    pass_rates["pass_rate_pct"] = pass_rates["pass_bar"] * 100

    print("\nBar Exam Pass Rates by Race:")
    print(pass_rates)

    # Create figure with multiple visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle(
        "Bias Analysis in Law School Bar Exam Passage Rates",
        fontsize=20,
        color=custom_palette[3],
    )

    # 1. Bar chart of pass rates by race
    ax1 = axes[0, 0]
    bars = ax1.bar(
        pass_rates[race_col],
        pass_rates["pass_rate_pct"],
        color=[custom_palette[1], custom_palette[3]],
    )
    ax1.set_title("Bar Exam Pass Rate by Race", color=custom_palette[4])
    ax1.set_ylabel("Pass Rate (%)", color=custom_palette[3])
    ax1.set_xlabel("Race", color=custom_palette[3])
    ax1.spines["bottom"].set_color(custom_palette[0])
    ax1.spines["top"].set_color(custom_palette[0])
    ax1.spines["left"].set_color(custom_palette[0])
    ax1.spines["right"].set_color(custom_palette[0])
    ax1.tick_params(colors=custom_palette[3])

    # Add text labels to the bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 1,
            f"{height:.1f}%",
            ha="center",
            va="bottom",
            color=custom_palette[4],
            fontweight="bold",
        )

    # 2. Count of students by race with pass/fail breakdown
    ax2 = axes[0, 1]
    pass_fail_counts = pd.crosstab(df[race_col], df["pass_bar"])
    pass_fail_counts.columns = ["Fail", "Pass"]  # Assuming 0=Fail, 1=Pass
    pass_fail_counts.plot(
        kind="bar", stacked=True, ax=ax2, color=[custom_palette[0], custom_palette[3]]
    )
    ax2.set_title("Pass/Fail Distribution by Race", color=custom_palette[4])
    ax2.set_ylabel("Number of Students", color=custom_palette[3])
    ax2.set_xlabel("Race", color=custom_palette[3])
    ax2.legend(title="Bar Exam Result", facecolor="white", edgecolor=custom_palette[1])
    ax2.spines["bottom"].set_color(custom_palette[0])
    ax2.spines["top"].set_color(custom_palette[0])
    ax2.spines["left"].set_color(custom_palette[0])
    ax2.spines["right"].set_color(custom_palette[0])
    ax2.tick_params(colors=custom_palette[3])

    # 3. Pie chart showing racial composition of students who passed
    ax3 = axes[1, 0]
    passed_by_race = df[df["pass_bar"] == 1][race_col].value_counts()
    wedges, texts, autotexts = ax3.pie(
        passed_by_race,
        labels=passed_by_race.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=[custom_palette[3], custom_palette[1]],
    )
    for text in texts:
        text.set_color(custom_palette[4])
    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")
    ax3.set_title("Racial Composition of Students Who Passed", color=custom_palette[4])
    ax3.axis("equal")

    # 4. Statistical disparity visualization
    ax4 = axes[1, 1]
    # Calculate statistical parity difference manually
    white_pass_rate = (
        pass_rates.loc[pass_rates[race_col] == "White", "pass_bar"].values[0]
        if "White" in pass_rates[race_col].values
        else None
    )
    nonwhite_pass_rate = (
        pass_rates.loc[pass_rates[race_col] == "Non-White", "pass_bar"].values[0]
        if "Non-White" in pass_rates[race_col].values
        else None
    )

    # If we have both rates, calculate disparity
    if white_pass_rate is not None and nonwhite_pass_rate is not None:
        # Statistical Parity Difference
        spd = white_pass_rate - nonwhite_pass_rate

        # Disparate Impact
        di = (
            nonwhite_pass_rate / white_pass_rate
            if white_pass_rate > 0
            else float("nan")
        )

        metrics = pd.DataFrame(
            [
                {
                    "Metric": "Statistical Parity\nDifference",
                    "Value": spd,
                    "Fair Value": 0,
                },
                {"Metric": "Disparate\nImpact", "Value": di, "Fair Value": 1},
            ]
        )

        bar_positions = np.arange(len(metrics))
        bar_width = 0.35

        ax4.bar(
            bar_positions,
            metrics["Value"],
            bar_width,
            label="Actual",
            color=custom_palette[2],
        )
        ax4.bar(
            bar_positions + bar_width,
            metrics["Fair Value"],
            bar_width,
            label="Fair Value",
            color=custom_palette[0],
        )
        ax4.set_xticks(bar_positions + bar_width / 2)
        ax4.set_xticklabels(metrics["Metric"], color=custom_palette[4])
        ax4.set_title(
            "Fairness Metrics: Actual vs. Fair Values", color=custom_palette[4]
        )
        ax4.axhline(y=0, color=custom_palette[0], linestyle="-", alpha=0.7)
        ax4.legend(facecolor="white", edgecolor=custom_palette[1])
        ax4.spines["bottom"].set_color(custom_palette[0])
        ax4.spines["top"].set_color(custom_palette[0])
        ax4.spines["left"].set_color(custom_palette[0])
        ax4.spines["right"].set_color(custom_palette[0])
        ax4.tick_params(colors=custom_palette[3])

        # Add text annotations
        ax4.text(
            0,
            spd / 2,
            f"{spd:.3f}",
            ha="center",
            va="bottom",
            color="white",
            fontweight="bold",
        )
        ax4.text(
            1 + bar_width,
            1,
            f"Fair: 1.0",
            ha="center",
            va="bottom",
            color=custom_palette[4],
        )
        ax4.text(
            bar_width,
            0,
            f"Fair: 0.0",
            ha="center",
            va="bottom",
            color=custom_palette[4],
        )
        ax4.text(
            1,
            di / 2,
            f"{di:.3f}",
            ha="center",
            va="bottom",
            color="white",
            fontweight="bold",
        )
    else:
        ax4.text(
            0.5,
            0.5,
            "Cannot calculate disparity metrics with available data",
            ha="center",
            va="center",
            transform=ax4.transAxes,
            color=custom_palette[4],
        )

    # Add an explanation text box
    fig.text(
        0.5,
        0.01,
        "Statistical Parity Difference: Difference in probability of positive outcome between groups (0 = fair)\n"
        "Disparate Impact: Ratio of favorable outcomes between unprivileged and privileged groups (1.0 = fair)",
        ha="center",
        va="bottom",
        color=custom_palette[4],
        fontsize=11,
        bbox=dict(facecolor=custom_palette[0], alpha=0.2, edgecolor=custom_palette[2]),
    )

    # Adjust layout and save
    plt.tight_layout()
    plt.subplots_adjust(top=0.92, bottom=0.08)

    # Save the visualization with the custom color scheme
    plt.savefig(
        "../visualizations/bias_visualization.png", dpi=300, bbox_inches="tight"
    )

    print(
        "\nVisualization complete. Saved to '../visualizations/bias_visualization.png'"
    )
    plt.show()


if __name__ == "__main__":
    visualize_law_school_bias()
