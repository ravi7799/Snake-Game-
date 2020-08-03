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
game_icon=pygame.image.load('icon\icon.png')
pygame.display.set_icon(game_icon)
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
def plot_snake(gameWindow ,count ,snake_list,snakeSize,snaketype):
    count=0
    
    if snaketype==1:
        for x,y in snake_list:
            if count%2==0:
                pygame.draw.rect(gameWindow,green,[x,y,snakeSize,snakeSize])
            else:
                pygame.draw.rect(gameWindow,(22, 171, 77),[x,y,snakeSize,snakeSize])
            count+=1
            
    if snaketype==2:
        for x,y in snake_list:
            if count%2==0 or count<=3:
                pygame.draw.rect(gameWindow,(255,250,250),[x,y,snakeSize,snakeSize])
            else:
                pygame.draw.rect(gameWindow,(162, 224, 178),[x,y,snakeSize,snakeSize]) 
            if count%2==1 and count>=3:
                pygame.draw.rect(gameWindow,(0, 0, 0),[x+snakeSize/2,y,snakeSize/2,snakeSize/2]) 
            count+=1
            
    if snaketype==5:
        for x,y in snake_list:
            if count%2==0:
                pygame.draw.rect(gameWindow,(168, 110, 39),[x,y,snakeSize,snakeSize])
            else:
                pygame.draw.rect(gameWindow,(168, 110, 39),[x,y,snakeSize,snakeSize])
            if count%2==1:
                pygame.draw.rect(gameWindow,(92, 52, 4),[x,y,snakeSize/2,snakeSize/2])
            count+=1
            
    if snaketype==4:
        for x,y in snake_list:
            if count%2==0:
                pygame.draw.rect(gameWindow,(61, 186, 153),[x,y,snakeSize,snakeSize])
            else:
                pygame.draw.rect(gameWindow,(61, 186, 153),[x,y,snakeSize,snakeSize])
            if count%2==1:
                pygame.draw.rect(gameWindow,(22, 171, 77),[x,y,snakeSize/2,snakeSize/2])
            count+=1

            
    if snaketype==3:
        for x,y in snake_list:
            if count%2==0:
                pygame.draw.rect(gameWindow,(105, 35, 148),[x,y,snakeSize,snakeSize])
            else:
                pygame.draw.rect(gameWindow,(189, 132, 224),[x,y,snakeSize,snakeSize])
            if count%2==1:
                pygame.draw.rect(gameWindow,(22, 171, 77),[x+snakeSize/2,y,snakeSize/2,snakeSize/2])
            count+=1

#Welcome screen...

def welcomescreen():
    welcomebg=pygame.image.load("images\homeBG1.jpg")
    welcomebg=pygame.transform.scale(welcomebg,(600,400)).convert_alpha()
    snakeimg=pygame.image.load("images\snake2.jfif")
    snakeimg=pygame.transform.scale(snakeimg,(100,100)).convert_alpha()
    exitgame=False
    pygame.mixer.music.load("music\HomeScreen.mp3")
    pygame.mixer.music.play(-1)
    while not exitgame:
        gameWindow.fill(welcomegreen)
        gameWindow.blit(welcomebg,(0,0))
        gameWindow.blit(snakeimg,(250,70))
        heading(" WELCOME TO SNAKE SMACKDOWN ",grey,20,200)
        text_screen("1. press SPACEBAR to PLAY", lightyellow, 170, 250)
        text_screen("3. press Q to QUIT", pink, 170, 310)
        text_screen("2. press S to to SELECT snake", green, 170, 280)
        text_screen("4. press H for HELP", (13, 189, 168), 170, 340)
        main_screen("@RAVEET_K", (199, 10, 111), 500, 380)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop(1)
                if event.key==pygame.QUIT:
                    exitgame=True
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
                if event.key==pygame.K_s:
                    snaketypescreen()
                if event.key==pygame.K_h:
                    helpscreen()
        
        clock=pygame.time.Clock()
        clock.tick(30)
    pygame.quit()


