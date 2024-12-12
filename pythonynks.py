import streamlit as st

from tkinter import Image

from PIL import Image
# streamlit run python.py で最初の実行
st.title('YNKS診断')
option1=st.selectbox('流行りには乗りたい方ですか？',list(['1.のりたい','2.のりたくない']))

option2=st.selectbox('こだわりは強い方ですか？',list(['1.つよい','2.つよくない']))

option3=st.selectbox('自分の時間を大切にする方ですか？',list(['1.大切にする','2.自分の時間より他人を優先しがち']))

if option1 == '1.のりたい':
    if option2 == "1.つよい":
     if option3 == '1.大切にする':
        st.write("自分のこだわりを大切にしつつ流行りに乗りたいあなたには、アメリカンスピリットがおすすめです！")
        st.image( 'amesupi.jpg')
if option1 == '1.のりたい':
    if option2 == "1.つよい":
      if option3 == '2.自分の時間より他人を優先しがち':
        st.write("流行りに敏感で他人に優しくこだわりが強いあなたはラッキーストライクがおすすめです！")
        st.image('rakisuto.jpg')
if option1 == '1.のりたい':
 if option2 == '2.つよくない':
  if option3 == '1.大切にする':
   st.write('こだわりはないが自身の時間と流行りを大切にするあなたはピースがおすすめです！')
   st.image('peace.webp')
 if option1 == '1.のりたい':
  if option2 == '2.つよくない':
   if option3 == '2.自分の時間より他人を優先しがち':
     st.write('自身のこだわりは特になく流行りに乗りたいだけのあなたはマルボロがおすすめです！特にアカマル')
     st.image('maruboro.jpg')
elif option1 == '2.のりたくない':
  if option2 == '1.つよい':
    if option3 == '1.大切にする':
      st.write('流行りは一切気にせず自分を貫くあなたにはセブンスターがおすすめです！')
      st.image('setta-.webp')
if option1 == '2.のりたくない':
       if option2 == '1.つよい':
        if option3 == '2.自分の時間より他人を優先しがち':
          st.write('こだわり深いが他人を思いやれる熱いあなたにはウィンストンがおすすめです！')
          st.image('winston.jpg')
if option1 == '2.のりたくない':
        if option2 == '2.つよくない':
          if option3 == '1.大切にする':
            st.write('こだわりが強くなくスマートなあなたにはラークがおすすめです！')
            st.image('lark.png')
if option1 == '2.のりたくない':
            if option2 == '2.つよくない':
              if option3 == '2.自分の時間より他人を優先しがち':
                st.write('どこまでも他人の気遣いができるあなたにはメビウスがおすすめです！')
                st.image('mevius.jpg')




# st.option1('1.のりたい'):option2('1.つよい'),option3('大切にする')
# st.write('あいうえお')
    


