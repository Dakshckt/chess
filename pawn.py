import pygame
import os
from peices import *

def white_pawn_generate(val  , get_white_peices , get_black_peices, white , black):
    peice1 = False
    x , y = val[1]
    newRect = []
    for wval , bval in zip(get_white_peices , get_black_peices):
        final_x = x
        final_y = y - 50
        attack_x1 = x - 50
        attack_y1 = y - 50
        attack_x2 = x + 50
        attack_y2 = y - 50
        if bval[1][0] == attack_x1 and bval[1][1] == attack_y1 :
            newRect.append((val , pygame.Rect(attack_x1 - center_peices_pad , attack_y1 - center_peices_pad , 50 , 50)))
        if bval[1][0] == attack_x2 and bval[1][1] == attack_y2:
            newRect.append((val , pygame.Rect(attack_x2 - center_peices_pad , attack_y2 - center_peices_pad , 50 , 50)))
        if wval[1][0] == final_x and wval[1][1] == final_y or bval[1][0] == final_x and bval[1][1] == final_y:
            peice1 = True
            
    if peice1 == True:
        pass
    else:
        newRect.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
    
    return newRect

def black_pawm_generate(val  , get_white_peices , get_black_peices , white , black):
    peice1 = False
    x , y = val[1]
    newRect = []
    for wval , bval in zip(get_white_peices , get_black_peices):
        final_x = x
        final_y = y + 50
        attack_x1 = x - 50
        attack_y1 = y + 50
        attack_x2 = x + 50
        attack_y2 = y + 50
        if wval[1][0] == attack_x1 and wval[1][1] == attack_y1 :
            newRect.append((val , pygame.Rect(attack_x1 - center_peices_pad , attack_y1 - center_peices_pad , 50 , 50)))
        if wval[1][0] == attack_x2 and wval[1][1] == attack_y2:
            newRect.append((val , pygame.Rect(attack_x2 - center_peices_pad , attack_y2 - center_peices_pad , 50 , 50)))
        if wval[1][0] == final_x and wval[1][1] == final_y or bval[1][0] == final_x and bval[1][1] == final_y:
            peice1 = True
    if peice1 == True:
        pass
    else:
        newRect.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
    
    return newRect