from webbrowser import BackgroundBrowser
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game:")

# 배경 이미지 불러오기
background = pygame.image.load("/Users/bh_chae/hello_world/Python_Prac/pygame_basic/Rectangle 2392.png")

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트
            ruuning = False

    # screen.fill((0,0,255))
    screen.blit(background, (0,0))#배경 그리기

    pygame.display.update() # 게임화면 다시 그리기!


#pygame 종료
pygame.quit()