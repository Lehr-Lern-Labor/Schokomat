import board
import neopixel

pixel_pin = board.D18  # Pin
num_pixels = 18  # Pixelzahl
ORDER = neopixel.GRB  # Farbreihenfolge

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.4, auto_write=False, pixel_order=ORDER
)
def norm_lighting():
    pixels.fill((150, 150, 255))
    pixels.show()

def work_lighting():
    pixels.fill((200, 50, 0))
    pixels.show()

def check_lighting():
    pixels.fill((0, 255, 50))
    pixels.show()

def ledstrip_off():
    pixels.fill((0, 0, 0))
    pixels.show()
