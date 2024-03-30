from pygame import *
from random import randint,shuffle,choice
W,H = 900, 550

import os
window = display.set_mode((W,H))
background = image.load('releaseProject\\releaseProject\\img\\newtable.jpg')
clock = time.Clock()
cards_bg = image.load('releaseProject\\releaseProject\\img\\BackgroundBlack.png')

init()
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y,name=''):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
        self.name = name
        

    def draw(self): 
        window.blit(self.image, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Player(GameSprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.cards = []

    def to_get_a_card(self, cards):
        shuffle(cards)
        card = choice(cards)
        self.cards.append(card)
        return card

    
take_card_img = image.load('releaseProject\\releaseProject\\img\\new_take_card.png')
menu_bg = image.load('releaseProject\\releaseProject\\img\\Знімок екрана 2024-03-30 171306.png')

take_card = GameSprite(take_card_img,100,50,650,275)

play_btn_img = image.load('releaseProject\\releaseProject\\img\\play_btn.png')
play_img = GameSprite(play_btn_img,200,100,350,100)
quit_btn_img = image.load('releaseProject\\releaseProject\\img\\quit_img.png')
quit_img = GameSprite(quit_btn_img,200,100,350,250) 
settings_btn_img = image.load('releaseProject\\releaseProject\\img\\settings_btn.png')
settings_img = GameSprite(settings_btn_img,200,100,350,400)

volume_up_img = image.load('releaseProject\\releaseProject\\img\\Знімок екрана 2024-03-30 172444.png')
volume_down_img = image.load('releaseProject\\releaseProject\\img\\Знімок екрана 2024-03-30 172450.png')

volume_down = GameSprite(volume_down_img,100,100,350,200)
volume_up = GameSprite(volume_up_img,100,100,500,200)




club_2_img = image.load('releaseProject\\releaseProject\\img\\club_2.png')
club_2 = GameSprite(club_2_img,50,50,450,300,name='club_2')
club_3_img = image.load('releaseProject\\releaseProject\\img\\club_3.png')
club_3 = GameSprite(club_3_img,50,50,450,300,name='club_3')
club_4_img = image.load('releaseProject\\releaseProject\\img\\club_4.png')
club_4 = GameSprite(club_4_img,50,50,450,300,name='club_4')
club_5_img = image.load('releaseProject\\releaseProject\\img\\club_5.png')
club_5 = GameSprite(club_5_img,50,50,450,300,name='club_5')
club_6_img = image.load('releaseProject\\releaseProject\\img\\club_6.png')
club_6 = GameSprite(club_6_img,50,50,450,300,name='club_6')
club_7_img = image.load('releaseProject\\releaseProject\\img\\club_7.png')
club_7 = GameSprite(club_7_img,50,50,450,300,name='club_7')
club_8_img = image.load('releaseProject\\releaseProject\\img\\club_8.png')
club_8 = GameSprite(club_8_img,50,50,450,300,name='club_8')
club_9_img = image.load('releaseProject\\releaseProject\\img\\club_9.png')
club_9 = GameSprite(club_9_img,50,50,450,300,name='club_9')
club_10_img = image.load('releaseProject\\releaseProject\\img\\club_10.png')
club_10 =GameSprite(club_10_img,50,50,450,300,name='club_10')
club_A_img = image.load('releaseProject\\releaseProject\\img\\club_A.png')
club_A = GameSprite(club_A_img,50,50,450,300,name='club_A')
club_J_img = image.load('releaseProject\\releaseProject\\img\\club_J.png')
club_J = GameSprite(club_J_img,50,50,450,300,name='club_J')
club_K_img = image.load('releaseProject\\releaseProject\\img\\club_K.png')
club_K = GameSprite(club_K_img,50,50,450,300,name='club_K')
club_Q_img = image.load('releaseProject\\releaseProject\\img\\club_Q.png')
club_Q = GameSprite(club_Q_img,50,50,450,300,name='club_Q')


# ##############################3
diamond_2_img = image.load('releaseProject\\releaseProject\\img\\Diamond_2.png')
diamond_2 = GameSprite(diamond_2_img,50,50,450,300,name='diamond_2')
diamond_3_img = image.load('releaseProject\\releaseProject\\img\\Diamond_3.png')
diamond_3 = GameSprite(diamond_3_img,50,50,450,300,name='diamond_3')
diamond_4_img = image.load('releaseProject\\releaseProject\\img\\Diamond_4.png')
diamond_4 = GameSprite(diamond_4_img,50,50,450,300,name='diamond_4')
diamond_5_img = image.load('releaseProject\\releaseProject\\img\\Diamond_5.png')
diamond_5 = GameSprite(diamond_5_img,50,50,450,300,name='diamond_5')
diamond_6_img = image.load('releaseProject\\releaseProject\\img\\Diamond_6.png')
diamond_6 = GameSprite(diamond_6_img,50,50,450,300,name='diamond_6')
diamond_7_img = image.load('releaseProject\\releaseProject\\img\\Diamond_7.png')
diamond_7 = GameSprite(diamond_7_img,50,50,450,300,name='diamond_7')
diamond_8_img = image.load('releaseProject\\releaseProject\\img\\Diamond_8.png')
diamond_8= GameSprite(diamond_8_img,50,50,450,300,name='diamond_8')
diamond_9_img = image.load('releaseProject\\releaseProject\\img\\Diamond_9.png')
diamond_9 = GameSprite(diamond_9_img,50,50,450,300,name='diamond_9')
diamond_10_img = image.load('releaseProject\\releaseProject\\img\\Diamond_10.png',)
diamond_10 =GameSprite(diamond_10_img,50,50,450,300,name='diamond_10')
diamond_A_img = image.load('releaseProject\\releaseProject\\img\\Diamond_A.png')
diamond_A = GameSprite(diamond_A_img,50,50,450,300,name='diamond_A')
diamond_J_img = image.load('releaseProject\\releaseProject\\img\\Diamond_J.png')
diamond_J = GameSprite(diamond_J_img,50,50,450,300,name='diamond_J')
diamond_K_img = image.load('releaseProject\\releaseProject\\img\\Diamond_K.png')
diamond_K = GameSprite(diamond_K_img,50,50,450,300,name='diamond_K')
diamond_Q_img = image.load('releaseProject\\releaseProject\\img\\Diamond_Q.png')
diamond_Q = GameSprite(diamond_Q_img,50,50,450,300,name='diamond_Q')


# ################################3
heart_2_img = image.load('releaseProject\\releaseProject\\img\\Heart_2.png')
heart_2 = GameSprite(heart_2_img,50,50,450,300,name='heart_2')
heart_3_img = image.load('releaseProject\\releaseProject\\img\\Heart_3.png')
heart_3 = GameSprite(heart_3_img,50,50,450,300,name='heart_3')
heart_4_img = image.load('releaseProject\\releaseProject\\img\\Heart_4.png')
heart_4 = GameSprite(heart_4_img,50,50,450,300,name='heart_4')
heart_5_img = image.load('releaseProject\\releaseProject\\img\\Heart_5.png')
heart_5 = GameSprite(heart_5_img,50,50,450,300,name='heart_5')
heart_6_img = image.load('releaseProject\\releaseProject\\img\\Heart_6.png')
heart_6 = GameSprite(heart_6_img,50,50,450,300,name='heart_6')
heart_7_img = image.load('releaseProject\\releaseProject\\img\\Heart_7.png')
heart_7 = GameSprite(heart_7_img,50,50,450,300,name='heart_7')
heart_8_img = image.load('releaseProject\\releaseProject\\img\\Heart_8.png')
heart_8 = GameSprite(heart_8_img,50,50,450,300,name='heart_8')
heart_9_img = image.load('releaseProject\\releaseProject\\img\\Heart_9.png')
heart_9 = GameSprite(heart_9_img,50,50,450,300,name='heart_9')
heart_10_img = image.load('releaseProject\\releaseProject\\img\\Heart_10.png')
heart_10 =GameSprite(heart_10_img,50,50,450,300,name='heart_10')
heart_A_img = image.load('releaseProject\\releaseProject\\img\\Heart_A.png')
heart_A = GameSprite(heart_A_img,50,50,450,300,name='heart_A')
heart_J_img = image.load('releaseProject\\releaseProject\\img\\Heart_J.png')
heart_J = GameSprite(heart_J_img,50,50,450,300,name='heart_J')
heart_K_img = image.load('releaseProject\\releaseProject\\img\\Heart_K.png')
heart_K = GameSprite(heart_K_img,50,50,450,300,name='heart_K')
heart_Q_img = image.load('releaseProject\\releaseProject\\img\\Heart_Q.png')
heart_Q = GameSprite(heart_Q_img,50,50,450,300,name='heart_Q')

# $####################################
spade_2_img = image.load('releaseProject\\releaseProject\\img\\spade_2.png')
spade_2 = GameSprite(spade_2_img,50,50,450,300,name='spade_2')
spade_3_img = image.load('releaseProject\\releaseProject\\img\\spade_3.png')
spade_3 = GameSprite(spade_3_img,50,50,450,300,name='spade_3')
spade_4_img = image.load('releaseProject\\releaseProject\\img\\spade_4.png') 
spade_4 = GameSprite(spade_4_img,50,50,450,300,name='spade_4')
spade_5_img = image.load('releaseProject\\releaseProject\\img\\spade_5.png')
spade_5 = GameSprite(spade_5_img,50,50,450,300,name='spade_5')
spade_6_img = image.load('releaseProject\\releaseProject\\img\\spade_6.png')
spade_6 = GameSprite(spade_6_img,50,50,450,300,name='spade_6')
spade_7_img = image.load('releaseProject\\releaseProject\\img\\spade_7.png')
spade_7 = GameSprite(spade_7_img,50,50,450,300,name='spade_7')
spade_8_img = image.load('releaseProject\\releaseProject\\img\\spade_8.png')
spade_8 = GameSprite(spade_8_img,50,50,450,300,name='spade_8')
spade_9_img = image.load('releaseProject\\releaseProject\\img\\spade_9.png')
spade_9 = GameSprite(spade_9_img,50,50,450,300,name='spade_9')
spade_10_img = image.load('releaseProject\\releaseProject\\img\\spade_10.png')
spade_10 =GameSprite(spade_10_img,50,50,450,300,name='spade_10')
spade_A_img = image.load('releaseProject\\releaseProject\\img\\spade_A.png')
spade_A = GameSprite(spade_A_img,50,50,450,300,name='spade_A')
spade_J_img = image.load('releaseProject\\releaseProject\\img\\spade_J.png')
spade_J = GameSprite(spade_J_img,50,50,450,300,name='spade_J')
spade_K_img = image.load('releaseProject\\releaseProject\\img\\spade_K.png')
spade_K = GameSprite(spade_K_img,50,50,450,300,name='spade_K')
spade_Q_img = image.load('releaseProject\\releaseProject\\img\\spade_Q.png')
spade_Q = GameSprite(spade_Q_img,50,50,450,300,name='spade_Q')



cards = [club_2,club_3,club_4,
club_5,
club_6,
club_7,
club_8,
club_9,
club_10,
club_A,
club_J,
club_K,
club_Q,
diamond_2,
diamond_3,
diamond_8,
diamond_5,
diamond_6,
diamond_7,
diamond_9,
diamond_10,
diamond_A,
diamond_J,
diamond_K,
diamond_Q,
heart_2,
heart_3,
heart_4,
heart_5,
heart_6,
heart_7,
heart_8,
heart_9,
heart_10,
heart_A,
heart_J,
heart_K,
heart_Q,
spade_2,
spade_3,
spade_4,
spade_5,
spade_6,
spade_7,
spade_8,
spade_9,
spade_10,
spade_A,
spade_J,
spade_K,
spade_Q]
def calculate_score(cards):
    global score 
    score = 0
    for card in cards:

        if  card.name == 'diamond_A' or card.name == 'heart_A' or card.name == 'spade_A':
            if score > 10:
                score += 1
            else:
                score += 11

        if card.name == 'club_2' or card.name == 'diamond_2' or card.name == 'heart_2' or card.name == 'spade_2':
            score += 2
        if card.name == 'club_3' or card.name == 'diamond_3' or card.name == 'heart_3' or card.name == 'spade_3':
            score += 3
        if card.name == 'club_4' or card.name == 'diamond_4' or card.name == 'heart_4' or card.name == 'spade_4':
            score += 4
        if card.name == 'club_5' or card.name == 'diamond_5' or card.name == 'heart_5' or card.name == 'spade_5':
            score += 5
        if card.name == 'club_6' or card.name == 'diamond_6' or card.name == 'heart_6' or card.name == 'spade_6':
            score += 6
   
        if card.name == 'club_7' or card.name == 'diamond_7' or card.name == 'heart_7' or card.name == 'spade_7':
            score += 7
        if card.name == 'club_8' or card.name == 'diamond_8' or card.name == 'heart_8' or card.name == 'spade_8':
            score += 8
        if card.name == 'club_9' or card.name == 'diamond_9' or card.name == 'heart_9' or card.name == 'spade_9':
            score += 9
        if card.name == 'club_10' or card.name == 'diamond_10' or card.name == 'heart_10' or card.name == 'spade_10':
            score += 10
        if card.name == 'club_J' or card.name == 'diamond_J' or card.name == 'heart_J' or card.name == 'spade_J':
            score += 10
        if card.name == 'club_K' or card.name == 'diamond_K' or card.name == 'heart_K' or card.name == 'spade_K':
            score += 10
        if card.name == 'club_Q' or card.name == 'diamond_Q' or card.name == 'heart_Q' or card.name == 'spade_Q':
            score += 10
   
    while score > 21 :
        score -= 10

    return score

def start_game():
    global player_cards, dealer_cards, player_score, dealer_score, cards
    player_cards.clear()
    dealer_cards.clear()
    player_score = 0
    dealer_score = 0
    


FPS = 60
display.set_caption('BlackJack')
font.init()
f1 = font.SysFont('Arial',24)
pressed_keys = key.get_pressed()


player = Player(cards_bg, 50, 50, 50, H*0.25)
dealer = Player(cards_bg, 50, 50, 50, H*0.25)

number = randint(1,2)





mixer.init()
mixer.music.load('releaseProject\\releaseProject\\img\\the-best-jazz-club-in-new-orleans-164472.mp3')
volume = 0.25
mixer.music.set_volume(volume)
mixer.music.play()





player_cards = []
dealer_cards = []
player_score = 0
dealer_score = 0
score = 0
screen = 'menu'
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if screen == 'menu':
            window.blit(menu_bg,(0,0))
            play_img.draw()
            quit_img.draw()
            settings_img.draw()
             
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if play_img.rect.collidepoint(e.pos):
                        
                        screen = 'game'
                    elif quit_img.rect.collidepoint(e.pos):
                        quit()
                    elif settings_img.rect.collidepoint(e.pos):
                        
                        screen = 'settings'

        if screen == 'settings':
            window.blit(menu_bg,(0,0))
            settigns_text = f"Ви знаходитесь в налаштуваннях"
            f5 = font.SysFont('Arial',36)
            dealer_text_surface = f5.render(settigns_text, True, (0, 0, 0))
            window.blit(dealer_text_surface, (270,50))
            volume_text = f'Звуки гри'
            volume_text_surface = f5.render(volume_text, True, (0, 0, 0))
            window.blit(volume_text_surface,(350,150))
            volume_up.draw()
            volume_down.draw()
            for e in event.get():
                if e.type == MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if volume_up.collidepoint(e.pos):
                            mixer_music.set_volume(volume+0.10)
                        elif volume_down.collidepoint(e.pos):
                            mixer_music.set_volume(volume-0.10)


            rules_text = "Натисни 'E' щоб побачити ігрові правила"
            rules_text_surface = f5.render(rules_text, True, (0, 0, 0))
            window.blit(rules_text_surface, (250, 500))
            if key.get_pressed()[K_e]:
       
                rules_surface = f1.render('''Задача гри - якнайшвидше дістатися до 21 очка але важливо не 
                                          перебрати за 21 очко . ''', True, (0, 0, 0))
                rules_surface2 = f1.render("Якщо гравець має більше ніж 21, то він автоматично програв", True, (0, 0, 0))
                window.blit(rules_surface, (200, 300))
                window.blit(rules_surface2, (200, 320))

        if screen == 'game':
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if len(player_cards) < 3 and take_card.rect.collidepoint(e.pos): 
                        player_card = player.to_get_a_card(cards)
                        cards.remove(player_card)
                        player_cards.append(player_card)
                        player_score = calculate_score(player_cards)
        
            window.blit(background, (0, 0))
            take_card.draw()

            
            card_x = W // 2 - 60
            card_y = H - 250
            for card in player_cards:
                card.rect.x = card_x
                card.rect.y = card_y
                card.draw()
                card_x += 60

            player_text = f"Player Score: {player_score}"
            player_text_surface = f1.render(player_text, True, (255, 255, 255))
            window.blit(player_text_surface, (20, 20))

            time.delay(250)
            if len(dealer_cards) < 2:
                dealer_card = dealer.to_get_a_card(cards)
                dealer_cards.append(dealer_card)
                dealer_score = calculate_score(dealer_cards)
                
            time.delay(250)



            card_x = W // 2 - 60
            card_y = H-395
            for card in dealer_cards:
                card.rect.x = card_x
                card.rect.y = card_y
                card.draw()
                card_x += 60

            dealer_text = f"Dealer Score: {dealer_score}"
            dealer_text_surface = f1.render(dealer_text, True, (255, 255, 255))
            window.blit(dealer_text_surface, (20, 50))
            if dealer_score == 21:
                window.blit(menu_bg,(0,0))
                dealer_text = f"Dealer Wins"
                dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                window.blit(dealer_text_surface, (300,300))
                time.delay(3000)
                start_game()
            if player_score == 21:
                
                dealer_text = f"Player Wins"
                dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                window.blit(dealer_text_surface, (300,300))
                time.delay(3000)
                start_game()
            if player_score > 21:
                
                dealer_text = f"Dealer Wins"
                dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                window.blit(dealer_text_surface, (300,300))
                time.delay(3000)
                start_game()
            if dealer_score > 21:
                
                dealer_text = f"Dealer Wins"
                dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                window.blit(dealer_text_surface, (300,300))
                time.delay(3000)
                start_game()
            if len(dealer_cards) == 2 and len(player_cards) == 2 or len(player_cards) == 3 or player_score > 18:
                if dealer_score < player_score:
                    dealer_text = f"Player Wins"
                    dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                    window.blit(dealer_text_surface, (300,300))
                    time.delay(3000)
                    start_game()
                else:
                    if len(player_cards) == 3 and player_score < dealer_score:
                        dealer_text = f"Dealer Wins"
                        dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                        window.blit(dealer_text_surface, (300,300))
                        time.delay(3000)
                        start_game()
                    if player_score == dealer_score:
                        dealer_text = f"Draw"
                        dealer_text_surface = f5.render(dealer_text, True, (255, 255, 255))
                        window.blit(dealer_text_surface, (300,300))
                        time.delay(3000)
                        start_game()





    display.update()
    clock.tick(FPS)
