import streamlit as st
import streamlit_lottie as st_lottie
import requests

import request_handling


st.set_page_config(page_title="Генерация обложек к видео и аватарок канала с помощью ИИ.", layout="wide")

st.markdown("""
<style>
.st-emotion-cache-zq5wmm, .st-emotion-cache-10pw50
{
    visibility: hidden;
}
.sticky{
  position: sticky;
  z-index: 10;
}

</style>
""", unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def creating_img():
    videos = st.file_uploader("Задача ясна! Теперь необходимо прикрепит файлу с контентом.",
                             type="mp4", accept_multiple_files=True)
    if videos is not None:
        for video in videos:
            st.video(video)

    st.write("##")
    st.write("Файлы загружены! Теперь к тематике.")

    subject_matter = st.multiselect("По желанию можешь выбрать тему, относящуюся к твоему контенту.",
                                    options=("Забавные животные",
                                             "Прохождение видеоигр",
                                             "Руководства и туториалы",
                                             "Сплетни о знаменитостях",
                                             "Влог",
                                             "Смешные видео",
                                             "Шопинг",
                                             "Распаковка посылок",
                                             "Пранки",
                                             "Кулинария",
                                             "Спорт",
                                             "Новости"))
    
    st.write("##")
    keywords = st.text_input("Есть ли ключевые слова, которые ты бы хотел указать в описании к видео?")

    st.write("##")
    images = st.file_uploader("Можешь прикрепить желаемые картинки для твоего изображения. Они будут добавлены на фото",
                              type=["png", "jpg"],
                              accept_multiple_files=True)
    if images is not None:
        for image in images:
            st.image(image)

    st.write("##")
    st.write("Отлично! Если ты всё загрузил! Жми кномку и лови обложку мечты")

    # обернули вызов обработчика в лямбду
    gen_button_handler = lambda video_path, text: request_handling.process(video_path,
                                                                           subject_matter,
                                                                           text,
                                                                           images)
    
    # тут надо вызывать
    start_btn = st.button("Начать генерацию!", on_click=gen_button_handler)


lottie_coding = load_lottieurl("https://lottie.host/77556afe-9041-4589-87d7-adb0a2fdc4d0/aEKCuzSaHO.json")


# --- Секция заголовков ---
with st.container():
    lf_col, rig_col = st.columns(2)
    with lf_col:
        st.write("Генерация обложек к видео и аватарок канала с помощью ИИ")
        st.header(
            "Создал крутой видео-контент и хочешь для него цепляющую за душу обложку? Или хочешь порадовать себя новой аватаркой в RUTUBE? Тогда тебе к нам!")
        st.subheader("Загружай видео, добавляй параметры и получи стильную обложку для своего контента")
    with rig_col:
        st.lottie(lottie_coding)

with st.container():
    st.write("---")
    st.header("Готов создать обложку мечты? Отлично, начинаем!")
    task = st.radio("Для начала выбери, какую задачу нужно решить?",
                    options=("Сгенерировать обложку для видео", "Сгенерировать аватарку для канала",
                             "Сгенерировать банера для страницы канала"))
creating_img()

if task == "Сгенерировать обложку для видео":
    pass
if task == "Сгенерировать аватарку для канала":
    pass
if task == "Сгенерировать банера для страницы канала":
    pass

lottie_loading = load_lottieurl("https://lottie.host/6056169b-b5e0-4763-803d-77e0a97e52b5/FmTPJdKcor.json")

contact_forms = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
"""