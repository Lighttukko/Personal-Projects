from sense_hat import SenseHat
import time
import random

def show_loading_screen():
    sense = SenseHat()
    colors = [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (255, 255, 255)  # White
        ]

    sense.clear()
    structure = sense.get_pixels()

    counter = 0
    pixels = [x for x in range(64)]
    
    while counter < 64:
        index = random.randint(0,6)
        color = colors[index]
        try:
            j = pixels.pop(random.randint(0, len(pixels)-1))
            
        except ValueError:
            pass
        
        sense.set_pixel(j//8, j%8, color)
        time.sleep(0.1-(counter//8)/100)
        counter+=1

    time.sleep(0.3)
    sense.clear(255, 255, 255)
    time.sleep(2)
    sense.clear()

if __name__ == "__main__":
    show_loading_screen()
