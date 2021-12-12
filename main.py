def get_font_family():

    import platform
    system_name = platform.system()

    if system_name == "Darwin":
        font_family = "AppleGothic"
    elif system_name == "Windows":
        font_family = "Malgun Gothic"
    else:
        pass

        import matplotlib.font_manager as fm

        fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
        font = fm.FontProperties(fname=fontpath, size=9)
        fm._rebuild()
        font_family = "NanumBarunGothic"

    return font_family

import pandas as pd
import FinanceDataReader as fdr
from pybithumb import Bithumb
import matplotlib.pyplot as plt


font_family = get_font_family()
plt.rc("font", family=font_family)
plt.rcParams['axes.unicode_minus'] = False
path = 'C://Users/82105/Desktop/open_sw_final/'

# 최대 수익률
def print_maxprofit(data, column, event):
    print(f"근 5년 중 가장 저점에서 사서 가장 고점에서 팔았을 경우 {event}의 수익률은 : ", ((data[column].max()/data[column].min())-1)*100, "% 입니다.")

# 안전성
def print_safety(data, column, event):
	count = 0
	for n in range(data.shape[0] - 1):
		if data[column][n] < data[column][n + 1]:
			count += 1
	print(f"{event}가 상승한 날은 전체", data.shape[0], "일 중에", count, "일 이다.")
	print("따라서", (count / data.shape[0]) * 100, "%의 확률로 투자 수익을 낼 수 있다.\n")

land_price = pd.read_csv(path + "지역별지가변동률.csv")

land_price.rename(columns={'Unnamed: 0':'날짜'}, inplace=True)
land_price = land_price.query('"2016-03-01"<=날짜<="2021-03-31"')
land_price.set_index('날짜', drop=True, inplace=True)

l_count = 0
for n in range(land_price.shape[0]-1):
    for m in range(1, land_price.shape[1]):
        if land_price.iloc[n, m]>0:
            l_count += 1
print("땅값이 상승한 달은 전체", land_price.shape[0]*land_price.shape[1], "개월 중에", l_count, "개월 이다.")
print("따라서", (l_count/(land_price.shape[0]*land_price.shape[1]))*100, "%의 확률로 투자 수익을 낼 수 있다.\n")


land_price_list = []

for lp in land_price.columns.tolist():
    temp = lp.replace('%','호')
    land_price_list.append(temp)

land_price.shape

# 땅값 상승률 시각화
land_price.plot(title='땅값 상승률 시각화')



kospi = fdr.DataReader('KS11', '2016-03-01', '2021-03-31')
dow = fdr.DataReader('DJI', '2016-03-01', '2021-03-31')
hongkong = fdr.DataReader('HSI', '2016-03-01', '2021-03-31')
ftse = fdr.DataReader('FTSE', '2016-03-01', '2021-03-31')
nikkei = fdr.DataReader('JP225', '2016-03-01', '2021-03-31')

# 코스피 시각화
kospi[['Close', 'Open', 'High', 'Low', 'Volume']].plot(title='코스피 시각화', secondary_y='Volume')
# 다우지수 시각화
dow[['Close', 'Open', 'High', 'Low', 'Volume']].plot(title='다우지수 시각화', secondary_y='Volume')
# 홍콩 시각화
hongkong[['Close', 'Open', 'High', 'Low', 'Volume']].plot(title='홍콩지수 시각화', secondary_y='Volume')
# 영국FTSE 시각화
ftse[['Close', 'Open', 'High', 'Low', 'Volume']].plot(title='영국FTSE 시각화', secondary_y='Volume')
# 닛케이 시각화
nikkei[['Close', 'Open', 'High', 'Low', 'Volume']].plot(title='닛케이 시각화', secondary_y='Volume')

print_maxprofit(kospi, 'Close', '코스피지수')
print_safety(kospi, 'Close', '코스피')

print_maxprofit(dow, 'Close', '다우지수')
print_safety(dow, 'Close', '다우지수')

print_maxprofit(hongkong, 'Close', '홍콩지수')
print_safety(hongkong, 'Close', '홍콩지수')

print_maxprofit(ftse, 'Close', '영국FTSE')
print_safety(ftse, 'Close', '영국 FTSE')

print_maxprofit(nikkei, 'Close', '닛케이')
print_safety(nikkei, 'Close', '닛케이 지수')

#2016.03 ~ 2021.03
btc = Bithumb.get_candlestick("BTC")
eth = Bithumb.get_candlestick("ETH")
xrp = Bithumb.get_candlestick("XRP")

btc = btc.query('"2016-03-01"<= time <="2021-03-31"')
eth = eth.query('"2016-03-01"<= time <="2021-03-31"')
xrp = xrp.query('"2016-03-01"<= time <="2021-03-31"')

# 비트코인 시각화
btc.plot(title='비트코인 시각화', secondary_y="volume")
# 이더리움 시각화
eth.plot(title='이더리움 시각화', secondary_y="volume")
# 리플 시각화
xrp.plot(title='리플 시각화', secondary_y="volume")

print_maxprofit(btc, 'close', '비트코인')
print_safety(btc, 'close', '비트코인')

print_maxprofit(eth, 'close', '이더리움')
print_safety(eth, 'close', '이더리움')

print_maxprofit(xrp, 'close', '리플')
print_safety(xrp, 'close', '리플')

plt.show()