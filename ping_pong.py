import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_height = 650
screen_width = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pingpong tournament !")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 180, 0)

police_carac = {
    1: 'D:/Documents/Paul/Font/celtic_md/celticmd.ttf',
    2: 'D:/Documents/Paul/Font/cowboy_wildwest/COWBOYWILDWEST.ttf',
    3: 'D:/Documents/Paul/Font/nasalization/nasalization-rg.otf',
    4: 'D:/Documents/Paul/Font/viking/VIKING-N.TTF',
    5: 'D:/Documents/Paul/Font/first_order/firstorder.ttf',

}
m = 1

# scores
player_score = 0
player2_score = 0
player_round = 0
player2_round = 0




# Images 

# fantaisie :

# image1 = 'D:/Workspace/esportjpg2.jpg'
# image2 = 'D:/Workspace/exportjpg3.jpg'
# police = 'D:/Documents/Paul/Font/celtic_md/celticmd.ttf'
# contraste_color = BLACK
# contraste2_color = WHITE

# western :

image1 = 'D:/Workspace/esportjpg3.jpg'
image2 = 'D:/Workspace/esportjpg4.jpg'
police = 'D:/Documents/Paul/Font/cowboy_wildwest/COWBOYWILDWEST.ttf'
contraste_color = WHITE
contraste2_color = BLACK




#fin de partie

