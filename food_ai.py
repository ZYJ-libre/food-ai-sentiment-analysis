import snownlp
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False     # 解决负号显示问题

# ================== 食品评论测试数据 ==================
comments = [
    "这个牛奶过期了，喝了拉肚子，太差了！",
    "零食很好吃，包装精美，下次还买",
    "生鲜水果不新鲜，有烂的，退货！",
    "添加剂太多，吃着不放心",
    "口感很棒，性价比高，推荐",
    "假货！和图片完全不一样",
    "保质期短，刚买就过期了",
    "味道不错，孩子爱吃"
]

positive = 0
negative = 0
keywords = []

for text in comments:
    s = snownlp.SnowNLP(text)
    score = s.sentiments
    if score > 0.5:
        positive += 1
    else:
        negative += 1
    if score < 0.5:
        words = jieba.lcut(text)
        for w in words:
            if len(w) > 1 and w in ["过期", "添加剂", "烂", "假货", "差", "拉肚子", "不新鲜", "保质期短"]:
                keywords.append(w)

print(f"正面评论: {positive} 条")
print(f"负面评论: {negative} 条")
print(f"高频差评关键词: {keywords}")
print("正在生成词云图...")

# 词云图（强制保存为图片）
text = " ".join(keywords)
wc = WordCloud(font_path="C:\\Windows\\Fonts\\simhei.ttf", background_color="white", width=800, height=400).generate(text)
plt.imshow(wc)
plt.axis("off")
plt.title("食品电商差评关键词词云图")
plt.savefig("食品差评词云图.png")   # 强制保存到 D:\COI 文件夹
plt.show()
print("词云图已保存为：食品差评词云图.png （去文件夹双击打开查看）")