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

# board[1][3] = 1
# print(board)

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

draw_vis_board()

while playing:
  # mposx = pygame.mouse.get_pos()[0]
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      playing = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      posx = event.pos[0]
      player_choice = int(math.floor(posx/squaresize))

      if place_piece(player_choice, player_current) == True:
        player_current, player_next = player_next, player_current

  draw_vis_board()
  pygame.display.flip()

pygame.quit()