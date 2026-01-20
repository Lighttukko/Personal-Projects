from sense_hat import SenseHat
import time
import random

def display_losing_screen():
    sense = SenseHat()
    losing_colors = [
        (255, 255, 255),  # White
        (255, 0, 0) # red
    ]
    lst = [1, 8, 10, 18, 25, 33+8]
    for x in range(30):
      x_coo = random.randint(0, 5)
      y_coo = random.randint(0, 2)
      new_lst = [y+x_coo + y_coo*8 for y in lst]
      
      for y in new_lst:
        sense.set_pixel(y%8, y//8, losing_colors[0])
        
      time.sleep(0.1)
      
      for y in new_lst:
        sense.set_pixel(y%8, y//8, (0, 0, 0))
        
    time.sleep(1)
    
    for x in range(20):
        color = losing_colors[x%2]
        sense.clear(color)
        time.sleep(0.02+((x//3)/30))
    sense.clear((255, 255, 255))
    time.sleep(0.3)
    sense.show_message("YOU LOST !!!", text_colour = (255, 0, 0), scroll_speed = 0.05)

    
    sense.clear()

if __name__ == "__main__":
    display_losing_screen()
