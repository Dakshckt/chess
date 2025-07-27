import pygame

white = (245,245,245)
black = (50,50,50)

def boardDsiplay(WIN):
    global boardVar , choiceColor
    for i in range(0 , 8):
        if i % 2 !=  0:
            choiceColor = False
        else:
            choiceColor = True
        for j in range(0 , 8):
            if choiceColor:
                use = white
                choiceColor = False
            else:
                use = black
                choiceColor = True
            pygame.draw.rect(WIN , use , (50 * j , 50 * i , 50 , 50))
    boardVar = False