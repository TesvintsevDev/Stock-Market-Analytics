#Get Stocks RU

import investpy
import numpy as np
from datetime import date
import time

stocks = investpy.stocks.get_stocks(country='russia')['symbol']

def array_to_string(a):
    string_stock = '['
    for i in range(len(a)):
        string_stock += a[i]
        if i != len(a) - 1:
            string_stock += ' , '
    string_stock += ']'
    return string_stock


counter = 0
index = 1
good_stocks = []
current_date = str(date.today().day) + '/' + str(date.today().month) + '/' + str(date.today().year)
a = date.today().month
if a == 1:
    from_date = str(date.today().day) + '/' + str(12) + '/' + str(date.today().year - 1)
else:
    from_date = str(date.today().day) + '/' + str(date.today().month - 1) + '/' + str(date.today().year)
for stock in stocks:
    if counter == 10:
        time.sleep(10)
        counter = 0
    try:
        df = investpy.get_stock_historical_data(stock=stock, country='russia', from_date=from_date,
                                                to_date=current_date)
        time.sleep(5)
        technical_indicators = investpy.technical.technical_indicators(stock, 'russia', 'stock', interval='daily')
        country = 'russia'
    except:
        continue
    tech_sell = len(technical_indicators[technical_indicators['signal'] == 'sell'])
    tech_buy = len(technical_indicators[technical_indicators['signal'] == 'buy'])

    time.sleep(2)
    moving_averages = investpy.technical.moving_averages(stock, country, 'stock', interval='daily')
    moving_sma_sell = len(moving_averages[moving_averages['sma_signal'] == 'sell'])
    moving_sma_buy = len(moving_averages[moving_averages['sma_signal'] == 'buy'])

    moving_ema_sell = len(moving_averages[moving_averages['ema_signal'] == 'sell'])
    moving_ema_buy = len(moving_averages[moving_averages['ema_signal'] == 'buy'])
    if tech_buy < 9 or tech_sell > 2 or moving_sma_buy < 5 or moving_ema_buy < 5:
        continue
    sma_20 = moving_averages['sma_signal'][2]
    sma_100 = moving_averages['sma_signal'][4]
    ema_20 = moving_averages['ema_signal'][2]
    ema_100 = moving_averages['ema_signal'][4]
    print(str(index) + ') ' + 'STOCK =', stock)
    print('Tech sell indicators: to buy =', tech_buy, 'of 12; ', 'to sell =', tech_sell, 'of 12')
    print('SMA moving averages: to buy =', moving_sma_buy, 'of 6; ', 'to sell =', moving_sma_sell, 'of 6')
    print('EMA moving averages: to buy =', moving_ema_buy, 'of 6; ', 'to sell =', moving_ema_sell, 'of 6')
    print('SMA_20 =', sma_20, ';', 'SMA_100 =', sma_100, ';', 'EMA_20 =', ema_20, ';', 'EMA_100 =', ema_100)
    print('Prices Last Five days of ' + stock + ' =', np.array(df['Close'][-5:][0]), ';', np.array(df['Close'][-5:][1]),
          ';', np.array(df['Close'][-5:][2]), ';', np.array(df['Close'][-5:][3]), ';', np.array(df['Close'][-5:][4]))
    p_1 = abs(1 - df['Close'][-5:][1] / df['Close'][-5:][0])
    if df['Close'][-5:][1] >= df['Close'][-5:][0]:
        pp_1 = '+' + str(round(p_1 * 100, 2)) + '%'
    else:
        pp_1 = '-' + str(round(p_1 * 100, 2)) + '%'
    p_2 = abs(1 - df['Close'][-5:][2] / df['Close'][-5:][1])
    if df['Close'][-5:][2] >= df['Close'][-5:][1]:
        pp_2 = '+' + str(round(p_2 * 100, 2)) + '%'
    else:
        pp_2 = '-' + str(round(p_2 * 100, 2)) + '%'
    p_3 = abs(1 - df['Close'][-5:][3] / df['Close'][-5:][2])
    if df['Close'][-5:][3] >= df['Close'][-5:][2]:
        pp_3 = '+' + str(round(p_3 * 100, 2)) + '%'
    else:
        pp_3 = '-' + str(round(p_3 * 100, 2)) + '%'
    p_4 = abs(1 - df['Close'][-5:][4] / df['Close'][-5:][3])
    if df['Close'][-5:][4] >= df['Close'][-5:][3]:
        pp_4 = '+' + str(round(p_4 * 100, 2)) + '%'
    else:
        pp_4 = '-' + str(round(p_4 * 100, 2)) + '%'
    print('Percentage +/- of ' + stock + ' =', pp_1, ';', pp_2, ';', pp_3, ';', pp_4, )
    print()
    index += 1
    counter += 1
    good_stocks.append(stock)
    time.sleep(2)

print('==================================================')

df = investpy.get_currency_cross_historical_data(currency_cross='USD/RUB', from_date=from_date, to_date=current_date)

print('Prices Last Five days of USD/RUB =', np.array(df['Close'][-5:][0]), ';', np.array(df['Close'][-5:][1]),
      ';', np.array(df['Close'][-5:][2]), ';', np.array(df['Close'][-5:][3]), ';', np.array(df['Close'][-5:][4]))
p_1 = abs(1 - df['Close'][-5:][1] / df['Close'][-5:][0])
if df['Close'][-5:][1] >= df['Close'][-5:][0]:
    pp_1 = '+' + str(round(p_1 * 100, 2)) + '%'
else:
    pp_1 = '-' + str(round(p_1 * 100, 2)) + '%'
p_2 = abs(1 - df['Close'][-5:][2] / df['Close'][-5:][1])
if df['Close'][-5:][2] >= df['Close'][-5:][1]:
    pp_2 = '+' + str(round(p_2 * 100, 2)) + '%'
else:
    pp_2 = '-' + str(round(p_2 * 100, 2)) + '%'
p_3 = abs(1 - df['Close'][-5:][3] / df['Close'][-5:][2])
if df['Close'][-5:][3] >= df['Close'][-5:][2]:
    pp_3 = '+' + str(round(p_3 * 100, 2)) + '%'
else:
    pp_3 = '-' + str(round(p_3 * 100, 2)) + '%'
p_4 = abs(1 - df['Close'][-5:][4] / df['Close'][-5:][3])
if df['Close'][-5:][4] >= df['Close'][-5:][3]:
    pp_4 = '+' + str(round(p_4 * 100, 2)) + '%'
else:
    pp_4 = '-' + str(round(p_4 * 100, 2)) + '%'
print('Percentage +/- of USD/RUB =', pp_1, ';', pp_2, ';', pp_3, ';', pp_4, )

