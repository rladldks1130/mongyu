import pygame
import mongyu_img as img

class Button:
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect(topleft=(x, y))

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def click(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				return True
		return False

# 버튼객체 생성
setting_btn = Button(80, 300, img.setting_btn)
save_btn = Button(80, 400, img.save_btn)
new_btn = Button(80, 500, img.new_btn)