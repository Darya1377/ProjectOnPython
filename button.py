import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initializes button's attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Initializing button's sizes and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        #Building rect object button and alignment by center of screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #Message of the button creates only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Makes msg rectangular and aligns text by the center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Empty button and message print
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)