# function for Selecting Type Of Snake....
def snaketypescreen():
    welcomebg=pygame.image.load("images\homeBG1.jpg")
    welcomebg=pygame.transform.scale(welcomebg,(600,400)).convert_alpha()
    snake1=pygame.image.load("icon\snake.png")
    snake1=pygame.transform.scale(snake1,(60,60)).convert_alpha()
    snake2=pygame.image.load("icon\snake1.jfif")
    snake2=pygame.transform.scale(snake2,(60,60)).convert_alpha()
    snake3=pygame.image.load("icon\snake2.png")
    snake3=pygame.transform.scale(snake3,(60,60)).convert_alpha()
    snake4=pygame.image.load("icon\snake3.png")
    snake4=pygame.transform.scale(snake4,(60,60)).convert_alpha()
    snake5=pygame.image.load("icon\snake4.png")
    snake5=pygame.transform.scale(snake5,(60,60)).convert_alpha()
    exitgame=False
    pygame.mixer.music.load("music\HomeScreen.mp3")
    pygame.mixer.music.play(-1)
    while not exitgame:
        gameWindow.fill(welcomegreen) 
        gameWindow.blit(welcomebg,(0,0))       
        heading(" WELCOME TO SNAKE SMACKDOWN ",(230, 250, 230),20,20)
        heading("1. Press 1",(34, 153, 8), 210, 70)
        gameWindow.blit(snake1,(380,55))
        heading("2. Press 2", (235,245,250), 210, 130)
        gameWindow.blit(snake2,(380,115))
        heading("3. Press 3", (106, 35, 173), 210, 180)
        gameWindow.blit(snake3,(380,159))
        heading("4. Press 4", (19, 207, 172), 210, 240)
        gameWindow.blit(snake4,(380,225))
        heading("5. Press 5", (204, 214, 19), 210, 300)   
        gameWindow.blit(snake5,(380,280))
        
        text_screen("Press Q to quit...", pink, 0,380)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    gameloop(1)
                
                if event.key==pygame.K_2:
                    gameloop(2)
                
                if event.key==pygame.K_3:
                    gameloop(3)
                
                if event.key==pygame.K_4:
                    gameloop(4)
                
                if event.key==pygame.K_5:
                    gameloop(5)
                    
                if event.key==pygame.QUIT:
                    exitgame=True
                
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
        
        clock=pygame.time.Clock()
        clock.tick(30)
    pygame.quit()
        

# HELP Screen
    
def helpscreen():
    exitgame=False
    pygame.mixer.music.load("music\help.mp3")
    pygame.mixer.music.play(-1)
    while not exitgame:
        gameWindow.fill((95, 199, 173))
        heading(" WELCOME TO SNAKE SMACKDOWN ",(12, 34, 133),20,20)
        text_screen("1. Snake will automatically move,just change direction:",(153, 12, 90), 0, 70)    
        main_screen("* -> key to move right", (207, 105, 37), 20, 90)
        main_screen("* <- key to move left", (106, 35, 173), 20, 113)
        main_screen("* ^ key to move up", (29, 88, 196), 20, 136)
        main_screen("* v key to move down", (40, 105, 2), 20, 160)
        text_screen("2. score will be addded according to :",(153, 12, 90), 0, 200)
        main_screen("* 10 points for eating cheese", (29, 88, 196), 20, 230)
        main_screen("* 30 points for eating meat", (40, 105, 2), 20, 253)
        text_screen("3. Credit :",(153, 12, 90), 0, 276)
        main_screen("* RAVEET KUMAR ", (207, 105, 37), 20, 306)
        main_screen("* kumarraveet52@gmail.com", (106, 35, 173), 20, 330)
        text_screen("Press Q to QUIT...", (148, 25, 3), 0,380)
        text_screen("Press H to HOME_SCREEN...", (148, 25, 3), 0,360)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
                if event.key==pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.key==pygame.K_h:
                    welcomescreen()
        clock=pygame.time.Clock()
        clock.tick(30)
    pygame.quit()



def main_screen(text,color,x,y):
    font=pygame.font.SysFont(text,23)
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


# Pause screen feature
def pause():
    done=True
    while done:
        heading("PAUSED",(126, 224, 198),230,185)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    done=False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit(0)
                if event.key== pygame.K_h:
                    welcomescreen()
        clock=pygame.time.Clock()
        clock.tick(30)



