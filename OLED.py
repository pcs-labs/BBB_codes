import time
from Adafruit_SSD1306 import SSD1306_128_64
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C and the SSD1306 OLED display
oled = SSD1306_128_64(rst=None, i2c_address=0x3C)
oled.begin()
oled.clear()
oled.display()

# Create a blank image for drawing
width = oled.width
height = oled.height
image = Image.new('1', (width, height))  # 1-bit color
draw = ImageDraw.Draw(image)

# Load a font (use default if not available)
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
except IOError:
    font = ImageFont.load_default()

# Write "Hello World!" to the OLED
draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear screen
text = "Hello, World!"
draw.text((10, 20), text, font=font, fill=255)  # Add text at position (10, 20)

# Display image on the OLED
oled.image(image)
oled.display()

# Keep the display active for a while
time.sleep(10)

# Clear the display before exiting
oled.clear()
oled.display()
