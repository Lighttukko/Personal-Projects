
from sense_hat import SenseHat
import time

def show_welcome_screen():
    sense = SenseHat()
    sense.clear()
    lst_white = [3, 4, 11, 12, 15+4, 15+5, 23+3, 23+4, 23+5, 23+6, 31+3, 31+4, 31+5, 31+6, 31+8+4, 31+8+5, ]
    lst_fuel = [55+4, 55+5]
    lst_stars = [1, 8, 22, 33, 39]
    welcome_message = "Welcome to spacecraft game!"
    white_color = (255, 255, 255) # White
    red_color = (255, 0, 0) # Red
    yellow_color = (255, 255, 0) # Yellow
    blue_color = (0, 0, 255) # blue
    for x in lst_white:
        sense.set_pixel(x//8, x%8, white_color)
        time.sleep(0.04)

    for x in range(10):
        
        for y in lst_fuel:
            sense.set_pixel(y//8, y%8, red_color)
        time.sleep(0.04)
        for y in lst_fuel:
            sense.set_pixel(y//8, y%8, (0, 0, 0))
        time.sleep(0.04)
    for y in lst_fuel:
            sense.set_pixel(y//8, y%8, red_color)
    time.sleep(1)
    for y in lst_fuel:
            sense.set_pixel(y//8, y%8, (0, 0, 0))
    
    for y in range(4):
        for x in lst_stars:
            sense.set_pixel(y+x//8, x%8, yellow_color)
            
        time.sleep(0.5)
        
        for x in lst_stars:
            sense.set_pixel(y+x//8, x%8, (0, 0, 0))
    

    time.sleep(2.2)
    sense.clear()
    
    sense.show_message(welcome_message, text_colour=blue_color, scroll_speed = 0.05)

    sense.clear()

if __name__ == "__main__":
    show_welcome_screen()
