import cv2
import numpy as np
import random
import string
import os

def save_video_drafts(v_class, file):
    vidcap = cv2.VideoCapture(file)
    success, image = vidcap.read()
    count = 0
    capt = 0
    while success:
        if count % 120 == 0:  # сохраняем только каждый 10-й кадр
            # Добавляем полупрозрачный текст на кадр
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (8, 15)
            fontScale = 0.3
            thickness = 1
            # Создаем маску для текста с полупрозрачным фоном
            mask = image.copy()

            # Выбираем цвет фона для текста (белый в вашем случае)
            text_bg_color = (111, 190, 248)

            # Заполняем маску выбранным цветом
            cv2.putText(mask, v_class, org, font, fontScale, text_bg_color, thickness, cv2.LINE_AA)

            # Создаем полупрозрачный текст
            alpha = 0.7  # Степень прозрачности (0.0 - полностью прозрачный, 1.0 - полностью непрозрачный)
            image_with_transparent_text = cv2.addWeighted(image, 1 - alpha, mask, alpha, 0)

            # Сохраняем изображение с полупрозрачным текстом
            random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
            cv2.imwrite("drafts/" + v_class + "_%d_%s.jpg" % (capt, random_chars), image_with_transparent_text)
            capt += 1
        success, image = vidcap.read()
        count += 1

def save_image_drafts(v_class, file):
    # Если файл является изображением, то просто подписываем его и сохраняем
    image = cv2.imread(file)
    # Добавляем полупрозрачный текст на изображение
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (8, 15)
    fontScale = 0.3
    thickness = 1
    text_bg_color = (111, 190, 248)
    cv2.putText(image, v_class, org, font, fontScale, text_bg_color, thickness, cv2.LINE_AA)
    # Сохраняем изображение с полупрозрачным текстом
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    cv2.imwrite("drafts_test/" + v_class + "_%s.jpg" % random_chars, image)

file_types = {
    'jpg': 'img',
    'jpeg': 'img',
    'png': 'img',
    'mp4': 'vid',
    'avi': 'vid',
    'mkv': 'vid',
}

def get_file_type(file_path):
    # Получаем расширение файла
    extension = os.path.splitext(file_path)[1][1:].lower()
    # Ищем тип файла в словаре
    file_type = file_types.get(extension, 'Неизвестный тип файла')
    return file_type

def parse_directory(directory):
    for root, dirs, files in os.walk(directory):
        # Получаем название текущей папки, удаляя путь до директории
        current_dir_name = os.path.basename(root)
        for file in files:
            full_path = os.path.join(root, file)
            if (get_file_type(full_path) == 'img'):
                print(f"✨ Processing 🏙️  image {current_dir_name} in {full_path}")
                save_image_drafts(current_dir_name,full_path)
            elif (get_file_type(full_path) == 'vid'):
                print(f"✨ Processing 📹  video {current_dir_name} in {full_path}")
                save_video_drafts(current_dir_name,full_path)
            else:
                print(f"⚠️  The file {full_path} has an unknown format or is damaged!")

parse_directory('preparation')