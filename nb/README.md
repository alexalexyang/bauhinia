## How to use

- Get stock prices with `get_prices.ipynb`
- Select stocks with `select.ipynb`
- Analyse with `analyse.ipynb`

## Todo next

Currently, this app finds tickers where the trend is rising over 6 months but falling over the last 24 hours.

Maybe we should find prices 2 STDs below mean in the current moment.


## Install latest Python in venv

- Install latest Python (eg 3.11) on local machine
- `path/to/python3.11 -m venv myenv`
- Or, make any .py file and let the IDE detect the latest installed version before creating the venv

## Use the venv

On 23 Dec 2023 I installed Python 3.12 in Conda.

Activate: `conda activate 3.12`

Check version: `python --version`

Install requirements: `pip install -r requirements.txt`

## Jupyter lab

Start without opening browser: `jupyter lab --no-browser`


## References

[yfinance](https://pypi.org/project/yfinance/)

[JupyterLab](https://jupyterlab.readthedocs.io)