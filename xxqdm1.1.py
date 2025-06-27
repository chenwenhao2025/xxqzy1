# 1. 导入库及读取数据
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统黑体
plt.rcParams['axes.unicode_minus'] = False    # 修复负号显示

df = pd.read_csv("nigerian-songs.csv")  # 以pandas库的read_csv函数读取csv文件
df.head()  # 查看前5行数据

# 2. 数据基本信息和缺失值统计
df.info()
df.isnull().sum()