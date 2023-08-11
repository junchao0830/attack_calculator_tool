import streamlit as st
from PIL import Image

st.set_page_config(page_title="武器的期望秒伤计算器", layout="wide")  # centered
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("武器的期望秒伤计算器")

configs_dict = {
    '每秒攻击力': [0.0, 100000.0, 0.0],
    '暴击率': [0.0, 1.0, 0.0],
    '暴击伤害倍率': [0.0, 100.0, 0.0],

}



header_layout_range = [0.5, 1.5, 0.5]
# Header layout
col_start1, col_start2, col_start3 = st.columns(
    header_layout_range
)
# lottie_spring_animation_loop


with st.container():
    with col_start2:
        #st.write("##")
        st.write("输入武器的每秒攻击力、暴击率、暴击伤害倍率，计算武器的期望秒伤。")
        image = Image.open('imgs/img.jpg')
        st.image(image, caption='',use_column_width=True)
        #st.write("##")
        
        key_1 = '每秒攻击力'
        attack_per_second = st.number_input(
                '每秒攻击力 （范围：0-100000）',
                min_value=configs_dict[key_1][0],
                max_value=configs_dict[key_1][1],
                value=configs_dict[key_1][2],
            )

        key_2 = '暴击率'
        sudden_attack_rate = st.number_input(
                '暴击率 （范围：0-1）',
                min_value=configs_dict[key_2][0],
                max_value=configs_dict[key_2][1],
                value=configs_dict[key_2][2],
            )     

        key_3 = '暴击伤害倍率'
        damage_multi_rate = st.number_input(
                '暴击伤害倍率 （范围：0-100）',
                min_value=configs_dict[key_3][0],
                max_value=configs_dict[key_3][1],
                value=configs_dict[key_3][2],
            )

        result = attack_per_second*(1-sudden_attack_rate)+attack_per_second*(sudden_attack_rate*damage_multi_rate)

        
        st.write(f"计算结果为：{result}")