import requests
import os
import base64

import get_frames

def process(path_to_video: str,
            subject_matter: list,
            keywords: str,
            images: list):
    
    # TODO: вызываю Толю, разбиваем видео на кадры
    frames_path = get_frames.get_frames(path_to_video, 'temp')



    # TODO: вызываю Настю, удаляем плохие слова

    # st.lottie(lottie_loading, height=50)
    # for image_path in img_list:
    #     st.image(image_path)

api = 'http://127.0.0.1:7860'

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
        
        output_path = f"temp/{name}.jpg" 
        with open(output_path, 'wb') as file:
            file.write(result_data)

        return name
    else:
        print("Ошибка при выполнении запроса:", sd_response.text)
        return None

prompt = int(input())
print(img2img(api, prompt, 15, '1.jpeg'))

