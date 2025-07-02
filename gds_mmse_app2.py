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

# 色付きバーをmatplotlibで表示（カラーバー部分）
def colored_bar(score, max_score, color, title):
    fig, ax = plt.subplots(figsize=(5, 0.4))
    ax.barh([0], [score], color=color, edgecolor='black')
    ax.set_xlim(0, max_score)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title(f"{title}: {score} / {max_score}", fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

st.subheader("スコア可視化（カラーバー）")
colored_bar(mmse, 30, mmse_color, "MMSE")
colored_bar(gds, 15, gds_color, "GDS")

# GDS×MMSEの組み合わせ別アドバイス
advice_dict = {
    ("正常", "正常"): "今のところ、記憶や気分の両面で問題は見られません。健康的な生活を心がけて過ごしましょう。",
    ("正常", "軽度認知障害"): "記憶力に少し変化が見られるかもしれませんが、気分は安定しています。日常のリズムを大切にし、生活の工夫やメモ活用などを取り入れてみましょう。",
    ("正常", "中等度認知症"): "記憶力の低下が日常生活に影響を与えている可能性がありますが、気分は比較的安定しています。サポートを受けながら、安心できる生活環境を整えていきましょう。",
    ("正常", "重度認知症"): "記憶や判断力に大きな低下が見られますが、気分は落ち着いています。周囲の支援を受けながら、心地よく暮らせる環境づくりが大切です。",
    
    ("軽度うつの可能性", "正常"): "気分に少し落ち込みが見られるかもしれませんが、記憶力は問題ありません。気分転換や人との交流を意識しながら、無理のない範囲で活動しましょう。",
    ("軽度うつの可能性", "軽度認知障害"): "気分と記憶の両面で軽い変化が見られます。疲れやすさを感じるかもしれませんが、休養と生活の見直し、必要に応じた相談をおすすめします。",
    ("軽度うつの可能性", "中等度認知症"): "物忘れと気分の低下が同時に見られる可能性があります。周囲の方に気持ちを伝えたり、必要な支援を早めに受けられるように環境を整えましょう。",
    ("軽度うつの可能性", "重度認知症"): "気分と記憶の両方に支援が必要な状態です。ひとりで抱え込まず、医療や福祉の専門家の協力を得ながら、安心して過ごせる方法を一緒に考えていきましょう。",
    
    ("中等度うつの可能性", "正常"): "気分の低下が生活に影響している可能性がありますが、記憶力は保たれています。医師や支援者と相談しながら、気分を整える手段を考えてみましょう。",
    ("中等度うつの可能性", "軽度認知障害"): "記憶力と気分の両方に注意が必要な段階です。早めの対応が、今後の生活の安定につながります。信頼できる人に相談してみましょう。",
    ("中等度うつの可能性", "中等度認知症"): "物忘れと気分の低下が日常生活に支障を与えている可能性があります。サポート体制を整え、無理なく生活できるよう一緒に工夫していきましょう。",
    ("中等度うつの可能性", "重度認知症"): "気分の落ち込みと認知機能の大きな低下が重なっています。早急に専門家の支援を受け、本人が安心できる環境づくりを行っていくことが大切です。",
    
    ("重度うつの可能性", "正常"): "気分の状態に強い落ち込みが見られますが、記憶力は保たれています。早めに専門家の支援を受け、心の元気を取り戻すことを目指しましょう。",
    ("重度うつの可能性", "軽度認知障害"): "気分の落ち込みと少しの物忘れが見られます。一人で抱え込まず、心身両面のサポートを受けながらゆっくり回復を目指しましょう。",
    ("重度うつの可能性", "中等度認知症"): "心の不調と物忘れが重なっている状態です。家族や支援者、専門職と連携しながら、安心できる日常を整えていきましょう。",
    ("重度うつの可能性", "重度認知症"): "心の元気と記憶・判断力の低下がともに強く見られる可能性があります。安全で穏やかな生活環境を周囲の協力のもとで整え、本人が安心して過ごせることを第一に考えましょう。",
}

st.subheader("あなたのスコアに基づく今後のアドバイス")
advice = advice_dict.get((gds_label, mmse_label), "現在の状態に応じて専門家にご相談ください。")
st.markdown(f"🖋🖋 {advice}")
