# 1. terminal-> pip install streamlit
# 2. streamlit run 파일명
# 3. 코드 작성 후 실행
# 4. 코드 실행 시 웹페이지 실시간 동기화됨

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import streamlit as st

data = {'x':[10,20,30,40,55,67,76,89,99,100],'y':[110,214,313,456,556,687,789,820,950,1023]}

df = pd.DataFrame(data)

x = df.drop(columns = ["y"], axis = 1)
y = df["y"]

model = LinearRegression()
model.fit(x,y)

import joblib
joblib.dump(model, './regression_model.pkl')

st.title('예측모델 앱 연습중입니')
st.subheader('(1) 아래에 당신 차의 평균 속도를 입력해주세요!!!')

values = st.slider('평균속도 입력하세요', 0, 200)  # st.number_input("평균속도")
st.write('평균속도:', values)

#머신러닝으로 저장된 모델을 호출하고 st로 부터 받은 값으로 예측한다.
loaded_model = joblib.load("./regression_model.pkl")
new_x = [values]
df_new_x = pd.DataFrame(new_x)
new_y = loaded_model.predict(df_new_x )

#예측결과를 화면에 뿌려준다.
st.subheader('(2) 속도에 따른 당신이 납부해야할 보험료는 다음과 같습니다.')
st.write('예상되는 납부보험료:', new_y[0])

######

