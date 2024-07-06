from PIL import Image, ImageDraw
from math import cos, sin, radians

def generate_flag():
    
    width, height = 600, 600
    indian_flag = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(indian_flag)

    draw.rectangle([(0, height//3*2), (width, height)], fill="#138808", outline=None)
    draw.rectangle([(0, 0), (width, height//3)], fill="#FF9933", outline=None)

    # Draw the Ashok Chakra
    center = (300, 300)
    radius = 100
    draw.ellipse([(center[0] - radius, center[1] - radius),
                  (center[0] + radius, center[1] + radius)],
                 outline="#000080", width=2)

    # Draw 24 spokes
    for i in range(24):
        angle = i * 15  # 360 degrees / 24 spokes
        x1 = center[0] + radius * cos(radians(angle))
        y1 = center[1] + radius * sin(radians(angle))
        x2 = center[0] 
        y2 = center[1] 
        draw.line([(x1, y1), (x2, y2)], fill='#000080', width=1)

    return indian_flag


def rotate(img, y):
    
    return img.rotate(y, resample=Image.BICUBIC, expand=True)

def rotatedFlags():
    
    global rotated_flag_0, rotated_flag_90, rotated_flag_180, rotated_flag_270
    original_flag =generate_flag()

    # Rotate the flag at different angles
    rotated_flag_0 = rotate(original_flag, 0)
    rotated_flag_90 = rotate(original_flag, 90)
    rotated_flag_180 = rotate(original_flag, 180)
    rotated_flag_270 = rotate(original_flag, 270)
    rotated_flag_0.show()
    rotated_flag_90.show()
    rotated_flag_180.show()
    rotated_flag_270.show()


rotatedFlags()
