import time
from sense_hat import SenseHat

def acceleromater():
    sense = SenseHat()
    sense.clear()
    structure = sense.get_pixels()
    counter = 0
    lst = []

    while True:
        acceleration = sense.get_accelerometer_raw()
        x, y, z = acceleration['x'], acceleration['y'], acceleration['z']
        lst.append((x, y, z))

        if abs(round(x, 4)) + abs(round(y, 4)) + abs(round(z, 4)) > 2:
            print(counter)
            counter += 1  
            sense.set_pixel((counter-1)//8, (counter-1)%8, (0, 255, 0))

        else:
            if counter > 0:
                sense.set_pixel((counter-1)//8, (counter-1)%8, (0, 0, 0))
                counter -= 1
                

        if counter == 64:
            time.sleep(1)
            for x in range(10):
                sense.clear((255, 255, 0))
                time.sleep(0.2)
                sense.clear()
                time.sleep(0.2)
            time.sleep(1)
            sense.clear()
            sense.show_message("Solar energy received", scroll_speed = 0.05)
            break

                    
            

        
        time.sleep(0.07)

        
if __name__ == "__main__":
    acceleromater()
    
