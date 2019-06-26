import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
style.use('ggplot')

df = pd.read_csv(r'Datasets\tsla.csv', parse_dates=True, index_col=0)

# min_periods - для того чтобы перыве 100 значений не были нулами
# первые сто значений каждое следующее значение берется средним из предыдущих
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# ohlc - open high low close for stock information
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

# сделаем индексацию по строкам, а даты превратим обратно в колонку
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
# печатает уродливые даты в формате матплотлиба в красивом формате
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values,
                 width=2,
                 colorup='g',
                 colordown='r')
ax2.fill_between(df_volume.index.map(mdates.date2num),
                 df_volume.values,
                 0,
                 facecolor='b',
                 alpha=0.5)



plt.show()
