import pygame
import mongyu_home as home

# 몽유 기본 세팅
pygame.init()
screen = pygame.display.set_mode((1100, 680))
pygame.display.set_caption("몽유 mongyu")
FPS = 60
clock = pygame.time.Clock()

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		home.home(screen)

		clock.tick(FPS)
		pygame.display.update()

if __name__ == "__main__":
	main()