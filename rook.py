import pygame
import os
from peices import *

def rook_generate(val , get_white_peices , get_black_peices , white , black):
    newRookList = []
    rook_x, rook_y = val[1]

    if white == 1:
        your_peices = get_white_peices
        opponent_peices = get_black_peices
    else:
        your_peices = get_black_peices
        opponent_peices = get_white_peices

    # Moving up
    peice1 = False
    peice2 = False
    i = 1
    while rook_y - (50 * i) >= 0:
        final_x = rook_x
        final_y = rook_y - (50 * i)
        for wval , bval in zip(your_peices , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
            break

        newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
        i += 1

    # Moving down
    peice1 = False
    peice2 = False
    i = 1
    while rook_y + (50 * i) < 400:
        final_x = rook_x
        final_y = rook_y + (50 * i)
        for wval , bval in zip(your_peices , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
            break

        newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
        i += 1

    # Moving left
    peice1 = False
    peice2 = False
    i = 1
    while rook_x - (50 * i) >= 0:
        final_x = rook_x - (50 * i)
        final_y = rook_y
        for wval , bval in zip(your_peices , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
            break

        newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
        i += 1

    # Moving right
    i = 1
    peice1 = False
    peice2 = False
    while rook_x + (50 * i) <= 400:
        final_x = rook_x + (50 * i)
        final_y = rook_y
        for wval , bval in zip(your_peices , opponent_peices):
            if wval[1][0] == final_x and wval[1][1] == final_y:
                peice1 = True
                break
            if bval[1][0] == final_x and bval[1][1] == final_y:
                peice2 = True
                break
        if peice1 == True:
            break
        if peice2 == True:
            newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
            break
        newRookList.append((val , pygame.Rect(final_x - center_peices_pad , final_y - center_peices_pad, 50, 50)))
        i += 1
    
    return newRookList

