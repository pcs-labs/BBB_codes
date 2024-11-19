import time
from Adafruit_SSD1306 import SSD1306_128_64
from PIL import Image, ImageDraw, ImageFont

# Initialize the display
disp = SSD1306_128_64(rst=None, i2c_address=0x3C)
disp.begin()
disp.clear()
disp.display()

# Create blank image for drawing
width, height = disp.width, disp.height
image = Image.new("1", (width, height))  # 1-bit color
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Function to display content
def show_display():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    draw.text((10, 20), "Display ON!", font=font, fill=255)
    disp.image(image)
    disp.display()

# Function to turn off the OLED
def turn_off_display():
    disp.command(0xAE)  # SSD1306_DISPLAYOFF

# Function to turn on the OLED
def turn_on_display():
    disp.command(0xAF)  # SSD1306_DISPLAYON

# Test OLED On/Off
try:
    print("Turning ON the OLED...")
    turn_on_display()
    show_display()
    time.sleep(5)  # Keep display ON for 5 seconds

    print("Turning OFF the OLED...")
    turn_off_display()
    time.sleep(5)  # OLED remains OFF for 5 seconds

    print("Turning ON the OLED again...")
    turn_on_display()
    show_display()
except KeyboardInterrupt:
    pass
finally:
    disp.clear()
    disp.display()
