import time
import subprocess
import netifaces
from read_json_file import load_automata

 
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

font = ImageFont.truetype('PibotoCondensed-Regular',10)
font_heading = ImageFont.truetype('PibotoCondensed-Regular.ttf', 18)
font_ip = ImageFont.truetype('PibotoCondensed-Regular.ttf', 12)


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

        draw.text((0, 16*zeile+8), net + ": " + ip, font=font_ip, fill=255)
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
    
def oled_off():
    # Leeres Display.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    disp.show()
    
def show_status_before(am: dict, inp: str, cur_st: int):
    states, transitions = load_automata(am)
    # Leeres Display.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    disp.show()
    draw.text((0, 0), "Aktueller Zustand: " + str(cur_st), font=font, fill=255)
    draw.text((0, 8), "Input: " + str(inp), font=font, fill=255)
    x_c = 0
    y_c = 16

    if inp in transitions[states[cur_st]]:
        for i in transitions[states[cur_st]][inp]["Output"]:
            draw.text((x_c, y_c), i, font=font, fill=255)
            x_c += 60
            if x_c > 80:
                x_c = 0
                y_c += 8

    disp.image(image)
    disp.show()

def show_status_after(cur_st: int):

    draw.text((0, 48), "Neuer Zustand: " + str(cur_st), font=font, fill=255)
    disp.image(image)
    disp.show()

def start_display():
    
    # Clear display.
    disp.fill(0)
    disp.show()

    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    disp.show()
    time.sleep(.5)

    draw.rectangle((width/6, 22, width/6+width/4, height), outline=1, fill=1)
    bx1 = 46
    bx2 = 49
    by1 = 45
    by2 = 48
    ba = 7
    draw.rectangle((width/6+2, 24, (width/3-2), height-16), outline=0, fill=0)
    draw.rectangle((width/6+2, height-12, (width/3-2), height-2), outline=0, fill=0)
    draw.ellipse((bx1,by1,bx2,by2), outline=0, fill=0)
    draw.ellipse((bx1,by1-ba,bx2,by2-ba), outline=0, fill=0)
    draw.ellipse((bx1,by1-2*ba,bx2,by2-2*ba), outline=0, fill=0)

    lx1 = 47
    lx2 = 48
    ly1 = 28
    ly2 = 29
    la = 3
    draw.ellipse((lx1,ly1,lx2,ly2), outline=0, fill=0)
    draw.ellipse((lx1-la,ly1,lx2-la,ly2), outline=0, fill=0)
    draw.ellipse((lx1+la,ly1,lx2+la,ly2), outline=0, fill=0)

    draw.rectangle((lx1-1,50,lx2,55), outline=1, fill=0)

    disp.image(image)
    disp.show()
    time.sleep(.5)

    draw.text((20, 2), "SCHOKOMAT", font=font_heading, fill=255, size=22)
    draw.text((95, 22), "2.0", font=font_heading, fill=255)

    disp.image(image)
    disp.show()
