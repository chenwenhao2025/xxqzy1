# 第一次作业：关于尼日利亚音乐数据集的K-means聚类分析


## 1.数据集简介

|列名|说明|
|---|---|
|name|歌曲名称|
|album|专辑名称|
|artist|歌手|
|artist_top_genre|音乐风格|
|release_date|发行日期|
|length|时长|
|popularity|流行度|
|danceability|可跳舞性|
|acousticness|原声感|
|energy|能量感|
|instrumentalness|乐器感/纯乐器度|
|liveness|现场感|
|loudness|响度|
|speechiness| 口语化程度|
|tempo|曲速|
|time_signature|节拍|


## 2. 数据基本信息和缺失值统计
df.info()
df.isnull().sum()
![屏幕截图 2025-06-27 214250](https://github.com/user-attachments/assets/b541c80f-8811-47fe-b532-0c809bbc7624)
![屏幕截图 2025-06-27 214356](https://github.com/user-attachments/assets/1d3c4ad5-0eb2-44d9-b326-3d0a186eaab3)


## 3. 探索性可视化分析
# 数值特征分布
![image](https://github.com/user-attachments/assets/40537a92-65d7-4d19-8a00-9ba7e23ab6a1)

# 流行度与音乐特征的关系
![image](https://github.com/user-attachments/assets/3c4c5553-f44e-4d35-98d6-18cd0a6be6fe)

# 音乐风格分析
![image](https://github.com/user-attachments/assets/688d8bf1-10e8-49b0-8c34-b7c08b34eb75)

# 查看不同数值型特征的箱型图分布
![image](https://github.com/user-attachments/assets/0e8d18ec-a7f0-4ee5-a2b1-51c8f32178e6)


# 获取歌曲数量最多的前20位歌手
![image](https://github.com/user-attachments/assets/88966956-ff99-4ba4-b73c-e3f6c4eb8727)

# 创建饼图展示顶级歌手占比（前10名）
![image](https://github.com/user-attachments/assets/9dbd3f57-b1c4-43a7-be81-0c186347dbf5)


# 肘部法则图和轮廓系数图
![image](https://github.com/user-attachments/assets/193afdde-76b1-43d7-a610-5e69d8d4c862)


# 特征分析 - 聚类中心分析
![image](https://github.com/user-attachments/assets/5e43ccd0-d2bf-4696-86ff-ac1d89b452c1)

# PCA降维与可视化
![image](https://github.com/user-attachments/assets/ba0b462c-6367-4cb9-ac06-ac7c53f9a8c0)

# 可视化特征贡献度
![image](https://github.com/user-attachments/assets/31fdb9ac-72e5-49a5-92e2-fa617ec25b75)


# 聚类结果分析
![屏幕截图 2025-06-27 215024](https://github.com/user-attachments/assets/d1ce0976-37f9-40ec-8a4e-3028b73ce03c)

# 可视化聚类特征
![image](https://github.com/user-attachments/assets/d750df85-00f8-43da-a4a0-8be24f0be494)


