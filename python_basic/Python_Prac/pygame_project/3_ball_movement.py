import pygame
import os
########################################
# 기본 초기화 (반드시 해야하는 것)
pygame.init() 

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado pang!!!") # 게임 이름

# FPS
clock = pygame.time.Clock()
########################################

#1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치


#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 둬야함

# 캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = (screen_height) - (character_height + stage_height)

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# 무기는 한번에 여러발 발사
weapons = []

#무기 이동 속도
weapon_speed = 10

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, 9] #index 0,1,2,3 에 행당하는 값

# 공 들
balls = []

# 최초 발생하는 큰 공
balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50, # 공의 y좌표
    "image_idx" : 0, # 공의 이미지 인덱스
    "to_x": 3, # x축 이동방향, -3이면 왼쪽, 3이면 오른쪽
    "to_y" : -6, # y축 이동 방향,
    "init_sped_y": ball_speed_y[0] #y의 최초 속도
})


running = True 
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    
    if character_x_pos < 0 :
            character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
            
            
    # 무기 위치 조정
    # ex) (100, 200) -> (100, 180 -> 160 -> 140)
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올림
    # list = [[i[0], (i[1]-speed)] for i in list]
    
    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] >= 0 ]
    # if 조건 만족하는 애들만 [i[0], i[1]]리스트로 저장(0보다 작아지면 제외)
    
    # 공 현재 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["image_idx"]
        
        #(공 크기 정의)
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        # (가로)경계값처리 : 튕겨 나오는 효과
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] *= -1
            
        # (세로) 경계값 처리 : 튕기는 효과
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_sped_y"]  #스테이지에 튕겨져 올라가는 처리
        else : #그 외에는 모든 경우에 속도가 증가
            ball_val["to_y"] += + 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    
    # 4. 충돌처리

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    for cur_weapon_x_pos, cur_weapon_y_pos in weapons:
        screen.blit(weapon, (cur_weapon_x_pos, cur_weapon_y_pos ))
        
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["image_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    

    
    pygame.display.update() 

pygame.quit()