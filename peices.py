import pygame
import os

white_pawn = pygame.image.load(os.path.join('img' , 'white_pawn.png'))
white_pawn = pygame.transform.scale(white_pawn , (40 , 40))
white_rook = pygame.image.load(os.path.join('img' , 'white_rook.png'))
white_rook = pygame.transform.scale(white_rook , (40 , 40))
white_knight = pygame.image.load(os.path.join('img' , 'white_knight.png'))
white_knight = pygame.transform.scale(white_knight , (40 , 40))
white_bishop = pygame.image.load(os.path.join('img' , 'white_bishop.png'))
white_bishop = pygame.transform.scale(white_bishop , (40 , 40))
white_queen = pygame.image.load(os.path.join('img' , 'white_queen.png'))
white_queen = pygame.transform.scale(white_queen , (40 , 40))
white_king = pygame.image.load(os.path.join('img' , 'white_king.png'))
white_king = pygame.transform.scale(white_king , (40 , 40))


black_pawn = pygame.image.load(os.path.join('img' , 'black_pawn.png'))
black_pawn = pygame.transform.scale(black_pawn , (40 , 40))
black_rook = pygame.image.load(os.path.join('img' , 'black_rook.png'))
black_rook = pygame.transform.scale(black_rook , (40 , 40))
black_knight = pygame.image.load(os.path.join('img' , 'black_knight.png'))
black_knight = pygame.transform.scale(black_knight , (40 , 40))
black_bishop = pygame.image.load(os.path.join('img' , 'black_bishop.png'))
black_bishop = pygame.transform.scale(black_bishop , (40 , 40))
black_queen = pygame.image.load(os.path.join('img' , 'black_queen.png'))
black_queen = pygame.transform.scale(black_queen , (40 , 40))
black_king = pygame.image.load(os.path.join('img' , 'black_king.png'))
black_king = pygame.transform.scale(black_king , (40 , 40))

center_peices_pad = 5

black_peices = []
white_peices = []

def arrangePeices(WIN):
    # Arranging Black Pawn on the board
    for i in range(0 , 8):
        black_x = 50 * i + center_peices_pad
        black_y = center_peices_pad + 50
        WIN.blit(black_pawn , (black_x , black_y))
        black_peices.append((black_pawn , (black_x , black_y)))

    # Arranging White Pawn on the board
    for i in range(0 , 8):
        white_x = 50 * i + center_peices_pad
        white_y = center_peices_pad + 300
        WIN.blit(white_pawn , (white_x , white_y))
        white_peices.append((white_pawn , (white_x , white_y)))
  
    #Arranging the Black Rook on the board
    black_rook_1_x = 0 + center_peices_pad
    black_rook_1_y = 0 + center_peices_pad
    black_rook_2_x = 350 + center_peices_pad
    black_rook_2_y = 0 + center_peices_pad
    WIN.blit(black_rook , (black_rook_1_x , black_rook_1_y))
    WIN.blit(black_rook , (black_rook_2_x , black_rook_2_y))
    black_peices.append((black_rook , (black_rook_1_x , black_rook_1_y)))
    black_peices.append((black_rook , (black_rook_2_x , black_rook_2_y)))

    #Arranging the White Rook on the board
    white_rook_1_x = 0 + center_peices_pad
    white_rook_1_y = 350 + center_peices_pad
    white_rook_2_x = 350 + center_peices_pad
    white_rook_2_y = 350 + center_peices_pad
    WIN.blit(white_rook , (white_rook_1_x , white_rook_1_y))
    WIN.blit(white_rook , (white_rook_2_x , white_rook_2_y))
    white_peices.append((white_rook , (white_rook_1_x , white_rook_1_y)))
    white_peices.append((white_rook , (white_rook_2_x , white_rook_2_y)))

    # Arranging the Black Knight on the board
    black_knight_1_x = 50 + center_peices_pad
    black_knight_1_y = 0 + center_peices_pad
    black_knight_2_x = 300 + center_peices_pad
    black_knight_2_y = 0 + center_peices_pad
    WIN.blit(black_knight , (black_knight_1_x , black_knight_1_y))
    WIN.blit(black_knight , (black_knight_2_x , black_knight_2_y))
    black_peices.append((black_knight , (black_knight_1_x , black_knight_1_y)))
    black_peices.append((black_knight , (black_knight_2_x , black_knight_2_y)))
    
    # Arranging the White Knight on the board
    white_knight_1_x = 50 + center_peices_pad
    white_knight_1_y = 350 + center_peices_pad
    white_knight_2_x = 300 + center_peices_pad
    white_knight_2_y = 350 + center_peices_pad
    WIN.blit(white_knight , (white_knight_1_x , white_knight_1_y))
    WIN.blit(white_knight , (white_knight_2_x , white_knight_2_y))
    white_peices.append((white_knight , (white_knight_1_x , white_knight_1_y)))
    white_peices.append((white_knight , (white_knight_2_x , white_knight_2_y)))

    # Arranging the Black Bishop on the board
    black_bishop_1_x = 100 + center_peices_pad
    black_bishop_1_y = 0 + center_peices_pad
    black_bishop_2_x = 250 + center_peices_pad
    black_bishop_2_y = 0 + center_peices_pad
    WIN.blit(black_bishop , (black_bishop_1_x , black_bishop_1_y))
    WIN.blit(black_bishop , (black_bishop_2_x , black_bishop_2_y))
    black_peices.append((black_bishop , (black_bishop_1_x , black_bishop_1_y)))
    black_peices.append((black_bishop , (black_bishop_2_x , black_bishop_2_y)))
    
    # Arranging the Black Bishop on the board
    white_bishop_1_x = 100 + center_peices_pad
    white_bishop_1_y = 350 + center_peices_pad
    white_bishop_2_x = 250 + center_peices_pad
    white_bishop_2_y = 350 + center_peices_pad
    WIN.blit(white_bishop , (white_bishop_1_x , white_bishop_1_y))
    WIN.blit(white_bishop , (white_bishop_2_x , white_bishop_2_y))
    white_peices.append((white_bishop , (white_bishop_1_x , white_bishop_1_y)))
    white_peices.append((white_bishop , (white_bishop_2_x , white_bishop_2_y)))

    # Arranging the Queens on the board
    black_queen_x = 150 + center_peices_pad 
    black_queen_y = 0 + center_peices_pad
    white_queen_x = 150 + center_peices_pad
    white_queen_y = 350 + center_peices_pad
    WIN.blit(black_queen , (black_queen_x , black_queen_y))
    WIN.blit(white_queen , (white_queen_x , white_queen_y))
    black_peices.append((black_queen , (black_queen_x , black_queen_y)))
    white_peices.append((white_queen , (white_queen_x , white_queen_y)))
    
    # Arranging the Kings on the board
    black_king_x = 200 + center_peices_pad 
    black_king_y = 0 + center_peices_pad
    white_king_x = 200 + center_peices_pad
    white_king_y = 350 + center_peices_pad
    WIN.blit(black_king , (black_king_x , black_king_y))
    WIN.blit(white_king , (white_king_x , white_king_y))
    black_peices.append((black_king , (black_king_x , black_king_y)))
    white_peices.append((white_king , (white_king_x , white_king_y)))

    

