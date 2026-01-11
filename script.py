
# Imports
import pygame
from enemy import enemy
from ground import ground


# Creating Game Window
pygame.init()
canvas = pygame.display.set_mode((750, 750), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
exit = False
pygame.display.update()
background_col = (25, 75, 25)


#Creating prerequisites for start screen
screen_color = (200, 150, 150)
start_box = pygame.Rect(275, 325, 200, 100)
start_box_color = (150, 200, 200)
start_box_hover_color = (150, 150, 200)




#A few Colors
coal_color = (0,0,0)
fire_turret_color = (250, 50, 50)
gray_color = (100,100,100)

# Creating Grid for Ground
grid = []
columns = 17
rows = 17
grid_color = (100,100,100)

for row in range(columns):
    grid_row = []
    for col in range(rows):
        rect = pygame.Rect(col * 50, row * 50, 50, 50)
        pygame.draw.rect(canvas, grid_color, rect, 1)
        tile = ground(row, col, grid_color, 1, False, False, "ground", False, False, 100)
        grid_row.append(tile)
    grid.append(grid_row)


# Function for Displaying Grid
def draw_grid():
    for row in grid:
        for tile in row:
            rect = pygame.Rect(tile.row * 50, tile.col * 50, 50, 50)
            pygame.draw.rect(canvas, tile.color, rect, tile.wid)
            if tile.type == "fire_turret":
                rect = pygame.Rect((tile.row * 50)+10, (tile.col * 50)+10, 30, 30)
                pygame.draw.rect(canvas, gray_color, rect, tile.wid)
                rect = pygame.Rect(tile.row * 50, tile.col * 50, 50, 50)
                pygame.draw.rect(canvas, gray_color, rect, 5)

#Enemy list and stuff
enemies = []

def draw_enemies():
    for enemy in enemies:
        rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
        pygame.draw.rect(canvas, (100,0,0), rect, 0)

def enemy_search1():
    for enemy in enemies:
        enemy_grid_row = enemy.x //50
        enemy_grid_col = enemy.y //50
        for x in range(2):
            y = -2
            if grid[enemy_grid_row + x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row + x][enemy_grid_col + y]
               enemy.target_dir = "up_right"
            if grid[enemy_grid_row - x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row - x][enemy_grid_col + y]
               enemy.target_dir = "up_left"
        for x in range(2):
            y = +2
            if grid[enemy_grid_row + x][enemy_grid_col + y].type == "fire_turret":
               enemy.target = grid[enemy_grid_row + x][enemy_grid_col + y]
               enemy.target_dir = "down_right"
            if grid[enemy_grid_row - x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row - x][enemy_grid_col + y]
               enemy.target_dir = "down_left"
        for x in range(2):
            y = -1
            if grid[enemy_grid_row + x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row + x][enemy_grid_col + y]
               enemy.target_dir = "up_right"
            if grid[enemy_grid_row - x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row - x][enemy_grid_col + y]
               enemy.target_dir = "up_left"
        for x in range(2):
            y = +1
            if grid[enemy_grid_row + x][enemy_grid_col + y].type == "fire_turret":
               enemy.target = grid[enemy_grid_row + x][enemy_grid_col + y]
               enemy.target_dir = "down_right"
            if grid[enemy_grid_row - x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row - x][enemy_grid_col + y]
               enemy.target_dir = "down_left"
        for x in range(3):
            y = 0
            b = x +1
            if grid[enemy_grid_row + b][enemy_grid_col + y].type == "fire_turret":
               enemy.target = grid[enemy_grid_row + x][enemy_grid_col + y]
               enemy.target_dir = "right"
            if grid[enemy_grid_row - x][enemy_grid_col + y].type == "fire_turret":
               enemy.target =  grid[enemy_grid_row - x][enemy_grid_col + y]
               enemy.target_dir = "left"
def tickle_ashton():
    global enemy_on_turret, build_rect
    for row in grid:
        for tile in row:
            for enemy in enemies:
                rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
                c = False
                if tile.type == "fire_turret":
                    build_rect = pygame.Rect(tile.row * 50, tile.col * 50, 50, 50)
                    c = rect.colliderect(build_rect)
                if c == True:
                    enemy_on_turret = True
                    tile.damage = True
                    print("collide")
            if tile.health <= 0:
                print("Ayeu")
                tile.type = "ground"
                tile.color = grid_color
                tile.wid = 1
                tile.damage = False
                tile.health = 100
                enemy_on_turret = False
                enemy.target = False
                enemy.target_dir = "Core"


enemy_on_turret = False
build_rect = pygame.Rect(-100,-100, 1, 1)
def enemy_move():
    global build_rect, enemy_on_turret
    for enemy in enemies:
        enemy_on_right_wall = False
        enemy_on_left_wall = False
        enemy_on_roof = False
        enemy_on_floor = False
        if enemy_on_turret == False:
            if enemy.x <= 0:
                enemy_on_left_wall = True
            if enemy.x >= 750:
                enemy_on_right_wall = True
            if enemy.y <= 0:
                enemy_on_roof = True
            if enemy.y >= 710:
                enemy_on_floor = True
            if enemy.target_dir == "up_right":
                if not enemy_on_right_wall:
                    enemy.x += 1
                if not enemy_on_roof:
                    enemy.y -= 1
            elif enemy.target_dir == "up_left":
                if not enemy_on_left_wall:
                    enemy.x -= 1
                if not enemy_on_roof:
                    enemy.y -= 1
            elif enemy.target_dir == "down_right":
                if not enemy_on_right_wall:
                    enemy.x += 1
                if not enemy_on_floor:
                    enemy.y += 1
            elif enemy.target_dir == "down_left":
                if not enemy_on_left_wall:
                    enemy.x -= 1
                if not enemy_on_floor:
                    enemy.y += 1
            elif enemy.target_dir == "right":
                if not enemy_on_right_wall:
                    enemy.x += 1
            elif enemy.target_dir == "left":
                if not enemy_on_left_wall:
                    enemy.x -= 1
            else:
                if not enemy_on_left_wall:
                    enemy.x -= 1
                if not enemy_on_floor:
                    enemy.y += 1



coal_place = False
game_screen = False
start_screen = True
fire_turret_place = False
enemy_place = False

while not exit:
    while start_screen:
        clock = pygame.time.Clock()
        canvas.fill(screen_color)

        #Draw start box
        robert = pygame.draw.rect(canvas, start_box_color, start_box, 0)

        #Get mouse
        mos_x, mos_y = pygame.mouse.get_pos()
        if 275 <= mos_x <= 475 and 325 <= mos_y <= 425:
            robert = pygame.draw.rect(canvas, start_box_hover_color, start_box, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 275 <= mos_x <= 475 and 325 <= mos_y <= 425:
                    game_screen = True
                    start_screen = False


        pygame.display.update()
        clock.tick(60)




    while game_screen == True:
        clock = pygame.time.Clock()
        canvas.fill(background_col)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mos_x, mos_y = pygame.mouse.get_pos()
                oth_mos_x = mos_x
                oth_mos_y = mos_y
                mos_x = mos_x // 50
                mos_y = mos_y //50
                if grid[mos_x][mos_y].type == "coal":
                    grid[mos_x][mos_y].mining_status = True
                if grid[mos_x][mos_y].mining_status == True:
                    print(str(grid[mos_x][mos_y]) + ' is being mined.')

                if coal_place == True and grid[mos_x][mos_y].occupy == False:
                    grid[mos_x][mos_y].type = "coal"
                    grid[mos_x][mos_y].color = coal_color
                    grid[mos_x][mos_y].wid = 0
                if fire_turret_place == True and grid[mos_x][mos_y].occupy == False:
                    grid[mos_x][mos_y].type = "fire_turret"
                    grid[mos_x][mos_y].color = fire_turret_color
                    grid[mos_x][mos_y].wid = 0
                    grid[mos_x][mos_y].occupy = True
                if enemy_place == True:
                    rect = pygame.Rect(oth_mos_x-20, oth_mos_y-20, 50, 50)
                    rect = enemy(oth_mos_x-25, oth_mos_y-25, "test", False, 100, False, "Core")
                    enemies.append(rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if coal_place == False:
                        coal_place = True
                    elif coal_place == True:
                        coal_place = False
                if event.key == pygame.K_p:
                    start_screen = True
                    game_screen = False
                if event.key == pygame.K_1 and fire_turret_place == False:
                    fire_turret_place = True
                elif event.key == pygame.K_1 and fire_turret_place == True:
                    fire_turret_place = False
                if event.key == pygame.K_2 and enemy_place == False:
                    enemy_place = True
                elif event.key == pygame.K_2 and enemy_place == True:
                    enemy_place = False



        # Display Grid
        enemy_search1()
        enemy_move()
        draw_grid()
        draw_enemies()
        pygame.display.update()


        if exit == True:
            pygame.quit()
        clock.tick(60)


