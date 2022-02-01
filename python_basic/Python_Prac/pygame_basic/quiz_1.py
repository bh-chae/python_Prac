from random import randint
from turtle import back
import pygame
import os

########################################
# 기본 초기화 (반드시 해야하는 것)
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
########################################

#1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기

background = pygame.image.load(os.path.join(current_path, "Rectangle 2392.png"))

# 캐릭터 불러오기
character = pygame.image.load(os.path.join(current_path, "character.png"))

character_size = character.get_rect().size # 이미지 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) 
character_y_pos = (screen_height - character_height)

#떨어지는 비
raining = pygame.image.load(os.path.join(current_path, "Enemy.png"))

raining_size = raining.get_rect().size 
raining_width = raining_size[0]
raining_height = raining_size[1] 
raining_x_pos = randint(0, (screen_width - raining_width/2))
raining_y_pos = 0


# 이동할 좌표
to_x = 0
to_y = 0

rain_to_y = 5

# 이동 속도
character_speed = 0.6


running = True 
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                to_x -= character_speed 
            if event.key == pygame.K_RIGHT :
                to_x += character_speed 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
    character_x_pos += to_x * dt

    # 경계값 처리
    if character_x_pos < 0 : 
        character_x_pos =0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    
    # 3. 게임 캐릭터 위치 정의 (비 내림)
    if running == True : 
        raining_y_pos += rain_to_y
        if raining_y_pos >= screen_height :
            raining_y_pos = 0
            raining_x_pos = randint(0, (screen_width - raining_width/2))
        

    # 4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    raining_rect = raining.get_rect()
    raining_rect.left = raining_x_pos
    raining_rect.top = raining_y_pos

    if character_rect.colliderect(raining_rect):
        print("Crushed!!!!")
        running = False


    # 5. 화면에 그리기
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(raining, (raining_x_pos, raining_y_pos))
    pygame.display.update() 

pygame.quit()