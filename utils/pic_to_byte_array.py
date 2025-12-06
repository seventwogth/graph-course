# Скрипт для преобразования изображения в byte-array, будет полезно при выполнении заданий текстурирования
# !!! ВАЖНО !!! - ваше изображение должно быть 128x128
# Убедись, что либа PIL у тебя установлена, если нет - pip install pillow
# Указываешь путь до изображения, прогоняешь его через скрипт, вывод копируешь в .h - файл

from PIL import Image

img = Image.open('source.jpg').convert('RGB')
img = img.resize((128, 128))

pixels = list(img.getdata())
output = []

print("Копируй всё, что ниже, в свой .h файл:")
print("/* My custom 128x128 texture */")

count = 0
line = ""
for r, g, b in pixels:
    line += f"{r},{g},{b}, "
    count += 1
    if count % 10 == 0:
        print(line)
        line = ""

if line:
    print(line)
