import os
from os.path import exists

from glob import glob
import shutil
import yfinance as yf # type: ignore
import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import NaN

def delete_data_dir():
    for match in glob('*data'):
       shutil.rmtree(match)


def download_data(
        tickers: list[str], 
        period: str, 
        interval: str
    ) -> dict[str, DataFrame]:
    data = yf.download( # type: ignore
      tickers = tickers,
      period=period,
      interval=interval,
      group_by = 'ticker'
      )
    
    return {tickers[0]: data} if len(tickers) == 1 else data # type: ignore


def use_existing_data(
        data_dir: str, 
        tickers: list[str],
        date: str) -> dict[str, DataFrame]:
    '''
    Use this if dir for today's data exists.
    Read the data into a dictionary of dataframes.
    Return the dictionary.
    '''
    multi_df = {}

    for ticker in tickers:
        filepath = f"{data_dir}/{date}_{ticker}.csv"
        
        if exists(filepath):
            df = pd.read_csv(filepath, index_col=['Date'], parse_dates=['Date']) # type: ignore
            multi_df[ticker] = df

            print(f"Using existing data for {ticker}.")

    return multi_df # type: ignore


def prep_and_save_stock_data(
      dfs: dict[str, DataFrame], 
      tickers: list[str], 
      data_dir: str, 
      date: str,
      ma_and_std_window: int) -> dict[str, DataFrame]:
    '''
    Calculates some features and adds them to dataframe for each ticker and saves them to csv.
    '''
    new_multi_df: dict[str, DataFrame] = {}

    for ticker in tickers:
        df = dfs[ticker][['Close']]
        df['Close Rolling Mean'] = df.Close.rolling(ma_and_std_window).mean() # type: ignore
        df['Close STD'] = df.Close.rolling(ma_and_std_window).std() # type: ignore

        df['1 STD Below Mean (Val)'] = df['Close Rolling Mean'] - df['Close STD']
        df['1 STD Below Mean (Bool)'] = df['Close'] < df['1 STD Below Mean (Val)']
        
        df['2 STD Below Mean'] = df['Close Rolling Mean'] - 2 * df['Close STD']
        df['2 STD Below Mean (Close)'] = np.where(df['Close'] < df['2 STD Below Mean'], df['Close'], NaN) # type: ignore
        
        df.to_csv(f"{data_dir}/{ticker}.csv")

        new_multi_df[ticker] = df

    return new_multi_df


def get_stock_data(
        tickers: list[str],
        period: str,
        interval: str,
        ma_and_std_window: int,
        date: str,
        data_dir: str,) -> dict[str, DataFrame]:
    if exists(data_dir):
        print("Today's data exists. Reusing it.")
        return use_existing_data(data_dir, tickers, date)
    else:
        print("Today's data not found in data dir. Getting new data.")
        os.makedirs(data_dir, exist_ok=True)
        multi_df = download_data(tickers, period, interval)
        return prep_and_save_stock_data(
            multi_df, tickers, data_dir, date, ma_and_std_window)