#game loop
     # TO GIVE USER THE OPTION TO SELECT TYPE OF SNAKE
def gameloop(snaketype):
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
    foodX=random.randrange(mazel+5,mazer-5,5)
    foodY=random.randrange(mazetop+5,mazebottom-5,5)
    clock=pygame.time.Clock()
    fps=30
    
    
    #Special food Specification
    sfoodX=random.randrange(mazel+5,mazer-5,5)
    sfoodY=random.randrange(mazetop+5,mazebottom-5,5)
    count=0
    
    smallfood=pygame.image.load("images\cheese.png")
    smallfood=pygame.transform.scale(smallfood,(15,15)).convert_alpha()
    bigfood=pygame.image.load("images\meat.png")
    bigfood=pygame.transform.scale(bigfood,(25,25)).convert_alpha()

    
    #Score of the player
    score=0
    

    
    # To increase the length of snake
    snake_list=[]
    snake_len=1              
    head=[]
            
    # Making background for main game screen..
    mainbg=pygame.image.load("images\gamebg.JPG")
    mainbg=pygame.transform.scale(mainbg,(600,400)).convert_alpha()
    
    
    # Making background for game over screen..
    gameoverbg=pygame.image.load("images\homebg.jpg")
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
    
    
    
    pygame.mixer.music.load("music\\backmain.mp3")
    pygame.mixer.music.play(-1)     
    
    eatsound = pygame.mixer.Sound("sound\\beep.wav")
    
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
                        gameloop(1)
                    
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
                    
                    if event.key==pygame.K_q:
                        pygame.quit()
                        sys.exit(0)
                   
                    if event.key==pygame.K_h:
                        welcomescreen()
                    
                    if event.key==pygame.K_p:
                        pause()
                
            snakeX=snakeX + velocityX
            snakeY=snakeY + velocityY
               
            
            # Setting the main game window color 
            gameWindow.fill(maincolor)
            gameWindow.blit(mainbg,(0,0))
            main_screen("Press P to PAUSE...", (16, 146, 163), 190,380)
            main_screen("Press Q to QUIT...", (16, 146, 163), 0,380)
            main_screen("Press H to HOME_SCREEN", (219, 187, 149), 400,380)
            
            if count%5 != 0 or count==0:
                gameWindow.blit(smallfood,(foodX,foodY))
                if(abs(snakeX-foodX)<15 and abs(snakeY-foodY)<15):
                    score+=10
                    eatsound.play()
                    foodX=random.randrange(mazel+5,mazer-5,5)
                    foodY=random.randrange(mazetop+5,mazebottom-5,5)
                    snake_len+=1
                    count+=1
                    
            else:
                gameWindow.blit(bigfood,(sfoodX,sfoodY))
                if(abs(snakeX-sfoodX)<20 and abs(snakeY-sfoodY)<20):
                    score+=30
                    eatsound.play()
                    sfoodX=random.randrange(mazel+5,mazer-5,5)
                    sfoodY=random.randrange(mazetop+5,mazebottom-5,5)
                    snake_len+=1
                    count+=1
            
                
            # Updating high score on screen
            if(highscore < score):
                highscore=score

            
            text_screen("SCORE:"+str(score)+"       HIGHSCORE:"+str(highscore),(255, 204, 255),160,0)
            
            
            # This is for the initial condition when snake size was 1
            head=[]
            head.append(snakeX)
            head.append(snakeY)
            snake_list.append(head)
            
            
            if(len(snake_list) > snake_len):
                del(snake_list[0])
            
            if(head in snake_list[:-1]) or (snakeX<=mazel or snakeY<mazetop or snakeX>mazer or snakeY>mazebottom):
                gameOver=True
                pygame.mixer.music.load("music\gameover.mp3")
                pygame.mixer.music.play()
                if(highscore <= score):
                    file=open("highscore.txt",'w')
                    s=highs[:-7]+" {0:06d}".format(score)
                    file.write(s)
                    file.close()
                
                    
            
            plot_snake(gameWindow,count, snake_list, snakeSize, snaketype)
        
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