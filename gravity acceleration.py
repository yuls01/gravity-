import pygame #cmd창에서 pip install pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
rockImage = ['images/rock01.png']
WIN = pygame.display.set_mode((padWidth, padHeight))
BLACK = (0, 0, 0)

h= 0.64 #1픽셀 당 1cm 
g= 9.80665

def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))

def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20)
    text = font.render('기준면 도달 사과: ' + str(count),True,(0,0,0))
    gamePad.blit(text,(300,0))

def initGame():
    global gamePad, clock, background, pointline
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight)) #게임 화면 크기 
    pygame.display.set_caption('Gravity') #게임이름
    background = pygame.image.load('images/background2.png') #배경그림
    pointline = pygame.image.load('images/line.png')#선그림
    pygame.mixer.music.load('musics/music.wav')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()

def runGame():
    global gamdPad, clock, background, rockSpeed
    clock = pygame.time.Clock()
    #운석 랜덤생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size #운석크기
    rockWidth = rockSize[0]
    timestep = 0
    updated_points = []
    rockX = random.randrange(0, padWidth - rockWidth) 
    rockY = 0
    rockPassed = 0
    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: #게임프로그램 종료
                pygame.quit()
                sys.exit()
        timestep +=1
        drawObject(background,0,0) #배경화면그리기
        clock.tick(60)
        rockSpeed = 2**(1/3)*g*h*(timestep/10) #루트2gh x 시간
        rockY += rockSpeed #운석 아래로 움직임
        updated_points.append((rockX + 35, rockY))
        print (rockSpeed)

        if rockY > padHeight-30:
            rock = pygame.image.load(random.choice(rockImage))
            rock = pygame.image.load(random.choice(rockImage))
            rockX = random.randrange(0, padWidth - rockWidth) 
            rockY = 0 #꼭대기
            rockPassed += 1 
            timestep = 0
            updated_points=[]
            sleep(1)
        writePassed(rockPassed)
        drawObject(rock, rockX, rockY)
        if timestep >= 3:
            pygame.draw.lines(WIN, BLACK, False, updated_points, 2)
        pygame.display.update() #게임화면 다시그림
        clock.tick(60) #게임화면 초당 프레임 수 60으로 설정
    pygame.quit() #게임종료

initGame()
runGame()
