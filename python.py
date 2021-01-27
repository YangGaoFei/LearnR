import numpy as np
import pandas as pd
import statsmodels.api as sm  # 统计运算
import scipy.stats as scs  # 科学计算
import matplotlib.pyplot as plt  # 绘图
# 更新方式 pip install -U jqdatasdk   每两周更新一次
import jqdatasdk as jd
jd.auth('18742071003', '121106229.ygf')

# 输出沪深300指数信息
jd.get_security_info("000300.XSHG")

hs_300 = jd.get_price('000300.XSHG',
                      start_date='2018-09-27',
                      end_date='2019-07-26',
                      frequency='daily',
                      fields=None,
                      skip_paused=False,
                      fq='pre')
hs_300.head()

stock_set = ['000413.XSHE','000063.XSHE','002007.XSHE','000001.XSHE','000002.XSHE']
noa = len(stock_set)
df = jd.get_price(stock_set, start_date = '2015-01-01', end_date ='2015-12-31', 
               frequency='daily', fields=['close'])
data = df['close']
#规范化后时序数据
data.describe()
(data/data.ix[0]*100).plot(figsize = (8,5))


%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn
from IPython.display import display, clear_output
import time
x = np.linspace(0,5)
f, ax = plt.subplots()
ax.set_title("Bessel functions")
for n in range(1,10):
   time.sleep(1)
   ax.plot(x, jn(x,n))
   clear_output(wait=True)
   display(f)    
plt.close()

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style = 'whitegrid')

diamonds = sns.load_dataset('diamonds')

f, ax = plt.subplots(figsize = (6.5, 6.5))
sns.despine(f, left = True, bottom = True)
clarity_ranking = [
  "I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"
]

sns.scatterplot(x = "carat", y = "price",
hue = "clarity", size = "depth",
palette = "ch:r=-.2,d=.3_r",
hue_order = clarity_ranking,
sizes = (1, 8), linewidth=0,
data=diamonds, ax=ax)  
                      
plt.show()                      
                      
                      
