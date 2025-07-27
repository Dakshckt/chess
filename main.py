import tkinter.messagebox
import pygame
import os
from boardGenerate import boardDsiplay 
from peices import arrangePeices
from peices import *
from movement import *
import tkinter
from tkinter.messagebox import *

pygame.init()

WIDTH , HEIGHT = 400 , 500
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Chess Game")

boardVar = True
choiceColor = True
FPS = 60
options = []
asd = True
var = True
turn = 'white'

def main():
    global options
    global boardVar , var , asd , turn
    font = pygame.font.Font(None , 30)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if turn == 'white':
                    for val in white_peices:
                        if position[0] > val[1][0] and position[0] < val[1][0] + 50 and position[1] > val[1][1] and position[1] < val[1][1] + 50:
                            options = check(val , white_peices , black_peices)
                elif turn == 'black':
                    for val in black_peices:
                        if position[0] > val[1][0] and position[0] < val[1][0] + 50 and position[1] > val[1][1] and position[1] < val[1][1] + 50:
                            options = check(val , white_peices , black_peices)
                               
                for option in options:
                    pygame.draw.rect(WIN , (255,255,0) , option[1] , 5)
                
                for option in options:
                    if position[0] > option[1].x and position[0] < option[1].x + 50 and position[1] > option[1].y and position[1] < option[1].y + 50:
                        if turn == 'white' and option[0] in white_peices:
                            index_remove = None
                            index = white_peices.index(option[0])        
                            curr_surf , curr_posi = white_peices[index]
                            new_posi = (option[1].x + center_peices_pad , option[1].y + center_peices_pad)
                            white_peices[index] = (curr_surf , new_posi)  
                            for val in black_peices:
                                if val[1][0] == option[1].x + center_peices_pad and val[1][1] == option[1].y + center_peices_pad:
                                    index_remove = black_peices.index(val)
                                    # print("killed")
                                    break
                            if index_remove is not None:
                                # print(black_peices[index_remove])
                                # print(black_peices[index_remove][0])
                                if black_peices[index_remove][0] == black_king:
                                    tkinter.messagebox.showinfo("Completed","White Won")
                                    run = False
                                    break
                                del black_peices[index_remove]
                                index_remove = None
                            turn = 'black'

                        elif turn == 'black' and option[0] in black_peices:
                            index_remove = None
                            index = black_peices.index(option[0])             
                            curr_surf , curr_posi = black_peices[index]
                            new_posi = (option[1].x + center_peices_pad , option[1].y + center_peices_pad)
                            black_peices[index] = (curr_surf , new_posi)  
                            for val in white_peices:
                                if val[1][0] == option[1].x + center_peices_pad and val[1][1] == option[1].y + center_peices_pad:
                                    index_remove = white_peices.index(val)
                                    # print("Killed")
                                    break
                            if index_remove is not None:
                                # print(white_peices[index_remove])
                                # print(white_peices[index_remove][0])
                                if white_peices[index_remove][0] == white_king:
                                    tkinter.messagebox.showinfo("Completed","Black Won")
                                    run = False
                                    break
                                del white_peices[index_remove]
                                index_remove = None
                            turn = 'white'

                if turn == 'white':
                    text = font.render("White Turn" , 1 , (0,0,0))
                    WIN.blit(text , (150 , 420))
                elif turn == 'black':
                    text = font.render("Black Turn" , 1 , (0,0,0))
                    WIN.blit(text , (150 , 420))
                            
                for val in white_peices:
                    surf , pos = val
                    WIN.blit(surf , pos)

                for val in black_peices:
                    surf , pos = val
                    WIN.blit(surf , pos)

                pygame.display.update()
                

            if event.type == pygame.QUIT:
                run = False

        # Display the black and white board
        boardDsiplay(WIN)
        pygame.draw.rect(WIN , (240 , 240 , 240) , (0,0,400,400) , 4)    
        pygame.draw.rect(WIN , (200 , 200 , 200) , (0 , 400 , 400 , 100))

        # Arrange all the pecies at the starting
        if asd == True:
            arrangePeices(WIN)
            text = font.render("White Turn" , 1 , (0,0,0))
            WIN.blit(text , (150 , 420))
            pygame.display.update()
        asd = False
        

    pygame.quit()

if __name__ == '__main__':
    main()
