import pygame
import os

# 載入圖片
menu = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
btn_upgrade = pygame.image.load(os.path.join("images", "upgrade.png"))
btn_sell = pygame.image.load(os.path.join("images", "sell.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(menu, (200, 200))
        self.upgrade_image = pygame.transform.scale(btn_upgrade, (60, 40))
        self.sell_image = pygame.transform.scale(btn_sell, (40, 40))
        self.rect_menu = self.menu_image.get_rect()
        self.rect_menu.center = (x, y)
        self.rect_upgrade =  self.upgrade_image.get_rect()
        self.rect_upgrade.center = (x, y-72)
        self.rect_sell = self.sell_image.get_rect()
        self.rect_sell.center = (x, y+75)
        self.__buttons = [Button(self.upgrade_image, "upgrade", self.rect_upgrade.centerx, self.rect_upgrade.centery),
                          Button(self.sell_image, "sell", self.rect_sell.centerx, self.rect_sell.centery)]  
        
    def draw(self, win):
        # draw menu
        win.blit(self.menu_image,self.rect_menu)
        # draw button
        win.blit(self.sell_image,self.rect_sell)
        win.blit(self.upgrade_image,self.rect_upgrade)

    def get_buttons(self):
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.rect_btn = image.get_rect()
        self.rect_btn.center = (x, y)
        
    def clicked(self, x, y):
        # 如果滑鼠點到按鈕，回傳True
        if(self.rect_btn.collidepoint(x, y) == True):
            return True
        else:
            return False

    def response(self):
        # 回傳按到的按鈕名字
        return self.name
        






