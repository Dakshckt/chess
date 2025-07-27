
import pygame
from peices import *

def king_generate(val , get_white_peices , get_black_peices, white , black):
    newKingList = []
    # print(val)
    if white == 1:
        opponent_peices = get_white_peices
    else:
        opponent_peices = get_black_peices
    peice = False
    x , y = val[1]
    steps = [
        (x , y + 50),
        (x , y - 50),
        (x + 50 , y),
        (x - 50 , y),
        (x + 50 , y + 50),
        (x + 50 , y - 50),
        (x - 50 , y + 50),
        (x - 50 , y - 50),
    ]
    for sval in steps:
        if sval[0] - center_peices_pad >= 0 and sval[1] - center_peices_pad >= 0 and sval[0] - center_peices_pad < 400 and sval[1] - center_peices_pad < 400:
            final_x = sval[0]
            final_y = sval[1]
            for oval in opponent_peices:
                if oval[1][0] == final_x and oval[1][1] == final_y:
                    peice = True
                    break
            if peice == True:
                peice = False
                continue
            newKingList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))

    return newKingList