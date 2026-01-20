from sense_hat import SenseHat
import time
import random


def display_winning_screen():
    sense = SenseHat()
    sense.clear()
    
    
    winning_colors = [
        (255, 0, 0),    # Red
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 255, 255),  # Cyan
        (0, 0, 255),    # Blue
        (255, 0, 255),  # Magenta
        (255, 255, 255),  # White
    ]
    lst = []
    color_lst = [(0, 0, 0)]
    counter = 0
    record = 0
    while True:
        data = sense.get_orientation()
        roll, pitch, yaw = data['roll'], data['pitch'], data['yaw']
        lst += [yaw]
        


            
        if (lst[0] > 260 and lst[-1] < 30) or record:
            record += 1
            lst[-1] += 360


        if (lst[-1] - lst[0]) >= 75 and  (lst[-1] - lst[0]) <= 120:
            lst = [yaw]
            color = random.choice(winning_colors)
            while color == color_lst[-1]:
                color = random.choice(winning_colors)
            color_lst.append(color)
            sense.clear(color)
            counter += 1

        if counter == 4:
            sense.clear()
            break
            
            

        time.sleep(0.04)
        print(f"Roll: {roll:.2f} degrees, Pitch: {pitch:.2f} degrees, Yaw: {yaw:.2f} degrees", "counter:", counter)
        

    for x in range(50):
        color = random.choice(winning_colors)
        sense.clear(color)
        time.sleep(0.05-(x//15)/100)
    sense.clear((255, 255, 255))
    time.sleep(1)
    sense.show_message("YOU WIN!!!", text_colour = (0, 0, 255), scroll_speed= 0.05)

    sense.clear()

if __name__ == "__main__":
    display_winning_screen()
