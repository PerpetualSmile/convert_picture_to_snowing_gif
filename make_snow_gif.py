import pygame
import random
import os
from PIL import Image
from pygame.sprite import Sprite
from pygame.sprite import Group
from PIL import ImageGrab
import shutil


# 表示单个雪花的类
class Snow(Sprite):
    def __init__(self, image, pos, speed, size, screen):
        super().__init__()
        self.screen = screen
        self.speed= speed
        self.pos = pos
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # 雪花旋转
        self.image = pygame.transform.rotate(self.image, 90)
        if self.check_edges():
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
        return False



def add_snow(path):
    pygame.init()
    size = Image.open(path).size
    screen = pygame.display.set_mode(size, pygame.NOFRAME)
    s = pygame.display.get_surface()

    bg = pygame.image.load_extended(path).convert()
    screen.blit(bg, (0, 0))

    # 加载雪花图片
    snow_image = pygame.image.load_extended('snow.png')
    snow_group = Group()


    for i in range(500):
        # 雪花起始位置
        pos = (random.randint(-size[0], size[0]), random.randint(-size[1], 0))

        # 控制雪花大小
        n = random.randint(4, 12)
        snow_size = (n, n)

        # 雪花下落速度
        speed = (2, random.randint(2, 7))
        snow_group.add(Snow(snow_image, pos, speed, snow_size, screen))

    clock = pygame.time.Clock()

    # 创建文件夹用于保存每一帧图片
    if not os.path.exists("frames"):
        os.makedirs("frames")

    flag = True
    num = 1;
    while flag:
        for event in pygame.event.get():
            # 退出窗口
            if event.type == pygame.QUIT:
                flag = False

        screen.blit(bg, (0, 0))
        for snow in snow_group.copy():
            snow.blitme()
        snow_group.update()

        # 保存当前画面
        pygame.image.save(screen, "frames\\"+str(num)+".jpg")


        # 刷新屏幕
        pygame.display.update()

        # 设置fps
        clock.tick(30)
        if num >= 250:
            break
        num += 1

    # 制作GIF图
    im = Image.open("frames\\1.jpg")
    images = []
    size = (int(im.size[0]/2), int(im.size[1]/2))
    for file in range(2, num + 1):
        filepath = "frames\\" + str(file) + ".jpg"
        temp = Image.open(filepath)
        temp = temp.resize(size, Image.ANTIALIAS)
        images.append(temp)

    im = im.resize(size, Image.ANTIALIAS)
    im.save('snow.gif', save_all=True, append_images=images, loop=2, duration=5)

    # 删除保存中间图片文件的文件夹
    shutil.rmtree("frames")



if __name__ == '__main__':
    add_snow('background.jpg')