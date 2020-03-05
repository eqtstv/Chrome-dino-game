from PIL import ImageGrab, ImageOps
import pyautogui as pya
import time
import numpy as np

# address: chrome://dino

class Bot:
    def __init__(self):
        self.restart_coords = (480, 503)
        self.dino_coords = (140, 475)
        self.area = (self.dino_coords[0] + 100, self.dino_coords[1],
                    self.dino_coords[0] + 160, self.dino_coords[1] + 5)
        self.i = 1

    def jump(self):
        pya.keyUp('down')
        pya.keyDown("space")
        time.sleep(0.105)
        pya.keyUp('space')
        pya.keyDown('down')
        self.speed_up()
        self.i += 1

    def restart(self):
        pya.click(self.restart_coords)
        pya.keyDown("down")

    def detection_area(self):
        image = ImageGrab.grab(self.area)
        gray_img = ImageOps.grayscale(image)
        img_arr = np.array(gray_img.getcolors())
        return img_arr.mean()
 
    def speed_up(self):
        list_area = list(self.area)
        if list_area[2] < 655:
            list_area[2] += 3
        self.area = tuple(list_area)

    def main(self):
        self.restart()
        while True:
            if self.detection_area() < 120:
                self.jump()



bot = Bot()
bot.main()        
