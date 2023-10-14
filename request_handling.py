import requests
import os
import base64

from get_frames import *

api = 'http://127.0.0.1:7860'


def process(path_to_video: str,
            subject_matter: list,
            keywords: str,
            images: list):
    
    # TODO: вызываю Толю, разбиваем видео на кадры
    frame_paths = get_frames(path_to_video, './temp')

    ret_list = []

    for path in frame_paths:
        print(path)
        ret_list.append(
            img2img(api, keywords, 15, path)
        )

    return ret_list

    # TODO: вызываю Настю, удаляем плохие слова

    # st.lottie(lottie_loading, height=50)
    # for image_path in img_list:
    #     st.image(image_path)


def img2img(api, text, steps, image_path):

    # путь до скрипта
    api_url = f"{api}/sdapi/v1/img2img"

    # открыли файл
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # закодировали для сетки
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    # это то что отправляем нейросетке 
    payload = {
        "init_images": [encoded_image],
        'prompt' : text,
        "steps": steps,
    }

    # ответ
    sd_response = requests.post(api_url, json=payload)
    
    name = f'{os.path.basename(image_path)}_temp'
    
    if sd_response.status_code == 200:

        sd_response = sd_response.json()
        encoded_result = sd_response["images"][0]
        result_data = base64.b64decode(encoded_result)
        
        output_path = f"results/{name}.jpg" 
        with open(output_path, 'wb') as file:
            file.write(result_data)

        return output_path
    
    else:
        print("Ошибка при выполнении запроса:", sd_response.text)
        return None

print(process('/home/stdf/Desktop/12.mp4', [], 'guy with a sport car', []))