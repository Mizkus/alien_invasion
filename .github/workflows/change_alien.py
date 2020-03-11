import pygame.font

class Change_alien():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 120
        self.height = 30
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottom = self.screen_rect.bottom
        self.rect.right = self.screen_rect.right
        self.prep_msg(msg)
        

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.change_alien_rect = self.msg_image.get_rect()
        self.change_alien_rect = self.rect

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.change_alien_rect)