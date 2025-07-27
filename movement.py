import pygame
import os
from peices import *
from pawn import *
from rook import *
from bishop import *
from knight import *
from king import *

def check(val , get_white_peices , get_black_peices):
    black , white = 0 , 0
    if val[0] == white_pawn:
        white , black = 1, 0
        return white_pawn_generate(val , get_white_peices , get_black_peices , white , black)
    elif val[0] == black_pawn:
        white , black = 0, 1
        return black_pawm_generate(val , get_white_peices , get_black_peices , white , black)
    
    elif val[0] == white_rook:
        white , black = 1, 0
        return rook_generate(val , get_white_peices , get_black_peices , white , black)
    elif val[0] == black_rook:
        white , black = 0, 1
        return rook_generate(val , get_white_peices , get_black_peices , white , black)
    
    elif val[0] == black_knight:
        white , black = 0, 1
        return knight_generate(val , get_white_peices , get_black_peices , white , black)
    elif val[0] == white_knight:
        white , black = 1, 0
        return knight_generate(val , get_white_peices , get_black_peices , white , black)
    
    elif val[0] == black_bishop:
        white , black = 0, 1
        return bishop_generate(val , get_white_peices , get_black_peices , white , black)
    elif val[0] == white_bishop:
        white , black = 1, 0
        return bishop_generate(val , get_white_peices , get_black_peices , white , black)
    
    elif val[0] == black_queen:
        white , black = 0, 1
        rook_list = rook_generate(val, get_white_peices , get_black_peices , white , black)
        bishop_list = bishop_generate(val, get_white_peices , get_black_peices , white , black)
        return rook_list + bishop_list
    elif val[0] == white_queen:
        white , black = 1, 0
        rook_list = rook_generate(val , get_white_peices , get_black_peices , white , black)
        bishop_list = bishop_generate(val , get_white_peices , get_black_peices , white , black)
        return rook_list + bishop_list
    
    elif val[0] == black_king:
        white , black = 0, 1
        return king_generate(val, get_white_peices , get_black_peices , white , black)
    elif val[0] == white_king:
        white , black = 1, 0
        return king_generate(val , get_white_peices , get_black_peices , white , black)
    
    else:
        return 0
    



