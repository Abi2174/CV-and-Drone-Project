from PIL import Image, ImageDraw
from math import cos, sin, radians

def generate_flag():
    
    width, height = 600, 600
    indian_flag = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(indian_flag)

    # Draw the green rectangle (bottom part of the flag)
    draw.rectangle([(0, height//3*2), (width, height)], fill="#138808", outline=None)
    # Draw the saffron rectangle (top part of the flag)
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


indian_flag = generate_flag()
indian_flag.show()
