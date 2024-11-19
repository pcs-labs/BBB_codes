from PIL import Image, ImageDraw, ImageFont

# Create a blank image
image = Image.new("1", (128, 64), "black")  # 128x64 pixels, 1-bit color
draw = ImageDraw.Draw(image)

# Draw a rectangle and some text
draw.rectangle((0, 0, 127, 63), outline=1, fill=0)
font = ImageFont.load_default()
draw.text((10, 25), "Hello, World!", font=font, fill=1)

# Save to file for verification
image.save("test_image.bmp")
print("Image created: test_image.bmp")
