import pygame 
import sys
import random
from time import sleep

vl= [5, 10, 15, 20, 25, 30, 35] #x 축 속도 임의 지정
v = random.choice(vl) # x 축 속도 임의 지정

padWidth = 1550 
padHeight = 800
rockImage = ['images/rock02.png'] #파란공 1
rock2Image = ['images/rock03.png'] #파란공 2
WIN = pygame.display.set_mode((padWidth, padHeight))
BLACK = (0, 0, 0)
lneobImage = ['images/line.png'] #기준면 선

h= 0.64 #1픽셀 당 1cm #높이
g= 9.80665 #중력가속도 상수

#게임에 등장하는 객체 드로잉
def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))


def initGame():
    global gamePad, clock,background, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight)) #게임 화면 크기 
    pygame.display.set_caption('Gravity compare') #게임이름
    background = pygame.image.load('images/background3.png') #배경그림
    pygame.mixer.music.load('musics/music.wav') #배경노래
    pygame.mixer.music.play(-1) 

def runGame():
    global gamdPad, clock, background, gameOverSound, v, lneOb
    clock = pygame.time.Clock() #시간 설정
    rock = pygame.image.load(random.choice(rockImage)) #공 1
    rock2 = pygame.image.load(random.choice(rock2Image)) #공2
    rockSize = rock.get_rect().size #공 크기
    timestep = 0
    updated_points = [] #따라오는 선 위치
    updated2_points = [] #따라오는 선 위치
    rockX = 0 #공1 초기 위치 설정
    rockY = 0 #공1,공2 초기 위치 설정
    rock2X = 0 #공2 초기 위치 설정

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: #게임프로그램 종료
                pygame.quit()
                sys.exit()
        timestep +=1 #기준 시간
        drawObject(background,0,0) #배경화면그리기
        clock.tick(60) #시간 설정
        rockSpeed = 2**(1/3)*g*h*(timestep/10) #루트2gh x 시간
        rockX += v #x속력
        rockY += rockSpeed #운석 아래로 움직임
        updated_points.append((rockX+35, rockY+20)) #따라오는 선
        updated2_points.append((rock2X + 35, rockY+20)) #따라오는 선
        print (rockSpeed) #공 속도 출력
        lneOb = pygame.image.load(random.choice(lneobImage)) #기준선 출력
        drawObject(lneOb ,0, padHeight - 72.2) #기준선 출력

        if rockY > padHeight -100:
            rock = pygame.image.load(random.choice(rockImage))
            rockX = 0 #초기 설정 복원
            rockY = 0 #초기 설정 복원
            timestep = 0 #초기 설정 복원
            updated_points=[] #초기 설정 복원
            updated2_points=[] #초기 설정 복원
            v = random.choice(vl) #초기 설정 복원
            sleep(2)
        drawObject(rock, rockX, rockY)
        drawObject(rock2, rock2X, rockY)

        if timestep >= 3:
            pygame.draw.lines(WIN, BLACK, False, updated_points, 2) #선 그리기
        if timestep >= 3:
            pygame.draw.lines(WIN, BLACK, False, updated2_points, 2) #선 그리기
        pygame.display.update() #게임화면 다시그림
        clock.tick(60) #게임화면 초당 프레임 수 60으로 설정

    pygame.quit() #게임종료

initGame()
runGame()
