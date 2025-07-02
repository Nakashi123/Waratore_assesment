import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="GDS・MMSE 判定ツール", layout="centered")
st.title("GDS・MMSE　健康状態簡易判定ツール")

gds = st.number_input("GDSスコア（0〜15）を入力", min_value=0, max_value=15, value=0)
mmse = st.number_input("MMSEスコア（0〜30）を入力", min_value=0, max_value=30, value=30)

def classify_gds(score):
    if score <= 4:
        return "正常", "🙂", "いまのところ、気分の落ち込みはあまり見られません。", "green"
    elif score <= 8:
        return "軽度うつの可能性", "😐", "少し気持ちが落ち込んでいるかもしれません。", "orange"
    elif score <= 11:
        return "中等度うつの可能性", "😟", "元気が出にくい状態かもしれません。", "darkorange"
    else:
        return "重度うつの可能性", "☹️", "心の元気がかなり下がっています。", "red"

def classify_mmse(score):
    if score >= 27:
        return "正常", "🙂", "記憶や考える力はしっかりしています。", "green"
    elif score >= 21:
        return "軽度認知障害", "😐", "少し忘れっぽさがあるかもしれません。", "orange"
    elif score >= 10:
        return "中等度認知症", "😟", "物忘れが生活に影響しているかもしれません。", "darkorange"
    else:
        return "重度認知症", "☹️", "記憶や判断の力が大きく低下しています。", "red"

gds_label, gds_icon, gds_msg, gds_color = classify_gds(gds)
mmse_label, mmse_icon, mmse_msg, mmse_color = classify_mmse(mmse)

st.subheader("判定結果")

st.markdown(f"### MMSE：**{mmse}点** {mmse_icon}")
st.markdown(f"**分類**：{mmse_label}　　**説明**：{mmse_msg}")
st.progress(mmse / 30)

st.markdown(f"### GDS：**{gds}点** {gds_icon}")
st.markdown(f"**分類**：{gds_label}　　**説明**：{gds_msg}")
st.progress(gds / 15)
