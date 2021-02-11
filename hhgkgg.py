import os
import sys

import pygame
import requests

map_request = "https://yandex.ru/maps/?ll=30.102221%2C51.388941&mode=poi&poi%5Bpoint%5D=30.098714%2C51.389402&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D16097910390&pt=30.058061%2C51.405339&source=entity_search&z=16.56"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)