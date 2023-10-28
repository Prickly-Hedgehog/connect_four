import math
import pygame

board = []

row_count = 6
column_count = 7

for i in range(row_count):
  board_row = [0] * column_count
  board.append(board_row)

player_current = 1
player_next = 2

playing = True

#pygame init and variables
#==========
pygame.init()
pygame.display.set_caption("Connect 4")

my_font = pygame.font.SysFont("monospace", 70)

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
  pygame.display.flip()

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

def check_win_negative_diagonal(player_current):
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

def check_win_positive_diagonal(player_current):
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
  if check_win_horizontal(player_current) != -1 or check_win_vertical(player_current) != -1 or check_win_positive_diagonal(player_current) != -1 or check_win_negative_diagonal(player_current) != -1:
    return player_current
  return -1

while playing:

  pygame.draw.rect(screen, BLACK, (0, 0, screen_width, squaresize))
  mposx = pygame.mouse.get_pos()[0]
  if player_current == 1:
    pygame.draw.circle(screen, RED, (round(mposx+50, -2)-50, squaresize/2), squaresize/2)
  else:
    pygame.draw.circle(screen, YELLOW, (round(mposx+50, -2)-50, squaresize/2), squaresize/2)

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      posx = event.pos[0]
      player_choice = int(math.floor(posx/squaresize))

      if place_piece(player_choice, player_current) == True:
        check_win_var = check_win(player_current)
        if check_win_var != -1:
          if check_win_var == 1:
            player_colour = RED
          else:
            player_colour = YELLOW
          pygame.draw.rect(screen, BLACK, (0, 0, screen_width, squaresize))
          win_text = "Player " + str(player_current) + " wins"
          label = my_font.render(str(win_text), 1, player_colour)
          label_rect = label.get_rect()
          label_rect.center = (screen_width/2, squaresize/2)
          screen.blit(label, label_rect)
          pygame.display.flip()
          playing = False
  
        player_current, player_next = player_next, player_current

  draw_vis_board()
  pygame.display.flip()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()