import math
import pygame

board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]

row_count = 6
column_count = 7

player_current = 1
player_next = 2

playing = True

#pygame init and variables
#==========
pygame.init()
pygame.display.set_caption("Connect 4")

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

squaresize = 100

screen_width = squaresize * column_count
screen_height = squaresize * row_count + squaresize

screen = pygame.display.set_mode((screen_width, screen_height))
#==========

def draw_vis_board():
  for c in range(column_count):
    for r in range(row_count):
      pygame.draw.rect(screen, BLUE, ((c*squaresize, r*squaresize+squaresize, squaresize, squaresize)))
      if board[r][c] == 0:
        pygame.draw.circle(screen, BLACK, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)
      elif board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)
      else:
        pygame.draw.circle(screen, YELLOW, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)
  pygame.display.update()

def place_piece(player_choice, player_current):

  found_open_square = False
  checking_row = row_count - 1

  while found_open_square == False:
    if board[checking_row][player_choice] == 0:
      board[checking_row][player_choice] = player_current
      found_open_square = True
    if checking_row == -1:
      print("Row full")
      return False
    else:
      checking_row -= 1
  return True

def check_win_horizontal(player_current):
  checking_row = 0
  checking_column = 0
  for c in range(column_count-3):
    checking_row = 0
    for r in range(row_count):
      if board[checking_row][checking_column] == player_current and board[checking_row][checking_column+1] == player_current and board[checking_row][checking_column+2] == player_current and board[checking_row][checking_column+3] == player_current:
        return player_current
      else:
        checking_row += 1
    checking_column += 1
  return -1

def check_win_vertical(player_current):
  checking_row = 0
  checking_column = 0
  for r in range(row_count-3):
    checking_column = 0
    for c in range(column_count):
      if board[checking_row][checking_column] == player_current and board[checking_row+1][checking_column] == player_current and board[checking_row+2][checking_column] == player_current and board[checking_row+3][checking_column] == player_current:
        return player_current
      else:
        checking_column += 1
    checking_row += 1
  return -1

def check_negative_diagonal_win(player_current):
  checking_row = 0
  checking_column = 0
  for r in range(row_count-3):
    checking_column = 0
    for c in range(column_count-3):
      if board[checking_row][checking_column] == player_current and board[checking_row+1][checking_column+1] == player_current and board[checking_row+2][checking_column+2] == player_current and board[checking_row+3][checking_column+3] == player_current:
        return player_current
      else:
        checking_column += 1
    checking_row += 1
  return -1

def check_positive_diagonal_win(player_current):
  checking_row = row_count-3
  checking_column = 0
  for r in range(row_count-3):
    checking_column = 0
    for c in range(column_count-3):
      if board[checking_row][checking_column] == player_current and board[checking_row-1][checking_column+1] == player_current and board[checking_row-2][checking_column+2] == player_current and board[checking_row-3][checking_column+3] == player_current:
        return player_current
      else:
        checking_column += 1
    checking_row += 1
  return -1

def check_win(player_current):
  horizontal_win = check_win_horizontal(player_current)
  vertical_win = check_win_vertical(player_current)
  negative_diagonal_win = check_negative_diagonal_win(player_current)
  positive_diagonal_win = check_positive_diagonal_win(player_current)

  if horizontal_win != -1:
    return "h", horizontal_win
  if vertical_win != -1:
    return "v", vertical_win
  if positive_diagonal_win != -1:
    return "pd", positive_diagonal_win
  if negative_diagonal_win != -1:
    return "nd", negative_diagonal_win
  return -1

while playing:
  # mposx = pygame.mouse.get_pos()[0]
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      playing = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      posx = event.pos[0]
      player_choice = int(math.floor(posx/squaresize))

      if place_piece(player_choice, player_current) == True:
        check_win_var = check_win(player_current)
        if check_win_var != -1:
          print(check_win_var[0], "player", check_win_var[1])
  
        player_current, player_next = player_next, player_current

  draw_vis_board()
  pygame.display.flip()

pygame.quit()