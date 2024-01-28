import streamlit as st
import pandas as pd


df = pd.read_csv('tenpura_app/data/人口変化.csv', index_col='都道府県コード', encoding='shift_jis')
st.dataframe(df)
