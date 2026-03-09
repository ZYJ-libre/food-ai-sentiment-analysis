# 基于电商背景的食品评论AI情感分析系统

**作者**：ZYJ（电商+计算机）  
**GitHub**：https://github.com/zyj-libre/food-ai-sentiment-analysis  
**项目时长**：零基础自学3天完成（已可直接用于27考研复试展示）

![食品差评词云图](食品差评词云图.png)

### 项目简介（导师最爱看这段）
本科大二从电商专业转计算机后，我深刻感受到**食品类商品差评**（过期、添加剂、口感差、假货）对店铺复购率和评分的影响极大。  
于是利用课余时间自学NLP，**独立开发**了这个垂直领域评论情感分析系统，可自动：
- 判断正面/负面情感比例
- 提取高频差评关键词（针对食品痛点）
- 生成词云可视化

**核心亮点**：真正把我的电商实战经验和AI结合（不是纯代码搬运），导师复试最爱这类“业务驱动型”项目！

### 运行效果（直接看图说话）
![食品差评词云图](食品差评词云图.png)

**控制台输出示例**：
- 正面评论：4 条
- 负面评论：4 条
- 高频差评关键词：['过期', '添加剂', '假货', '拉肚子']

### 核心功能
1. 情感分析（SnowNLP实现正负分类）
2. 差评关键词智能提取（jieba分词 + 食品领域词库）
3. 词云图可视化（Matplotlib + WordCloud）
4. 支持任意评论输入（后续可扩展成网页版）

### 技术栈
- Python 3.10 + Anaconda
- SnowNLP（中文情感分析）
- jieba（中文分词）
- WordCloud + Matplotlib（可视化）
- pandas（数据处理）

### 如何本地运行（3步）
```bash
git clone https://github.com/zyj-libre/food-ai-sentiment-analysis.git
cd food-ai-sentiment-analysis
python food_ai.py
