import pygame as pg
import sys
import time as t

pg.init()
screen = pg.display.set_mode((900,700))
pg.display.set_caption("ultra mega pro hash++ clicker! ")
bg_colour = (135, 206, 235)

cookie = pg.image.load('hash+++.png').convert_alpha()
cookie_size = pg.transform.scale(cookie, (400, 400))

text = pg.font.Font(None, 80)
text_position = (200, 50)

score = 0
score_text = text.render(f"Score: {score}", True, (230,230,230))
score_pos = (550,150)

shop_button = pg.image.load('shop.png').convert_alpha()
shop_button = pg.transform.scale(shop_button, (100, 100))
shop_button_rect = shop_button.get_rect(topleft=(770, 20))

laugh_emoji = pg.image.load('laugh.png').convert_alpha()
laugh_emoji = pg.transform.scale(laugh_emoji, (300,300))

shop_text_size = pg.font.Font(None, 50)

in_shop = False

while True:
    screen.fill(bg_colour)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            
            if in_shop:
                
                in_shop = False
                
           
            else:
                
                if shop_button_rect.collidepoint(event.pos):
                    in_shop = True
                
               
                else:
                    cookie_rect = cookie_size.get_rect(topleft=(235, 250))
                    if cookie_rect.collidepoint(event.pos):
                        score += 1
                        score_text = text.render(f"Score: {score}", True, (230, 230, 230))
                        
                        cookie_size = pg.transform.scale(cookie, (500, 500))
                        
                        
                        screen.fill(bg_colour)
                        screen.blit(score_text, score_pos)
                        text_surface = text.render("bradar pls click!!!!", True, (230, 230, 230))
                        screen.blit(text_surface, text_position)
                        screen.blit(cookie_size, (185, 200))
                        screen.blit(shop_button, shop_button_rect.topleft)
                        
                        pg.display.flip()
                        t.sleep(0.1)
                        cookie_size = pg.transform.scale(cookie, (400, 400))

    
    if in_shop:
        
        screen.fill((50, 50, 50)) 
        shop_text = shop_text_size.render("nothing for your poor ahh bradar ", True, (255, 255, 255))
        shop_text_two = shop_text_size.render("click anywhere and go back rich!! ", True, (255, 255, 255))
        screen.blit(shop_text, (200, 300))
        screen.blit(shop_text_two, (200, 350))
        screen.blit(laugh_emoji, (300, 390))
    else:
        
        screen.blit(score_text, score_pos)
        text_surface = text.render("bradar pls click!!!!", True, (230, 230, 230))
        screen.blit(text_surface, text_position)
        screen.blit(cookie_size, (235, 250))
        screen.blit(shop_button, shop_button_rect.topleft)

    pg.display.flip()