import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df_cleaned = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_cleaned.index, df_cleaned["value"], label="Page Views", color="red")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.legend(loc="upper left")
    plt.grid(True)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    plt.show()  # This will display the plot in the notebook
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df_cleaned.copy()
    df_bar["year"] = df_cleaned.index.year
    df_bar["month"] = df_cleaned.index.strftime("%B")

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.barplot(x="year", y="value", hue="month", data=df_bar, ci=None, palette="viridis")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(title="Months", loc="upper left", bbox_to_anchor=(1, 1))
    plt.title("Average Daily Page Views for Each Month Grouped by Year")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    plt.show()  # This will display the plot in the notebook
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    
    # Ensure the index is a datetime object
    df_box['date'] = pd.to_datetime(df_box['date'])
    
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=[
        "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    
    plt.show()  # This will display the plot in the notebook
    return fig


# Example usage
draw_line_plot()
draw_bar_plot()
draw_box_plot()
