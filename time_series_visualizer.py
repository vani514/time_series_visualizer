import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import and clean data
df = pd.read_csv("/home/rguktongole/Downloads/fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# 2. Clean data (remove top & bottom 2.5%)
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= lower) & (df['value'] <= upper)]


def draw_line_plot():
    # Ensure index is datetime and data is copied cleanly
    df_line = df_clean.copy()
    df_line.index = pd.to_datetime(df_line.index)

    # Explicitly convert index and values to numpy arrays for compatibility
    x = df_line.index.to_numpy()
    y = df_line['value'].to_numpy()

    # Now plot using clean numpy arrays
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(x, y, color='red', linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.tight_layout()
    return fig



def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')

    # Group and pivot
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Reorder months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped[month_order]

    # Plot
    fig = df_grouped.plot(kind='bar', figsize=(12, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Months')
    plt.tight_layout()
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    # Draw plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    # Year-wise boxplot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise boxplot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.tight_layout()
    return fig
