import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('BoxCat.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

largura = 640
altura = 480
x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_maca = randint(40,600)
y_maca = randint(50,430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('jogo Dos Quadrados')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if pygame.key.get_pressed()[K_a]:
            x_cobra = x_cobra-20
        if pygame.key.get_pressed()[K_d]:
            x_cobra = x_cobra + 20
        if pygame.key.get_pressed()[K_w]:
            y_cobra = y_cobra - 20
        if pygame.key.get_pressed()[K_s]:
            y_cobra = y_cobra + 20
            
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        barulho_colisao.play()
    
    tela.blit(texto_formatado, (455,40))
    pygame.display.update()