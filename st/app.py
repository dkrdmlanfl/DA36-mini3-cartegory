import streamlit as st
import streamlit as st
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import base64
import time

if 'page' not in st.session_state:
    st.session_state['page'] = 1
# 페이지 변경 함수
def go_to_page(page_num):
    st.session_state['page'] = page_num

if st.session_state['page'] == 1:

    main_bg_color = "#ECF8E0"  # 메인 페이지 배경색
    # CSS 스타일을 적용하여 배경 색 변경
    st.markdown(f"""
        <style>
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        /* 제목 스타일 */
        .big-title {{
            font-size: 4em;  /* 글자 크기 조정 */
            text-align: center;
            margin-bottom: 0.5em;
            color: #333;  /* 제목 색상 */
        }}
        .big-subtitle {{
            font-size: 1em;  /* 부제목 크기 조정 */
            text-align: center;
            margin-bottom: 1.5em;
            color: #666;  /* 부제목 색상 */
        }}
        /* 이미지 크기 조정 */
        .custom-image {{
            display: block;
            margin: 0 auto;  /* 이미지 중앙 정렬 */
            width: 80%;  /* 이미지 너비 조정 (원하는 크기로 설정) */
            max-width: 600px;  /* 최대 너비 제한 */
            height: auto;  /* 비율 유지 */
        }}
        </style>
        """, unsafe_allow_html=True)

    # 이미지 출력 (크기 조정 및 중앙 정렬)
    st.image('data/park.jpg')
    # 큰 제목 한 글자씩 출력 (누적)
    title = "Where to Park?"
    subtitle = "CARTEGORY BY 하와수"

    title_placeholder = st.empty()
    current_title = ""
    for char in title:
        current_title += char
        title_placeholder.markdown(f"<div class='big-title'>{current_title}</div>", unsafe_allow_html=True)
        time.sleep(0.2)

    st.markdown(f"<div class='big-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


    st.markdown('-' * 10)
    col1, col2, col3 = st.columns([2, 2, 2])
    with col3:
        # 버튼 출력
        if st.button("LeT's gO"):
            go_to_page(2)


elif st.session_state['page'] == 2:
    st.markdown(
        """
        <style>
        .stApp {
            max-width: 140%;  /* 페이지의 가로 너비를 100%로 설정 */
            padding-top: 50px;  /* 상단 여백 */
        }
        </style>
        """, unsafe_allow_html=True
    )
    image_path = "data/parkinglot.png"  # 배경 이미지 경로
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
            <style>
            .stApp {{
                background: url(data:image/png;base64,{base64_image});
                background-size: cover;
            }}
            </style>
            """,
        unsafe_allow_html=True
    )

    st.markdown('<br>' * 7, unsafe_allow_html=True)
    st.title('Please register your vehicle 👀')
    st.write('-'*10)
    st.subheader('Upload here⬇️')


    # 모델 로드
    @st.cache_resource  # 캐싱을 통해 모델 로드 속도 향상
    def load_trained_model(model_path):
        return load_model(model_path)


    # model_path = "mb_model.h5"
    model_path = "Xception_model.h5"
    model = load_trained_model(model_path)

    # 차량 모델 리스트
    label_classes = ['Carens', 'Kona', 'Mohave', 'Niro', 'Palisade', 'Santafe',
                     'Seltos', 'Sorento', 'Soul', 'Sportage', 'Tucson', 'Veracruz']

    # 현대차, 기아차 모델 리스트
    electric_vehicles = ['Kona', 'Niro', 'Model', 'Santefe', 'Palisade']
    hyundai_models = ['Palisade', 'Tucson', 'Santafe', 'Veracruz', 'Kona', 'Niro']
    kia_models = ['Carens', 'Mohave', 'Seltos', 'Sorento', 'Soul', 'Sportage']

    # 이미지 업로드
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    with st.container():
        col1, col2 = st.columns([2, 2.5])  # 두 개의 열로 나누기
        with col1:
            st.subheader('Upload here⬇️')
            # 모델 로드
            @st.cache_resource  # 캐싱을 통해 모델 로드 속도 향상
            def load_trained_model(model_path):
                return load_model(model_path)

            # model_path = "mb_model.h5"
            model_path = "Xception_model.h5"
            model = load_trained_model(model_path)

            # 차량 모델 리스트
            label_classes = ['Carens', 'Kona', 'Mohave', 'Niro', 'Palisade', 'Santafe',
                             'Seltos', 'Sorento', 'Soul', 'Sportage', 'Tucson', 'Veracruz']

            # 현대차, 기아차 모델 리스트
            electric_vehicles = ['Kona', 'Niro', 'Model', 'Santefe', 'Palisade']
            hyundai_models = ['Palisade', 'Tucson', 'Santafe', 'Veracruz', 'Kona', 'Niro']
            kia_models = ['Carens', 'Mohave', 'Seltos', 'Sorento', 'Soul', 'Sportage']

            # 이미지 업로드
            uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

            if uploaded_file is not None:
                # 업로드된 이미지 표시
                st.image(uploaded_file, caption="Car Image", use_column_width=True)

        with col2:
            if uploaded_file is None:
                st.write(' ')
            if uploaded_file is not None:
                # 업로드된 이미지 표시
                # st.image(uploaded_file, caption="Car Image", use_column_width=True)

                # 이미지 전처리
                IMAGE_SIZE = 299  # 모델 입력 크기
                image = Image.open(uploaded_file).convert("RGB")  # 이미지를 RGB로 변환
                image = image.resize((IMAGE_SIZE, IMAGE_SIZE))  # 크기 조정
                image_array = np.array(image)
                image_array = preprocess_input(image_array)  # 모델 입력 형식에 맞게 전처리
                batch_image = np.expand_dims(image_array, axis=0)  # 배치 차원 추가

                # 모델 예측
                pred_proba = model.predict(batch_image)
                pred_index = np.argmax(pred_proba)
                pred_label = label_classes[pred_index]
                confidence = pred_proba[0][pred_index]
                # st.markdown('<br>' * 10, unsafe_allow_html=True)
                # 예측 결과에 따른 출력
                # if confidence < 10:
                #     st.markdown('<br>'*6, unsafe_allow_html=True)
                #     st.error ("Sorry, I couldn't recognize this car model.")


                if pred_label in hyundai_models:
                    st.markdown(
                        """
                        < style >
                        .stSuccess
                        {
                            font - size: 24px;
                        padding: 20
                        px;
                        }
                        < / style >
                            """, unsafe_allow_html=True)
                    st.success(f"🚗... Your car is **<Hyundai> - {pred_label}**")
                    st.success(f"🤖... Accuracy is **{confidence * 100:.2f}%**")
                  elif pred_label in kia_models:
                      st.success(f"🚗... Your car is **<Kia> - {pred_label}**")
                      st.success(f"🤖... Accuracy is **{confidence * 100:.2f}%**")

                  # 전기차일 경우 안내 문구 출력
                  if pred_label in electric_vehicles:
                      st.markdown(f"잠깐🤚🏻 {pred_label}는 전기차입니다! 지상 주차장을 이용해주세요.")
                  else:
                      st.info(f"{pred_label}은 지하 주차장에 진입할 수 있습니다. 🥳")

                  # 서버에 이미지 저장
                  SAVE_DIR = "./uploaded_images"
                  os.makedirs(SAVE_DIR, exist_ok=True)
                  save_path = os.path.join(SAVE_DIR, uploaded_file.name)
                  with open(save_path, "wb") as f:
                      f.write(uploaded_file.getbuffer())
                  # st.info(f"The image is successfully saved: {save_path}")

      st.write('-' * 10)
      col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기
      with col1:
          if st.button("⬅️Back"):
              go_to_page(1)

      with col3:
          if st.button("More➡️"):
              go_to_page(3)


  elif st.session_state['page'] == 3:
      main_bg_color = "#ECF8E0"  # 메인 페이지 배경색
      st.markdown(f"""
        <style>
        /* 메인 페이지 배경 색 설정 */
        .stApp {{
            background-color: {main_bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    link = "https://www.chargekorea.com/charge/index.php?"  # 이동할 링크

    main_bg_color = "#ECF8E0"  # 메인 페이지 배경색
    st.markdown(f"""
            <style>
            /* 메인 페이지 배경 색 설정 */
            .stApp {{
                background-color: {main_bg_color};
            }}
            </style>
            """, unsafe_allow_html=True)

    # 이미지 및 타이틀 설정
    # st.image('data/evicon.png')
    # st.title("More about EV!")
    # st.write('-' * 20)
    st.title("EV charging stations near you!")
    st.markdown('<br>', unsafe_allow_html=True)
    image_url = "https://www.chargekorea.com/charge/index.php?"  # 원하는 링크
    image_path = "data/evicon.png"  # 이미지 경로

    # HTML 코드로 이미지를 링크로 감싸기
    st.markdown(
        f"""
        <a href="{image_url}" target="_blank">
            <img src="data:image/png;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" alt="Click here" width="500"/>
        </a>
        <p style="text-align:left; font-size:17px; color:#888;">(Click the image to go to the website.)</p>
        """, unsafe_allow_html=True
    )

    # st.title("EV charging stations near you!")
    # st.write('Click the image to go to the website.')
    st.write('-' * 20)

    col1, col2, col3 = st.columns([2, 4, 2])  # 좌측, 중앙, 우측 열로 나누기

    with col1:
        if st.button("🏠 Home"):
            go_to_page(1)

