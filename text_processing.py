from translatepy import Translator

# Переводит текст с русского на английский
def translate(rus_text):
	translator = Translator()

	eng_text = translator.translate(rus_text, "English")

	return eng_text

# Проверяет наличие запретных слов
# Возвращает 1, если ЕСТЬ запретные слова
# Возвращает 0, если НЕТ запретных слов
def is_stop_word(rus_text, path_words):
	with open(path_words, 'r') as f:
		stop_words = [bad_word[:-1].lower() for bad_word in f.readlines()]
		for word in rus_text.split():
			if word.lower() in stop_words:
				return 1
	return 0

# Обработка и перевод текста
# Возвращает переведенную на английский строку
# Или пустую строку, в случае неудачи
def text_process(rus_text, path_words):
	if not is_stop_word(rus_text, path_words):
		return translate(rus_text)
	return ""

if __name__ == '__main__':
	rus_text = input()
	path_words = "stopwords.txt"

	print(text_process(rus_text, path_words))