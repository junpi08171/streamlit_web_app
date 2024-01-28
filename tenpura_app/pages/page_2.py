import streamlit as st
import datetime

with st.form(key='profile_form'):
 # テキストボックス

  name = st.text_input('名前')
  address = st.text_input('住所')

 #  セレクトボックス
  
  age_categoly = st.selectbox(
    '年齢層',
    ('子供(18歳未満)', '大人(18歳以上)'))
  
 #  マルチセレクト
  
  hobby = st.multiselect(
    '趣味',
    ('スポーツ','読書','開発','アニメ','釣り','料理')
  )

 #  チェックボックス
  mail_subscribe = st.checkbox('メールマガジンを購読する')

  # スライダー
  height = st.slider('身長', min_value=100,max_value= 230)

  # 日付
  birthday = st.date_input(
    '誕生日',
    datetime.date(2015, 1, 1))
  

  # ボタン
  submit_btn = st.form_submit_button('送信！')
  cansel_btn = st.form_submit_button('キャンセル')
  if submit_btn:
    st.text(f'ようこそ！{name}さん!{address}に書籍を送りました！')
    st.text(f'年齢層:{age_categoly}')
    st.text(f'趣味:{",".join(hobby)}')
    st.write(f'誕生日:, {birthday}')