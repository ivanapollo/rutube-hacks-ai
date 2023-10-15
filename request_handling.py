import requests
import os
import base64

import streamlit as st

from get_frames import *

api = 'http://127.0.0.1:7860'

SD_MODEL = '768-v-ema.safetensors'

negp = '''two bodies, two heads, doll, extra nipples, bad anatomy, blurry, fuzzy, extra arms, extra fingers, poorly drawn hands, disfigured, tiling, deformed, mutated, out of frame, cloned face, ugly, disfigured, bad proportion, out of frame, b&w, painting, drawing, watermark, logo, text, signature, icon, monochrome, blurry, ugly, cartoon, 3d, bad_prompt, long neck, totem pole, multiple heads, multiple jaws, disfigured, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, username, artist name, ancient, character, frame, child, asian, cartoon, animation, grayscale 3d, disfigured, bad art, deformed, poorly drawn, extra limbs, strange colours, boring, sketch, lackluster, repetitive, cropped, naked, nude, disfigured, double heads, duplicated, text, oversaturated'''

def process(path_to_video: str,
            subject_matter: list,
            keywords: str,
            images: list):
    
    # st.lottie(lottie_loading, height=50)
    
    # TODO: вызываю Толю, разбиваем видео на кадры
    frame_paths = get_frames(path_to_video, './temp')

    ret_list = []

    for path in frame_paths:
        gen_path = img2img(api, keywords, 15, path)
        ret_list.append(gen_path)
        st.image(gen_path)

    return ret_list

    # TODO: вызываю Настю, удаляем плохие слова


def img2img(api, text, steps, image_path):

    opt = requests.get(url=f'{api}/sdapi/v1/options')
    opt_json = opt.json()

    # TODO: тут менять модель 
    opt_json['sd_model_checkpoint'] = SD_MODEL

    requests.post(url=f'{api}/sdapi/v1/options', json=opt_json)

    # путь до скрипта
    api_url = f"{api}/sdapi/v1/img2img"

    # открыли файл
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # закодировали для сетки
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    # это то что отправляем нейросетке 
    payload = {
        'prompt' : text,
        'negative_prompt': negp,
        "init_images": [encoded_image],
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

# print(process('/home/stdf/Desktop/12.mp4', [], 'guy with a sport car', []))