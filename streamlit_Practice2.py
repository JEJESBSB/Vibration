# module import
# 터미널에서 streamlit run 파일명

import streamlit as st
import numpy as np
import pandas as pd

st.write('바로 이것이 streamlit입니다.')

st.subheader('데이터프레임라이터')
st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 }))

data_frame = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 })
st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame,
         'Above is a dataframe.')


## altair 차트 그리기
import altair as alt
df = pd.DataFrame({
     'a': [1, 2, 3, 4],
     'b': [10, 20, 30, 40],
     'c' : [10, 20, 30, 40],
 })

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

## 각종 헤드 및 마크다운 명령어
## https://docs.streamlit.io/library/api-reference 참조
st.markdown('마크다운명령어: '+ 'Streamlit is **_really_ cool**.')

st.title('타이틀명령어: '+ 'This is a title')

st.header('헤더명령어: '+'This is a header')

st.subheader('서브헤더명령어: ' + 'This is a subheader')

st.caption('캡션명령어: ' + 'This is a string that explains something above.')

st.subheader('코드명령어:')
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

st.text("텍스트명령어: " + 'This is some text.')

# 라텍스 : 수식어 명령
st.subheader('라텍스명령어')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')

# 스크롤되는
df = pd.DataFrame(
    np.random.randn(50, 20), #50x20의 어레이 생성, 컬럼수가 20개 이므로 20개 생성
    columns=('col %d' % i for i in range(20)))

st.subheader('st.dataframe명령어')
st.dataframe(df)  # Same as st.write(df)

# 전체 표 출력
st.subheader('st.table명령어')
st.table(df)

st.subheader('st.metric명령어')

# 단위
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# 컬럼
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


st.metric(label="Gas price", value=4, delta=+0.5,
     delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
     delta_color="off")


import cv2
st.title('카메라 입력입니다.')

img_buffer = st.camera_input("Take a picture")
if img_buffer is not None:
    bytes_data = img_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)



