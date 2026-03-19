import streamlit as st
import snownlp
import jieba

st.title("🍜 食品电商AI情感分析系统（实时演示版）")
st.write("输入任意食品评论，秒出情感判断 + 差评关键词")

user_input = st.text_input("请输入评论：", "这个牛奶过期了，喝了拉肚子，太差了！")

if st.button("开始分析"):
    if user_input.strip():
        s = snownlp.SnowNLP(user_input)
        score = s.sentiments
        sentiment = "正面 👍" if score > 0.5 else "负面 👎"
        
        words = jieba.lcut(user_input)
        keywords = [w for w in words if len(w) > 1 and w in ["过期", "添加剂", "烂", "假货", "差", "拉肚子", "不新鲜", "保质期短"]]
        
        st.success(f"情感判断：{sentiment}（置信度 {score:.3f}）")
        st.info(f"提取的差评关键词：{keywords if keywords else '无明显痛点'}")
    else:
        st.warning("请输入评论内容")