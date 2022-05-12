import streamlit as st
#AI모델을 불러오기 위한 joblib 불러오기
import joblib
import pandas as pd

ohe_station = joblib.load("ohe_station.pkl")
scaler_call = joblib.load("scaler.pkl")
model_call = joblib.load("model.pkl")

data = pd.read_csv("5.Shop_rental.csv")
print(data.head(5))

# 빈칸에 값 입력받기
def user_input_features() :
  dist = st.sidebar.number_input("거리: ")
  office =st.sidebar.number_input("오피스비중: ")
  home = int(st.sidebar.number_input("홈비중: "))
  station =st.sidebar.number_input("역근처여부: ")
  co2 = st.sidebar.number_input("일산화탄소양: ")
  room =st.sidebar.number_input("방수: ")
  age = st.sidebar.number_input("연수: ")
  pop = st.sidebar.number_input("유동인구수: ")
  road = st.sidebar.number_input("고속도로: ")
  mange = st.sidebar.number_input("관리비: ")
  kid = st.sidebar.number_input("아이들비중: ")

  # 입력받은 값 data에 저
  data = {'dist' : [dist],
          'office' : [office],
          'home' : [home],
          'station' : [station],
          'co2' : [co2],
          'room' : [room],
          'age' : [age],
          'pop' : [pop],
          'road' : [road],
          'mange' : [mange],
          'kid' : [kid]
          }
  data_df = pd.DataFrame(data, index=[0])
  return data_df

st.title('렌탈료 예측 서비스')
st.markdown('* 우측에 데이터를 입력해주세요')

# 입력된 데이터 값 new_x_df에 저장하기
new_x_df = user_input_features()

# 입력받은 값 원핫인코딩 실행
data_cat2 = ohe_station.transform(new_x_df[['station']])
data_concat = pd.concat([new_x_df.drop(columns=['station']),pd.DataFrame(data_cat2, columns=['station_' + str(col) for col in ohe_station.categories_[0]])], axis=1)

# 원핫인코딩 실행 후 scale 조정
data_con_scale = scaler_call.transform(data_concat)

# 전처리 된 데이터 통해서 예측 모델 수행
result = model_call.predict(data_con_scale)

#예측결과를 화면에 뿌려준다.
st.subheader('결과는 다음과 같습니다.')
st.write('예상되는 렌탈료:', result[0])