def end_round1():
    fond = pygame.image.load(image1).convert_alpha()
    screen.blit(fond, (0, 0))
    font = pygame.font.Font(police, 20)
    end_text = font.render(f"Player Blue won : {player2_round} - {player_round} / {player2_score} - {player_score}", True, BLUE)
    screen.blit(end_text, (screen_width // 7, screen_height // 2.5))

def end_round2():
    fond = pygame.image.load(image1).convert_alpha()
    screen.blit(fond, (0, 0))
    font = pygame.font.Font(police, 20)
    end_text = font.render(f"Player Green won : {player2_round} - {player_round} / {player2_score} - {player_score}", True, GREEN)
    screen.blit(end_text, (screen_width // 7, screen_height // 2.5))

def end_game1():
    fond = pygame.image.load(image1).convert_alpha()
    screen.blit(fond, (0, 0))
    font = pygame.font.Font(police, 25)
    endgame_text = font.render("VICTORY green !", True, RED)
    screen.blit(endgame_text, (screen_width // 5, screen_height // 4))
    endgame_text = font.render("Blue    Green", True, GREEN)
    screen.blit(endgame_text, (screen_width // 3.8, screen_height // 3))
    endgame_text = font.render(f"{player2_round}              {player_round}", True, contraste_color)
    screen.blit(endgame_text, (screen_width // 3.3, screen_height // 2.5))

def end_game2():
    fond = pygame.image.load(image1).convert_alpha()
    screen.blit(fond, (0, 0))
    font = pygame.font.Font(police, 25)
    endgame_text = font.render("VICTORY blue !", True, RED)
    screen.blit(endgame_text, (screen_width // 5, screen_height // 4))
    endgame_text = font.render("Blue    Green", True, BLUE)
    screen.blit(endgame_text, (screen_width // 3.8, screen_height // 3))
    endgame_text = font.render(f"{player2_round}              {player_round}", True, contraste_color)
    screen.blit(endgame_text, (screen_width // 3.3, screen_height // 2.5))


# Affichage écran d'accueil

def game_begin():
    fond = pygame.image.load(image1).convert_alpha()
    screen.blit(fond, (0, 0))
    font = pygame.font.Font(police, 16)
    begin_text = font.render("Welcome to the BEST ping-pong tournament !", True, contraste_color)
    screen.blit(begin_text, (screen_width //40, screen_height // 4.5))
    font = pygame.font.Font(police, 25)
    begin_text = font.render("Two players game", True, RED)
    screen.blit(begin_text, (screen_width //5, screen_height // 3))
    font = pygame.font.Font(police, 15)
    begin_text = font.render("Choose your style mode by pressing the UP key", True, BLUE)
    screen.blit(begin_text, (screen_width //50, screen_height // 2))





# FPS
fps = 60


# Paramètres du joueur
player_width = 80
player_height = 20
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 10
player_speed = (20*30) /fps

# Paramètres du joueur2
player2_width = 80
player2_height = 20
player2_x = (screen_width - player2_width) // 2
player2_y = 130
player2_speed = (20*30) /fps

# Paramètres de la balle
ball_width = 22
ball_height = 22
ball_x =  (screen_width - ball_width) // 2
ball_y = (screen_height - ball_height) // 2
ball_speed_x = 0
ball_speed_y = (7*30) /fps
ball_speedmax = 20

# Bots







# Boucle principale du jeu
running = True
clock = pygame.time.Clock()


game_begin()
pygame.display.update()
pygame.time.delay(5000)
        
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # changement de police
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and m == 1:
            m = 2
            police = police_carac[2]
            continue
    if keys[pygame.K_UP] and m == 2:
            m = 3
            police = police_carac[3]
            continue
    if keys[pygame.K_UP] and m == 3:
            m = 4
            police = police_carac[4]
            continue
    if keys[pygame.K_UP] and m == 4:
            m = 5
            police = police_carac[5]
            continue
    if keys[pygame.K_UP] and m == 5:
            m = 1
            police = police_carac[1]
            continue

    # Mouvement des joueurs

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < (screen_width - player_width):
        player_x += player_speed
    if keys[pygame.K_q] and player2_x > 0:
        player2_x -= player2_speed
    if keys[pygame.K_d] and player2_x < (screen_width - player2_width):
        player2_x += player2_speed

    # Mouvement de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Rebonds sur les murs
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_speed_x = -ball_speed_x

    # Rebonds sur les raquettes
    if (player_x < ball_x < player_x + player_width or player_x < ball_x + ball_width < player_x + player_width) and ball_y + ball_height >= player_y:
        ball_speed_y = -ball_speed_y 
        ball_y = player_y - ball_height
        ball_speed_x += random.randint(-5, 5)
        
        
        
    if (player2_x < ball_x < player2_x + player2_width or player2_x < ball_x + ball_width < player2_x + player2_width) and ball_y <= player2_y + player2_height:
        ball_speed_y = -ball_speed_y
        if ball_speed_y != ball_speedmax:
            ball_speed_y += 1
        ball_y = player2_y + player2_height
        ball_speed_x += random.randint(-5, 5)
        


    # Réinitialisation de la balle si elle sort des limites
    if ball_y > screen_height:
        player2_score += 1
        player_score += 0
        ball_x = (screen_width - ball_width) // 2
        ball_y = (screen_height - ball_height) // 2
        ball_speed_x = 0
        ball_speed_y = (8*30) /fps
        if player2_score >= 4 :
            if player_score < player2_score - 1 :
                player2_round += 1
                if player2_round == 3 :
                    print("Player 2 won !")
                    end_game2()
                    pygame.display.update()
                    pygame.time.delay(5000)
                    break
                print(f"Blue : {player2_score}")
                print(f"Green : {player_score}")
                end_round1()
                pygame.display.update()
                pygame.time.delay(5000)
                player_score = player2_score = 0
                player2_width -= 15
            else :
                continue

    if ball_y < 110:
        player_score += 1
        player2_score += 0
        ball_x = (screen_width - ball_width) // 2
        ball_y = (screen_height - ball_height) // 2
        ball_speed_x = 0
        ball_speed_y = (-8*30) /fps
        if player_score >= 4 :
            if player2_score < player_score - 1 :
                player_round += 1
                if player_round == 3 :
                    print("Player 1 won !")
                    end_game1()
                    pygame.display.update()
                    pygame.time.delay(5000)
                    break
                print(f"Blue : {player2_score}")
                print(f"Green : {player_score}")
                end_round2()
                pygame.display.update()
                pygame.time.delay(5000)
                player_score = player2_score = 0
                player_width -= 15
            else :
                continue
    
    # Affichage des éléments à l'écran
    #fond = screen.fill(BLACK)
    
    fond = pygame.image.load(image2).convert_alpha()
    screen.blit(fond, (0, 0))


    pygame.draw.rect(screen, BLUE, (player2_x, player2_y, player2_width, player2_height))
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_width, ball_height))
    pygame.draw.rect(screen, contraste2_color, (0, 105, screen_width, 5))
    pygame.font.init()
    font = pygame.font.Font(police, 20)
    score_text2 = font.render(f"Blue: {player2_score}", True, contraste2_color)
    score_text = font.render(f"Green: {player_score}", True, contraste2_color)
    screen.blit(score_text, (10, 10))
    screen.blit(score_text2, (10, 50))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
