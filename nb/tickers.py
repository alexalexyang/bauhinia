# https://www.investopedia.com/top-energy-stocks-4582081
energy_most_momentum = ['AR', 'OXY', 'DVN', 'XLE']
energy_fast_growing = ['MRO', 'CTRA', 'COP']
energy_low_pe_0827 = ['APA', 'MRC', 'FANG']

# https://finance.yahoo.com/news/10-energy-stocks-buy-winter-230454016.html
yahoo_energy_picks = ['XOM', 'CVX', 'DVN', 'TTE', 'ENB', 'BP', 'CTRA', 'VLO', 'BP']

con_energy_tickers = list(set(
    yahoo_energy_picks + 
    energy_low_pe_0827 + 
    energy_fast_growing + 
    energy_most_momentum +
    ['RYDAF', 'EQNR', 'PBR']
))


alt_energy_eu = ['VWDRY', 'DNNGY', 'IBDRY']
# https://www.investopedia.com/investing/alternative-energy-stocks/ ++
alt_energy_others = ['JKS', 'TAC', 'DQ', 'CWEN', 'EE', 'AQN', 'ENPH', 'EVA', 'ORA', 'ICLN', 'NEE', 'BEP', 'BEPC', 'FSLR', 'SEDG', 'RUN', 'NOVA']
# https://seekingalpha.com/news/3841098-solar-clean-energy-stocks-surge-again-on-europes-planned-green-push
alt_energy_seeking_alpha = ['TAN', 'ENPH', 'SEDG', 'SHLS', 'MAXN', 'FTCI', 'SPWR', 'SOL', 'CSIQ', 'ARRY', 'JKS', 'NOVA', 'RUN', 'DQ', 'FSLR', 'BE', 'BLDP', 'GNRC', 'FCEL', 'PLUG', 'FAN', 'ICLN', 'QCLN', 'PBW', 'PBD', 'ACES', 'CNRG', 'SMOG', 'ERTH']


alt_energy_tickers = list(set(
    alt_energy_eu +
    alt_energy_others +
    alt_energy_seeking_alpha
))

# tickers = large_cap + mid_cap + small_cap
# tickers = sorted(con_energy_tickers)
picks = list(set(con_energy_tickers + alt_energy_tickers))

tickers = sorted(picks)
# tickers = ["AAPL", "MSFT"]

# large_cap = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values.tolist()[:5]
# mid_cap = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_400_companies')[0]['Ticker symbol'].values.tolist()[:5]
# small_cap = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_600_companies')[1]['Ticker symbol'].values.tolist()[:5]