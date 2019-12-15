from PIL import Image, ImageDraw


image = Image.open("elsa.jpg")  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width, height = image.size
pix = image.load()  # Выгружаем значения пикселей.


def negative():
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    image.save('negative_elsa.png')


def quality():
    image = Image.open('elsa.jpg')
    image = image.resize((width * 2, height * 2))
    image.save("resized_picture.png")


def sepia():
    depth = 30
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
    image.save('sepia_elsa.png')


def b_w():
    factor = 100

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image.save('elsabw.png')


if __name__ == "__main__":
    negative()
    sepia()
    quality()
    b_w()
