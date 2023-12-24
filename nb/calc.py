import yfinance as yf # type: ignore
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.dates as mdates

import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')

my_year_month_fmt = mdates.DateFormatter('%m/%y')


def calc_line_params(
        df: DataFrame
    ) -> tuple[float, float, list[float]]:
    '''Returns coeff, intercept, and fitted line values.'''

    x = df.index # type: ignore
    y = df['Close'] # type: ignore

    # Create sequence of integers from 0 to x.size to use in np.polyfit()
    x_seq = np.arange(x.size)

    fit = np.polyfit(x_seq, y, 1) # type: ignore
    coeff = fit[0]
    intercept = fit[1]

    fitted_line = coeff * x_seq + intercept
    # df["Fitted"] = fitted_line

    return coeff, intercept, fitted_line


def get_target_tickers(
        dfs: dict[str, DataFrame]
    ) -> dict[str, DataFrame]:
    '''
    We might want to buy these tickers
    '''
    suitable: dict[str, DataFrame] = {}
    
    for ticker, df in dfs.items():
        coeff, intercept, fitted_line = calc_line_params(df)

        # Rising trend over longer period
        if coeff > 0:
            latest_df = yf.download(
                tickers=ticker,
                period="1d",
                interval="1m",
            )

            latest_coeff, latest_intercept, latest_fitted_line = calc_line_params(latest_df)

            # Falling trend over last 24 hours
            if latest_coeff < 0:
                # print(f'{ticker}, Slope: {coeff}, Intercept: {intercept}')
                df["Fitted"] = fitted_line
                suitable[ticker] = df
        
    return suitable


def plot_ticker(ticker: str, period: str, ma_and_std_window: int, df: DataFrame):
    fig, ax = plt.subplots(figsize=(16,9))

    ax.plot(df.index, df.Close, label='Close price', color='skyblue')
    ax.plot(df.index, df['Close Rolling Mean'], label = f'{ma_and_std_window}-day MA', color='lightgrey')
    ax.plot(df.index, df['2 STD Below Mean (Close)'], label = f'2 STD below Mean', color='red')
    ax.plot(df.index, df.Fitted, label='Fitted', color='orange')

    ax.legend(loc='best')
    ax.set_ylabel('Price in $')
    ax.set_title(f'{ticker}, {period}')
    ax.xaxis.set_major_formatter(my_year_month_fmt)

    
def visualise_dataframes(dfs: dict[str, DataFrame], period: str, ma_and_std_window: int):
    for ticker, df in dfs.items():
        plot_ticker(ticker, period, ma_and_std_window, df)