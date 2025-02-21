import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title("Streamlit　超入門")
st.write('プログレスバーの表示')
'Start!!'
latest_iteration= st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'

# st.write("DataFrame")

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目': [10, 20, 30, 40]
# })
# st.write("動的なDFはdataframeを使用")
# st.dataframe(df.style.highlight_max(axis=0), 
#             #  width=200, height=200
#              )
# st.write("静的なDFはtableを使用")
# st.table(df.style.highlight_max(axis=0), 
#             #  width=200, height=200
#              )

# st.write("マジックコマンドでマークダウンでの記述")
# """
# # 章
# ## 節
# ### 項目
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd

# ```
# """
# st.write("乱数を生成したDF")
# df_2 = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=["a", "b", "c"]
# )
# st.dataframe(df_2)
# st.line_chart(df_2)
# st.area_chart(df_2)
# st.bar_chart(df_2)
# st.write("マップを表示")
# df_3 = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] +[35.69, 139.70],
#     columns=["lat", "lon"]
# )
# st.dataframe(df_3, height=200)
# st.map(df_3)

if st.checkbox('Show Image'):
    img = Image.open("imgs/astro_corgi_cats.webp")
    st.image(img, caption="Astro corgi and cats", use_container_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     options=list(range(1, 10))
# )
# st.write(f'あなたの好きな数字は{option}です。')

left_column, right_column= st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容1を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内2容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容3を書く')

# hobby = st.text_input('あなたの趣味を教えてください')
# st.write(f'貴方の趣味は{hobby}です')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# st.write(f'コンディション: {condition}')