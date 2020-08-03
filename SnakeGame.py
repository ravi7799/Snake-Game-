import pygame
import random
import sys
import os

x=pygame.init()

# For adding audio file..
pygame.mixer.init()
pygame.mixer.pre_init(44100,-16,2,512)



#creating colors
white=(0,0,0)
grey=(170,170,170)
black=(20,20,20)
red=(255,0,0)
green=(0,255,100,0.2)
lightgreen=(0,128,0)
darkgreen=(18, 77, 40)
blue=(0,0,255)
fushia=(255,0,255)
yellow=(255,255,0)
pink=(196, 71, 142)
lightpurple=(55, 37, 143)
welcomegreen=(2, 71, 59)
gameovercol=(41, 6, 22)
lightyellow=(207, 191, 17)
maincolor=(0, 26, 18)



#creating game window
# width=600 & height=400
gameWindow=pygame.display.set_mode((600,400))
pygame.display.set_caption("SNAKES VIPER")
pygame.display.update()



####### A FILE THAT STORES HIGSCORE IS ATTACHED IN THE FOLDER WITH GAME


# To Print Score on Screen
def text_screen(text,color,x,y):
    font=pygame.font.SysFont(text,30)
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#For Heading
def heading(text,color,x,y):
    font=pygame.font.SysFont(text,45)
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


# To increase size of snake....
def plot_snake(gameWindow , color,snake_list,snakeSize):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snakeSize,snakeSize])


#Welcome screen...

def welcomescreen():
    welcomebg=pygame.image.load("homeBG1.jpg")
    welcomebg=pygame.transform.scale(welcomebg,(600,400)).convert_alpha()
    snakeimg=pygame.image.load("snake2.jfif")
    snakeimg=pygame.transform.scale(snakeimg,(100,100)).convert_alpha()
    exitgame=False
    pygame.mixer.music.load("HomeScreen.mp3")
    pygame.mixer.music.play(-1)
    while not exitgame:
        gameWindow.fill(welcomegreen)
        gameWindow.blit(welcomebg,(0,0))
        gameWindow.blit(snakeimg,(250,70))
        heading(" WELCOME TO SNAKE SMACKDOWN ",grey,20,200)
        text_screen("press SPACEBAR to play...", lightyellow, 20, 370)
        text_screen("press Q to quit...", pink, 20, 340)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
                if event.key==pygame.QUIT:
                    exitgame=True
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
        
        clock=pygame.time.Clock()
        clock.tick(30)
    pygame.quit()

            
        
        
        

