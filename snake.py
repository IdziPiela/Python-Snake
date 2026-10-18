import time
import os


in_alive = True

snake_place_x = 25

snake_place_y = 3

def screen():
        print("X" * 50)
        for x in range(7):
            if x == snake_place_y:
                print("X" + " " * (snake_place_x-1) + "S" + " " * (48 - snake_place_x) + "X")
            else:
                print("X" + " " *48 + "X")
        print("X" * 50)



while in_alive:
    
    screen()
    snake_place_x = snake_place_x +1 
    snake_place_y = snake_place_y





    time.sleep (0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    
    