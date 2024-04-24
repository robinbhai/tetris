import pygame as p
import sys
from game import Game

p.init()

navy = (00,00,100)
white = (255,255,255)
grey =(211, 211, 211)
black = (0,0,0)
lightblack = p.Color(0,0,0,100)
#FONT
title_font = p.font.Font(None, 40)
line_font = p.font.Font(None, 30)
gameoverfont = p.font.Font(None, 30)
helpfont = p.font.Font(None, 25)

#score
score_surface = title_font.render("Score", True, white)
score_screen = p.Rect(320,55,170,60)
#next clock
next_block = title_font.render("Next Block", True , white)
next_block_screen = p.Rect(320,230, 170,170)
#lines count
line_surface = line_font.render("Lines Cleared", True, white)
line_screen = p.Rect(320,475,170,60)
#game over
game_over = gameoverfont.render("Game Over , Click any button to restart", True , black)
gameoverscreen = p.Rect(20,270,460,60)

helpmenu = helpfont.render("Press ESC for help", True, white)

#helpscreen
def helpscreen():
    p.draw.rect(game_screen, (0,100,0),[100,180,300,270],0,10)

#help
esc = helpfont.render("Esc for help",True, white)
left = helpfont.render("- A to move left",True, white)
right = helpfont.render("- D to move right",True, white)
down = helpfont.render("- S to move down",True, white)
rotate = helpfont.render("- W to rotate the block",True, white)
resume = helpfont.render("- Esc to resume the game",True, white)

def help():
    game_screen.blit(left , (120 , 200, 50 ,50))
    game_screen.blit(right , (120 , 250, 50 ,50))
    game_screen.blit(down , (120 , 300, 50 ,50))
    game_screen.blit(rotate , (120 , 350, 50 ,50))
    game_screen.blit(resume , (120 , 400, 50 ,50))


#screen
game_screen = p.display.set_mode((500,620))
p.display.set_caption("Tetris")




#clockspeed
clock = p.time.Clock()

game = Game()



falling_speed = 200
Game_flow = p.USEREVENT
p.time.set_timer(Game_flow, falling_speed)

def pause():
        paused = True
        
        while paused:      
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE :
                        paused = False
            helpscreen()
            help()
            p.display.update()
            p.mixer.music.pause()
        if paused == False:
            p.mixer.music.unpause()

            


        
#gameloop
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        #keyboard input
        if event.type == p.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.game_reset()
            elif event.key == p.K_a:
                game.left_move()
            elif event.key == p.K_d:
                game.right_move()
            elif event.key == p.K_s:
                game.down_move()
            elif event.key == p.K_w:
                game.rotate_block()
            elif event.key == p.K_ESCAPE:
                pause()
        
        if event.type == Game_flow and game.game_over == False:
            game.down_move()


    #score
    scored = title_font.render(str(game.score), True, black)

    lines_count= title_font.render(str(game.line), True, black)



    #display update
    game_screen.fill(black)
    game_screen.blit(score_surface , (370,20,50,50))
    p.draw.rect(game_screen, grey, score_screen , 0,10)
    game_screen.blit(scored , scored.get_rect(centerx = score_screen.centerx , centery = score_screen.centery))

    #next block
    game_screen.blit (next_block,(335, 200, 50, 50 ))
    p.draw.rect(game_screen , grey, next_block_screen ,0,10)

    #lines count
    game_screen.blit(line_surface , (335,450,50,50))
    p.draw.rect(game_screen, grey, line_screen , 0,10)
    game_screen.blit(lines_count , lines_count.get_rect(centerx = line_screen.centerx , centery = line_screen.centery))

    game_screen.blit(helpmenu , (330,580,50,50))
    

    #game over
    game.draw_blocks(game_screen)
    if game.game_over == True:
        p.draw.rect(game_screen, white , gameoverscreen ,0 , 10)
        game_screen.blit(game_over , (50 , 290, 50 ,50))
    p.display.update()
    clock.tick(60)