import pygame

rei_preto   = pygame.image.load('../assets/pieces/rei_preto.png')
rei_preto   = pygame.transform.scale(rei_preto, (80, 80))
rei_preto_p = pygame.transform.scale(rei_preto, (45, 45))

dama_preta   = pygame.image.load('../assets/pieces/dama_preta.png')
dama_preta   = pygame.transform.scale(dama_preta, (80, 80))
dama_preta_p = pygame.transform.scale(dama_preta, (45, 45))

bispo_preto   = pygame.image.load('../assets/pieces/bispo_preto.png')
bispo_preto   = pygame.transform.scale(bispo_preto, (80, 80))
bispo_preto_p = pygame.transform.scale(bispo_preto, (45, 45))

cavalo_preto   = pygame.image.load('../assets/pieces/cavalo_preto.png')
cavalo_preto   = pygame.transform.scale(cavalo_preto, (80, 80))
cavalo_preto_p = pygame.transform.scale(cavalo_preto, (45, 45))

torre_preta   = pygame.image.load('../assets/pieces/torre_preta.png')
torre_preta   = pygame.transform.scale(torre_preta, (80, 80))
torre_preta_p = pygame.transform.scale(torre_preta, (45, 45))

peao_preto   = pygame.image.load('../assets/pieces/peao_preto.png')
peao_preto   = pygame.transform.scale(peao_preto, (80, 80))
peao_preto_p = pygame.transform.scale(peao_preto, (45, 45))

rei_branco   = pygame.image.load('../assets/pieces/rei_branco.png')
rei_branco   = pygame.transform.scale(rei_branco, (80, 80))
rei_branco_p = pygame.transform.scale(rei_branco, (45, 45))

dama_branca   = pygame.image.load('../assets/pieces/dama_branca.png')
dama_branca   = pygame.transform.scale(dama_branca, (80, 80))
dama_branca_p = pygame.transform.scale(dama_branca, (45, 45))

bispo_branco   = pygame.image.load('../assets/pieces/bispo_branco.png')
bispo_branco   = pygame.transform.scale(bispo_branco, (80, 80))
bispo_branco_p = pygame.transform.scale(bispo_branco, (45, 45))

cavalo_branco   = pygame.image.load('../assets/pieces/cavalo_branco.png')
cavalo_branco   = pygame.transform.scale(cavalo_branco, (80, 80))
cavalo_branco_p = pygame.transform.scale(cavalo_branco, (45, 45))

torre_branca   = pygame.image.load('../assets/pieces/torre_branca.png')
torre_branca   = pygame.transform.scale(torre_branca, (80, 80))
torre_branca_p = pygame.transform.scale(torre_branca, (45, 45))

peao_branco   = pygame.image.load('../assets/pieces/peao_branco.png')
peao_branco   = pygame.transform.scale(peao_branco, (80, 80))
peao_branco_p = pygame.transform.scale(peao_branco, (45, 45))

pygame.init()
pygame.display.set_caption("ChessPaths")
LARGURA_TELA = 1000
ALTURA_TELA = 900
tela = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])
fonte = pygame.font.Font('../assets/fonts/Monocraft-nerd-fonts-patched.ttf', 20)
fonte_grande = pygame.font.Font('../assets/fonts/Monocraft-nerd-fonts-patched.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# GAME LOOP

run = True
while run:
    timer.tick(fps)
    tela.fill('dark gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()