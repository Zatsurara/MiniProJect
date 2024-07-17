from PIL import Image, ImageGrab
import os
import time
from numpy import *

class Mybot():
    def __init__(self):
        self.grab = ImageGrab
        self.mainpath = os.path.dirname(__file__)
        self.pathphoto = os.path.join(self.mainpath, "photo")

        # ตรวจสอบและสร้างโฟลเดอร์ photo ถ้าไม่มี
        if not os.path.exists(self.pathphoto):
            os.makedirs(self.pathphoto)

        self.box = ()

    def Grab_img(self):
        # จับภาพหน้าจอ
        img = self.grab.grab()
        img.save(f"{self.pathphoto}/xxxx.jpg")

bot = Mybot()
bot.Grab_img()