from PIL import Image

img = Image.open("pixel_art.png").convert("RGBA")

width, height = img.size
pixels = [[img.getpixel((x, y)) for x in range(width)] for y in range(height)]

max_size = 1

def check_rect(x1, y1, x2, y2):
    value = pixels[y1][x1]
    while y1 != y2:
        while x1 != x2:
            if pixels[y1][x1] != value:
                return False
        x1 += 1
    y1 += 1
    return True

for y in range(height):
    for x in range(width):


new_img = Image.new("RGBA", (width, height))
for y in range(height):
    for x in range(width):
        new_img.putpixel((x, y), pixels[y][x])

new_img.save("new.png")
