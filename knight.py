import pygame
from peices import *


def knight_generate(val  , get_white_peices , get_black_peices , white , black):
    newKnightList = []
    peice = False
    # print(val)
    
    if white == 1:
        opponent_peice = get_white_peices
    else:
        opponent_peice = get_black_peices
    x , y = val[1]
    steps = [
        (x - 50 , y - 100),
        (x + 50 , y - 100),
        (x + 100 , y - 50),
        (x + 100 , y + 50),
        (x + 50 , y + 100),
        (x - 50 , y + 100),
        (x - 100 , y + 50),
        (x - 100 , y - 50)
    ]
    for sval in steps:
        if sval[0] - center_peices_pad >= 0 and sval[1] - center_peices_pad >= 0 and sval[0] - center_peices_pad < 400 and sval[1] - center_peices_pad < 400:
            final_x = sval[0]
            final_y = sval[1]
            for oval in opponent_peice:
                if oval[1][0] == final_x and oval[1][1] == final_y:
                    peice = True
                    break    
            if peice == True:
                peice = False
                continue
            newKnightList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))

    return newKnightList