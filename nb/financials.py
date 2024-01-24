import yahooquery as yq # type: ignore
from yahooquery import Ticker # type: ignore
import yfinance as yf # type: ignore
from pandas import DataFrame


def get_all_earnings_info(dfs: dict[str, DataFrame]) -> list[dict[str, Ticker | dict[str, int]]]:
    '''
    Takes a list of tickers as strings and returns a list of YQ ticker objects
    '''
    info_list: list[dict[str, Ticker | dict[str, int]]] = []

    for ticker, _ in dfs.items():
        yf_ticker = yf.Ticker(ticker)
        info = yf_ticker.info

        info_list.append({
            "yq": yq.Ticker(ticker),
            "yf": {
                "symbol": info.get("symbol", "NA"),
                "trailingPE": info.get("trailingPE", "NA"),
                "forwardPE": info.get("forwardPE", "NA"),
                "pegRatio": info.get("pegRatio", "NA"),
                "trailingPegRatio": info.get("trailingPegRatio", "NA"),
                "beta": info.get("beta", "NA"),
                }
        })

    return info_list

def show_earnings_info(info_list: list[dict[str, Ticker | dict[str, int]]]):
    '''
    Takes a list of YQ ticker objects
    '''
    for info in info_list:
        display(info["yq"].recommendation_trend[:1])

        for key, value in info["yf"].items():
            print(f"{key}: {value}")
        
        info["yq"].calendar_events