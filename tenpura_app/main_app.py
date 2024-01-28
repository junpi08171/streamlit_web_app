import datetime
import streamlit as st
from PIL import Image
import pandas as pd

# テキスト関連

st.title('てんぷらアプリ')
st.caption('これはてんぷらの練習用のテストアプリです')

# 画像
image = Image.open('./data/プリニー族A.jpg')
st.image(image, width=200)
