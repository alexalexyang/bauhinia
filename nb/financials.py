import yahooquery as yq # type: ignore
from yahooquery import Ticker # type: ignore

from pandas import DataFrame

def earnings_info(ticker: str):
    data = yq.Ticker(ticker)
    return data

def get_all_earnings_info(dfs: dict[str, DataFrame]) -> list[Ticker]:
    '''
    Takes a list of tickers as strings and returns a list of YQ ticker objects
    '''
    info_list: list[Ticker] = []

    for ticker, _ in dfs.items():
        info = earnings_info(ticker)
        info_list.append(info)

    return info_list

def show_earnings_info(target_tickers: list[Ticker]):
    '''
    Takes a list of YQ ticker objects
    '''
    for ticker in target_tickers:
        display(ticker.recommendation_trend[:1])