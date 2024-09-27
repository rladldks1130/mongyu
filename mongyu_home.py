import pygame
import mongyu_img as img
import mongyu_btn as btn
import mongyu_trigger as trigger

def home(screen, event):
	screen.blit(img.home_bg, (0,0))
	btn.setting_btn.draw(screen)
	btn.save_btn.draw(screen)
	btn.new_btn.draw(screen)

	if btn.setting_btn.click(event):
		trigger.homeOn = False
		trigger.settingOn = True
	
	if btn.save_btn.click(event):
		trigger.homeOn = False
		trigger.saveOn = True
	
	if btn.new_btn.click(event):
		trigger.homeOn = False
		trigger.newOn = True

def setting(screen, event):
	screen.blit(img.setting_bg, (0,0))

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			trigger.homeOn = True
			trigger.settingOn = False

def save(screen, event):
	screen.blit(img.save_bg, (0,0))
	
	# 테스트용 나중에 이어하기 연결하면 지울것
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			trigger.homeOn = True
			trigger.saveOn = False

def new(screen, event):
	screen.blit(img.new_bg, (0,0))
	
	# 테스트용 나중에 새로하기 연결하면 지울것
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			trigger.homeOn = True
			trigger.newOn = False






	
