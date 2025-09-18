# 1~100
import random
datas = [random.randint(1,100) for i in range(100)]
print(datas)

import streamlit as st
st.bar_chart(datas)
st.line_chart(datas)