import pygame

# CONFIGURAÇÕES DA TELA
pygame.init()
pygame.display.set_caption("ChessPaths")
LARGURA_TELA = 1000
ALTURA_TELA = 900
tela = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])
fonte = pygame.font.Font('../assets/fonts/Monocraft-nerd-fonts-patched.ttf', 20)
fonte_grande = pygame.font.Font('../assets/fonts/Monocraft-nerd-fonts-patched.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# CONFIGURAÇÕES DO JOGO
pecas_brancas = ['torre', 'cavalo', 'bispo', 'dama', 'rei', 'bispo', 'cavalo', 'torre',
                 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

pecas_pretas = ['torre', 'cavalo', 'bispo', 'dama', 'rei', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

loc_brancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

loc_pretas = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

cap_brancas = []

cap_pretas = []

turn_step = 0

peca_selecionada = -1

movimentos_validos = []

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

imagens_brancas = [peao_branco, torre_branca, cavalo_branco, bispo_branco, dama_branca, rei_branco, bispo_branco, cavalo_branco, torre_branca]

imagens_pretas = [peao_preto, torre_preta, cavalo_preto, bispo_preto, dama_preta, rei_preto, bispo_preto, cavalo_preto, torre_preta]

imagens_brancas_p = [peao_branco_p, torre_branca_p, cavalo_branco_p, bispo_branco_p, dama_branca_p, rei_branco_p, bispo_branco_p, cavalo_branco_p, torre_branca_p]

imagens_pretas_p = [peao_preto_p, torre_preta_p, cavalo_preto_p, bispo_preto_p, dama_preta_p, rei_preto_p, bispo_preto_p, cavalo_preto_p, torre_preta_p]

lista_pecas = ['peao', 'torre', 'cavalo', 'bispo', 'dama', 'rei']

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