import streamlit as st
import streamlit_lottie as st_lottie
import requests

st.set_page_config(page_title="Генерация обложек к видео и аватарок канала с помощью ИИ.", layout="wide")

st.markdown("""
<style>
.st-emotion-cache-zq5wmm, .st-emotion-cache-10pw50
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def creating_ava():
    link = st.text_input("Задача ясна! Теперь необходимо прикрепит ссылку к каналу с контентом.")

    st.write("##")
    st.write("Ссылка получена! Теперь к тематике канала")

    subject_matter = st.multiselect("По желанию можешь выбрать тему, относящуюся к твоему контенту.",
                                    options=("Забавные животные",
                                             "Прохождение видеоигр",
                                             "Руководства и туториалы",
                                             "Сплетни о знаменитостях",
                                             "Влог",
                                             "Смешные видео",
                                             "Шопинг",
                                             "Распаковка посылок",
                                             "Паранки",
                                             "Кулинария",
                                             "Спорт",
                                             "Новости"))
    st.write("##")
    keywords = st.text_area("Есть ли ключевые слова, которые ты бы хотел указать в описании к каналу?")
    st.write("##")
    images = st.file_uploader("Можешь прикрепить желаемые картинки для твоего изображения. Они будут добавлены на фото",
                              type=["png", "ipg"],
                              accept_multiple_files=True)
    if images is not None:
        for image in images:
            st.image(image)

    st.write("##")
    st.write("Отлино! Если ты всё загрузил! Жми кномку и лови аватарку мечты")
    start_btn = st.button("Начать генерацию!", on_click=btn_click)


def creating_cover():
    video = st.file_uploader("Задача ясна! Теперь необходимо прикрепит файлу с контентом.",
                             type="mp4")
    if video is not None:
        st.video(video)

    st.write("##")
    st.write("Файлы загружены! Теперь и тематике.")

    subject_matter = st.multiselect("По желанию можешь выбрать тему, относящуюся к твоему контенту.",
                                    options=("Забавные животные",
                                             "Прохождение видеоигр",
                                             "Руководства и туториалы",
                                             "Сплетни о знаменитостях",
                                             "Влог",
                                             "Смешные видео",
                                             "Шопинг",
                                             "Распаковка посылок",
                                             "Паранки",
                                             "Кулинария",
                                             "Спорт",
                                             "Новости"))
    st.write("##")
    keywords = st.text_input("Есть ли ключевые слова, которые ты бы хотел указать в описании к видео?")
    st.write("##")
    images = st.file_uploader("Можешь прикрепить желаемые картинки для твоего изображения. Они будут добавлены на фото",
                              type=["png", "ipg"],
                              accept_multiple_files=True)
    if images is not None:
        for image in images:
            st.image(image)

    st.write("##")
    st.write("Отлино! Если ты всё загрузил! Жми кномку и лови обложку мечты")
    start_btn = st.button("Начать генерацию!", on_click=btn_click)


def creating_banner():
    link = st.text_input("Задача ясна! Теперь необходимо прикрепит ссылку к каналу с контентом.")

    st.write("##")
    st.write("Ссылка получена! Теперь к тематике канала")

    subject_matter = st.multiselect("По желанию можешь выбрать тему, относящуюся к твоему контенту.",
                                    options=("Забавные животные",
                                             "Прохождение видеоигр",
                                             "Руководства и туториалы",
                                             "Сплетни о знаменитостях",
                                             "Влог",
                                             "Смешные видео",
                                             "Шопинг",
                                             "Распаковка посылок",
                                             "Паранки",
                                             "Кулинария",
                                             "Спорт",
                                             "Новости"))
    st.write("##")
    keywords = st.text_area("Есть ли ключевые слова, которые ты бы хотел указать в описании к каналу?")
    st.write("##")
    images = st.file_uploader("Можешь прикрепить желаемые картинки для твоего изображения. Они будут добавлены на фото",
                              type=["png", "ipg"],
                              accept_multiple_files=True)
    if images is not None:
        for image in images:
            st.image(image)

    st.write("##")
    st.write("Отлино! Если ты всё загрузил! Жми кномку и лови банер мечты")
    start_btn = st.button("Начать генерацию!", on_click=btn_click)


def btn_click():
    pass


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


if task == "Сгенерировать обложку для видео":
    creating_cover()
if task == "Сгенерировать аватарку для канала":
    creating_ava()
if task == "Сгенерировать банера для страницы канала":
    creating_banner()

    contact_forms = """
<form action="https://formsubmit.co/your@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>
    """
