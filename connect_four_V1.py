import pygame
import math

board = [["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-"]]

row_count = 5
column_count = 6

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

def draw_vis_board():
  for c in range(column_count):
    for r in range(row_count):
      pygame.draw.rect(screen, BLUE, ((c*squaresize, r*squaresize+squaresize, squaresize, squaresize)))
      if board[r][c] == "-":
        pygame.draw.circle(screen, BLACK, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)
      elif board[r][c] == "1":
        pygame.draw.circle(screen, RED, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)
      else:
        pygame.draw.circle(screen, YELLOW, (int(c*squaresize+squaresize/2), int(r*squaresize+squaresize+squaresize/2)), squaresize/2 - 5)

draw_vis_board()

pygame.display.update()

def ask_p1_input():
  global player
  player = "1"
  clicked = False
  while clicked == False:
    for event in pygame.event.get():

      if event.type == pygame.MOUSEBUTTONDOWN:
        posx = event.pos[0]

        global playerchoice
        playerchoice = int(math.floor(posx/squaresize))
        
        clicked = True
  
def placepiece():
  row = 0
  global rowfull
  rowfull = False
  
  while True:

    if board[row][playerchoice] == "-":
      row = row +1
      if row > 3:
        if board[row][playerchoice] == "-":
          row = 4
          break

        else:
          row = row - 1
          break
    
    else:
      if row == 0:
        rowfull = True
        break

      else:
        row = row - 1
        break

  if rowfull == False:
    if player == "1":  
      board[row][int(playerchoice)] = "1"
  
    else:
      board[row][int(playerchoice)] = "2"

def check_horizontal_win(player):
  horizontal_win_found = False
  checking_row = 0
  checking_column = 0

  while horizontal_win_found == False:
    for c in range(3):
      checking_row = 0
      for r in range(5):
        if board[checking_row][checking_column] == player and board[checking_row]  [checking_column+1] == player and board[checking_row][checking_column+2] == player and board[checking_row][checking_column+3] == player: 
          if player == "1":
            return "p1_wins"
          else:
            return "p2_wins"
          horizontal_win_found = True
        else:
          checking_row = checking_row + 1
      checking_column = checking_column + 1
    break

def check_vertical_win(player):
  vertical_win_found = False
  checking_row = 3
  checking_column = 0

  while vertical_win_found == False:
    for c in range(6):
      checking_row = 3
      for r in range(2):
        if board[checking_row][checking_column] == player and board[checking_row-1]  [checking_column] == player and board[checking_row-2][checking_column] == player and board[checking_row-3][checking_column] == player: 
          if player == "1":
            return "p1_wins"
          else:
            return "p2_wins"
          vertical_win_found = True
        else:
          checking_row = checking_row + 1
      checking_column = checking_column + 1
    break

def check_positive_diagonal_win(player):
  positive_diagonal_win_found = False
  checking_row = 3
  checking_column = 0

  while positive_diagonal_win_found == False:
    for c in range(3):
      checking_row = 3
      for r in range(2):
        if board[checking_row][checking_column] == player and board[checking_row-1]  [checking_column+1] == player and board[checking_row-2][checking_column+2] == player and board[checking_row-3][checking_column+3] == player: 
          if player == "1":
            return "p1_wins"
          else:
            return "p2_wins"
          positive_diagonal_win_found = True
        else:
          checking_row = checking_row + 1
      checking_column = checking_column + 1
    break

def check_negative_diagonal_win(player):
  negative_diagonal_win_found = False
  checking_row = 0
  checking_column = 0

  while negative_diagonal_win_found == False:
    for c in range(3):
      checking_row = 0
      for r in range(2):
        if board[checking_row][checking_column] == player and board[checking_row+1]  [checking_column+1] == player and board[checking_row+2][checking_column+2] == player and board[checking_row+3][checking_column+3] == player: 
          if player == "1":
            return "p1_wins"
          else:
            return "p2_wins"
          negative_diagonal_win_found = True
        else:
          checking_row = checking_row + 1
      checking_column = checking_column + 1
    break

my_font = pygame.font.SysFont("monospace", 70)

def check_win(player):
  if check_horizontal_win(player) == "p1_wins" or check_vertical_win(player) == "p1_wins" or check_positive_diagonal_win(player) == "p1_wins" or check_negative_diagonal_win(player) == "p1_wins":
    pygame.draw.rect(screen, BLACK, (0, 0, screen_width, squaresize))
    return "gameover"

  elif check_horizontal_win(player) == "p2_wins" or check_vertical_win(player) == "p2_wins" or check_positive_diagonal_win(player) == "p2_wins" or check_negative_diagonal_win(player) == "p2_wins":
    pygame.draw.rect(screen, BLACK, (0, 0, screen_width, squaresize))
    return "gameover"

playing = True
clicked = False
playerchoice = 0
player = "1"

while playing == True:

  pygame.draw.rect(screen, BLACK, (0, 0, screen_width, squaresize))
  mposx = pygame.mouse.get_pos()[0]
  if player == "1":
    pygame.draw.circle(screen, RED, (round(mposx+50, -2)-50, squaresize/2), squaresize/2)
  else:
    pygame.draw.circle(screen, YELLOW, (round(mposx+50, -2)-50, squaresize/2), squaresize/2)

  pygame.display.update()


  for event in pygame.event.get():


    if event.type == pygame.QUIT:
      pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:

      if player == "1":

        posx = event.pos[0]
        playerchoice = int(math.floor(posx/squaresize))
        
        placepiece()

        if rowfull == False:
          draw_vis_board()

          if check_win(player) == "gameover":

            label = my_font.render("Player 1 wins!", 1, RED)
            screen.blit(label, (0,0))
            pygame.display.update()
            playing = False
            break

          else:
            draw_vis_board()
            player = "2"

        else:
          continue

      else:
        posx = event.pos[0]
        playerchoice = int(math.floor(posx/squaresize))

        placepiece()

        if rowfull == False:
          draw_vis_board()

          if check_win(player) == "gameover":

            label = my_font.render("Player 2 wins!", 1, YELLOW)
            screen.blit(label, (0,0))
            pygame.display.update()

            playing = False
            break

          player = "1"

        else:
          continue

pygame.time.wait(5000)
pygame.quit()