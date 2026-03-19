import snownlp
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ================== 解决中文乱码（永久修复） ==================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ================== 测试数据（先跑一次完整效果） ==================
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

text = " ".join(keywords)
wc = WordCloud(font_path="C:\\Windows\\Fonts\\simhei.ttf", background_color="white", width=800, height=400).generate(text)
plt.imshow(wc)
plt.axis("off")
plt.title("食品电商差评关键词词云图")
plt.savefig("食品差评词云图.png")
plt.show()

# ================== 项目2.0：实时输入演示模式 ==================
print("\n" + "="*50)
print("【项目2.0 实时输入演示模式】")
print("复试演示专用：输入任意食品评论，秒出情感+关键词")
print("输入 'exit' 或 '退出' 结束演示")
print("="*50)

while True:
    user_input = input("\n请输入一条食品评论：")
    if user_input.strip().lower() in ['exit', '退出']:
        print("演示结束！项目2.0已完美收工～")
        break
    
    s = snownlp.SnowNLP(user_input)
    score = s.sentiments
    sentiment = "正面👍" if score > 0.5 else "负面👎"
    
    # 提取关键词
    words = jieba.lcut(user_input)
    hit_keywords = [w for w in words if len(w) > 1 and w in ["过期", "添加剂", "烂", "假货", "差", "拉肚子", "不新鲜", "保质期短"]]
    
    print(f"情感判断：{sentiment}（置信度: {score:.3f}）")
    print(f"提取的差评关键词：{hit_keywords if hit_keywords else '无明显痛点关键词'}")
    print("-" * 40)