#game loop
def gameloop():
    #creating game Specific
    gameExit=False
    gameOver=False
    
    # MAZE specifications
    mazel=30
    mazer=560
    mazetop=40
    mazebottom=350
    mazeblocksize=10
    
    # Snake Specification
    snakeX=50
    snakeY=100
    velocityX=0
    velocityY=0
    initialVelocity=10
    snakeSize=10
    
    # Food Specification
    food_sizeX=10
    food_sizeY=10
    foodX=random.randrange(mazel+5,mazer-5,5)
    foodY=random.randrange(mazetop+5,mazebottom-5,5)
    clock=pygame.time.Clock()
    fps=30
    
    
    #Special food Specification
    sfoodsizeX=20
    sfoodsizeY=20
    sfoodX=random.randrange(mazel+5,mazer-5,5)
    sfoodY=random.randrange(mazetop+5,mazebottom-5,5)
    count=0
    
    
    #Score of the player
    score=0
    

    
    # To increase the length of snake
    snake_list=[]
    snake_len=1
    head=[]
            
    # Making background for main game screen..
    mainbg=pygame.image.load("gamebg.JPG")
    mainbg=pygame.transform.scale(mainbg,(600,400)).convert_alpha()
    
    
    # Making background for game over screen..
    gameoverbg=pygame.image.load("homebg.jpg")
    gameoverbg=pygame.transform.scale(gameoverbg,(600,400)).convert_alpha()
    
    # File operation for storing highest score
    
    # If file does not exists....
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt",'w') as f:
            f.write("HIGHSCORE : 000000")
    file=open("highscore.txt",'r')
    highs=file.read()
    file.close()
    highscore=int(highs[-6:])
    pygame.mixer.music.load("backmain.mp3")
    pygame.mixer.music.play(-1)     
    
    eatsound = pygame.mixer.Sound("eat.mp3")
    
    # main game loop
    while not gameExit:
        if gameOver:
            gameWindow.fill((64, 82, 163))
            gameWindow.blit(gameoverbg,(0,0))
            heading("GAME OVER", gameovercol, 200, 170)
            text_screen("Press Q to quit...", blue,20, 310)
            text_screen("Press SPACE to continue playing...", lightyellow,20, 340)
            text_screen("Press ENTER to reach Home Screen...", lightpurple ,20, 370)
            
            for event in pygame.event.get():        
                if event.type==pygame.QUIT:        # To make user exit the game ..anytime they wants...
                    gameExit=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        gameloop()
                    
                    if event.key==pygame.K_RETURN:
                        welcomescreen()
                
                    if event.key==pygame.K_q:
                        pygame.quit()
                        sys.exit(0)
        else:
            for event in pygame.event.get():        
                if event.type==pygame.QUIT:        # To make user exit the game ..anytime they wants...
                    gameExit=True
                              
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocityX=initialVelocity
                        velocityY=0
                
                    if event.key==pygame.K_LEFT:
                        velocityX=-initialVelocity
                        velocityY=0
        
                    if event.key==pygame.K_UP:
                        velocityY=-initialVelocity
                        velocityX=0
        
                    if event.key==pygame.K_DOWN:
                        velocityX=0
                        velocityY=initialVelocity
                    # Cheat to increase your score :-P
                    if event.key==pygame.K_a:
                        score+=10
                
            snakeX=snakeX + velocityX
            snakeY=snakeY + velocityY
               
            
            # Setting the main game window color 
            gameWindow.fill(maincolor)
            gameWindow.blit(mainbg,(0,0))
            
            if count%5 != 0 or count==0:
                pygame.draw.rect(gameWindow,red,[foodX,foodY,food_sizeX,food_sizeY])
                if(abs(snakeX-foodX)<10 and abs(snakeY-foodY)<10):
                    score+=10
                    eatsound.play()
                    foodX=random.randrange(mazel+5,mazer-5,5)
                    foodY=random.randrange(mazetop+5,mazebottom-5,5)
                    snake_len+=1
                    count+=1
                    
            else:
                pygame.draw.rect(gameWindow,lightpurple ,[sfoodX,sfoodY,sfoodsizeX,sfoodsizeY])
                if(abs(snakeX-sfoodX)<20 and abs(snakeY-sfoodY)<20):
                    score+=30
                    sfoodX=random.randrange(mazel+5,mazer-5,5)
                    sfoodY=random.randrange(mazetop+5,mazebottom-5,5)
                    snake_len+=1
                    count+=1
                
                
            # Updating high score on screen
            if(highscore < score):
                highscore=score

            
            text_screen("SCORE:"+str(score)+"       HIGHSCORE:"+str(highscore),green,160,0)
            
            
            # This is for the initial condition when snake size was 1
            head=[]
            head.append(snakeX)
            head.append(snakeY)
            snake_list.append(head)
            
            
            if(len(snake_list) > snake_len):
                del(snake_list[0])
            
            if(head in snake_list[:-1]) or (snakeX<=mazel or snakeY<mazetop or snakeX>mazer or snakeY>mazebottom):
                gameOver=True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                if(highscore <= score):
                    file=open("highscore.txt",'w')
                    s=highs[:-7]+" {0:06d}".format(score)
                    file.write(s)
                    file.close()
                
                    
            plot_snake(gameWindow,lightgreen , snake_list, snakeSize)
            # Making a MAZE
            for i in range(30,561,20):
                pygame.draw.rect(gameWindow,darkgreen,[i,30,mazeblocksize, mazeblocksize ])
                pygame.draw.rect(gameWindow,pink,[i+10,30,mazeblocksize, mazeblocksize ])
            for j in range(30,370,20):
                pygame.draw.rect(gameWindow,darkgreen,[30,j,mazeblocksize, mazeblocksize ])
                pygame.draw.rect(gameWindow,pink,[30,j+10,mazeblocksize, mazeblocksize ])
            for i in range(30,561,20):
                pygame.draw.rect(gameWindow,darkgreen,[i,360,mazeblocksize, mazeblocksize ])
                pygame.draw.rect(gameWindow,pink,[i+10,360,mazeblocksize, mazeblocksize ])
            for j in range(30,370,20):
                pygame.draw.rect(gameWindow,darkgreen,[570,j,mazeblocksize, mazeblocksize ])
                pygame.draw.rect(gameWindow,pink,[570,j+10,mazeblocksize, mazeblocksize ])
            
           
                
        pygame.display.update()
        clock.tick(fps)
    
    #to stop game
    pygame.quit()
    sys.exit(0)


if __name__=='__main__':
    welcomescreen()