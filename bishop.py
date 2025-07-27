import pygame
from peices import *


def bishop_generate(val  , get_white_peices , get_black_peices, white , black):
    newbishopList = []
    x , y = val[1]

    if white == True:
        your_pecies = get_white_peices
        opponent_peices = get_black_peices
    else:
        your_pecies = get_black_peices
        opponent_peices = get_white_peices

    # Moving Right Up
    peice1 = False
    peice2 = False
    i = 1
    while x + (50 * i) < 400 and y - (50 * i) >= 0:
        final_x = x + (50 * i)
        final_y = y - (50 * i)
        for wval , bval in zip(your_pecies , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
            break

        newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
        i += 1
    # Moving Left Up
    peice1 = False
    peice2 = False
    i = 1
    while x - (50 * i) >= 0 and y - (50 * i) >= 0:
        final_x = x - (50 * i)
        final_y = y - (50 * i)
        for wval , bval in zip(your_pecies , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
            break
        newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad  , 50 , 50)))
        i += 1
    # Moving Right Down
    peice1 = False
    peice2 = False
    i = 1
    while x + (50 * i) < 400 and y + (50 * i) < 400:
        final_x = x + (50 * i)
        final_y = y + (50 * i)
        for wval , bval in zip(your_pecies , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
            break
        newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad  , 50 , 50)))
        i += 1
    # Moving Left Down
    peice1 = False
    peice2 = False
    i = 1
    while x - (50 * i) >= 0 and y + (50 * i) < 400:
        final_x = x - (50 * i)
        final_y = y + (50 * i)
        for wval , bval in zip(your_pecies , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad , 50 , 50)))
            break
        newbishopList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad  , 50 , 50)))
        i += 1
    i = 1

    return newbishopList


