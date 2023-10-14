import os
import sys
import cv2
from random import randint

# Функция, которая вырезает нужные кадры и возвращает массив ссылок на них
def get_frames(filename, out_path):
	video = cv2.VideoCapture(filename)

	frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

	step = frame_count // 4

	paths = []

	for i in range(4):
		video.set(cv2.CAP_PROP_POS_FRAMES,randint(step*i,step*(i+1)))
		success, image = video.read()
		if success:
			imgpath = out_path + "/img" + str(i) + ".jpg"
			cv2.imwrite(imgpath, image)
			paths.append(imgpath)
		else:
			print("Ошибка получения кадра")
			return []

	return(paths)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Требуется два аргумента: путь к видеофайлу, путь к директории вывода")
		exit()

	try:
		filename = str(sys.argv[1])
		out_path = str(sys.argv[2])
	except Exception:
		print("Ошибка чтения аргументов")
		exit()

	if not os.path.exists(out_path):
		os.makedirs(out_path)

	for i in range(4):
		imgpath = out_path + "img" + str(i) + ".jpg"
		if os.path.isfile(imgpath):
			try:
				os.remove(imgpath)
			except Exception:
				print("Ошибка: файл уже существует")
				exit()

	get_frames(filename,out_path)