request_handling.process(path_to_video: str, 
                            subject_matter: list
                            keywords: str
                            images: list)

def process(path_to_video: str,
            subject_matter: list,
            keywords: str,
            images: list):
    
    # TODO: вызываю Толю, разбиваем видео на кадры

    # TODO: вызываю Настю, удаляем плохие слова

    


    st.lottie(lottie_loading, height=50)
    for image_path in img_list:
        st.image(image_path)