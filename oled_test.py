import time
import subprocess
import netifaces
import urllib.request

 
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('PibotoCondensed-Regular',12)


def show_ipaddr():
    # Leeres Display.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    disp.show()

    net_list = netifaces.interfaces()
    zeile = 0
    for net in net_list:
        try:
            ip = netifaces.ifaddresses(net)[2][0]['addr']
        except:
            ip = "not connected"
    
        draw.text((0, 16*zeile+8), net + ": " + ip, font=font, fill=255)
        zeile += 1

    disp.image(image)
    disp.show()

def internet_test():
    try:
        with urllib.request.urlopen('https://kit.edu') as response:
            html = response.read()
            print(html)
    except Exception as e:
        print("Failed to fetch", e)

while True:
    show_ipaddr()
    internet_test()
    time.sleep(10)    
