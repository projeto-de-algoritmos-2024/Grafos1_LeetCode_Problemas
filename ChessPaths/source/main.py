import pygame

# CONFIGURAÇÕES DA TELA
pygame.init()
pygame.display.set_caption("ChessPaths")
LARGURA_TELA = 1000
ALTURA_TELA = 900
tela = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])
fonte = pygame.font.Font('assets/fonts/Monocraft-nerd-fonts-patched.ttf', 10)
fonte_grande = pygame.font.Font('assets/fonts/Monocraft-nerd-fonts-patched.ttf', 25)
timer = pygame.time.Clock()
fps = 60

# CONFIGURAÇÕES DO JOGO
pecas_brancas = ['torre', 'cavalo', 'bispo', 'dama', 'rei', 'bispo', 'cavalo', 'torre',
                 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

pecas_pretas = ['torre', 'cavalo', 'bispo', 'dama', 'rei', 'bispo', 'cavalo', 'torre',
                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']

loc_pretas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

loc_brancas = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
              (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

cap_brancas = []

cap_pretas = []

turn_step = 0

peca_selecionada = -1

movimentos_validos = []

rei_preto   = pygame.image.load('assets/pieces/rei_preto.png')
rei_preto   = pygame.transform.scale(rei_preto, (80, 80))
rei_preto_p = pygame.transform.scale(rei_preto, (45, 45))

dama_preta   = pygame.image.load('assets/pieces/dama_preta.png')
dama_preta   = pygame.transform.scale(dama_preta, (80, 80))
dama_preta_p = pygame.transform.scale(dama_preta, (45, 45))

bispo_preto   = pygame.image.load('assets/pieces/bispo_preto.png')
bispo_preto   = pygame.transform.scale(bispo_preto, (80, 80))
bispo_preto_p = pygame.transform.scale(bispo_preto, (45, 45))

cavalo_preto   = pygame.image.load('assets/pieces/cavalo_preto.png')
cavalo_preto   = pygame.transform.scale(cavalo_preto, (80, 80))
cavalo_preto_p = pygame.transform.scale(cavalo_preto, (45, 45))

torre_preta   = pygame.image.load('assets/pieces/torre_preta.png')
torre_preta   = pygame.transform.scale(torre_preta, (80, 80))
torre_preta_p = pygame.transform.scale(torre_preta, (45, 45))

peao_preto   = pygame.image.load('assets/pieces/peao_preto.png')
peao_preto   = pygame.transform.scale(peao_preto, (65, 65))
peao_preto_p = pygame.transform.scale(peao_preto, (45, 45))

rei_branco   = pygame.image.load('assets/pieces/rei_branco.png')
rei_branco   = pygame.transform.scale(rei_branco, (80, 80))
rei_branco_p = pygame.transform.scale(rei_branco, (45, 45))

dama_branca   = pygame.image.load('assets/pieces/dama_branca.png')
dama_branca   = pygame.transform.scale(dama_branca, (80, 80))
dama_branca_p = pygame.transform.scale(dama_branca, (45, 45))

bispo_branco   = pygame.image.load('assets/pieces/bispo_branco.png')
bispo_branco   = pygame.transform.scale(bispo_branco, (80, 80))
bispo_branco_p = pygame.transform.scale(bispo_branco, (45, 45))

cavalo_branco   = pygame.image.load('assets/pieces/cavalo_branco.png')
cavalo_branco   = pygame.transform.scale(cavalo_branco, (80, 80))
cavalo_branco_p = pygame.transform.scale(cavalo_branco, (45, 45))

torre_branca   = pygame.image.load('assets/pieces/torre_branca.png')
torre_branca   = pygame.transform.scale(torre_branca, (80, 80))
torre_branca_p = pygame.transform.scale(torre_branca, (45, 45))

peao_branco   = pygame.image.load('assets/pieces/peao_branco.png')
peao_branco   = pygame.transform.scale(peao_branco, (65, 65))
peao_branco_p = pygame.transform.scale(peao_branco, (45, 45))

imagens_brancas = [peao_branco, torre_branca, cavalo_branco, bispo_branco, dama_branca, rei_branco, bispo_branco, cavalo_branco, torre_branca]

imagens_pretas = [peao_preto, torre_preta, cavalo_preto, bispo_preto, dama_preta, rei_preto, bispo_preto, cavalo_preto, torre_preta]

imagens_brancas_p = [peao_branco_p, torre_branca_p, cavalo_branco_p, bispo_branco_p, dama_branca_p, rei_branco_p, bispo_branco_p, cavalo_branco_p, torre_branca_p]

imagens_pretas_p = [peao_preto_p, torre_preta_p, cavalo_preto_p, bispo_preto_p, dama_preta_p, rei_preto_p, bispo_preto_p, cavalo_preto_p, torre_preta_p]

lista_pecas = ['peao', 'torre', 'cavalo', 'bispo', 'dama', 'rei']

# FUNÇÕES
def desenharTabuleiro():
    pygame.draw.rect(tela, 'purple4', [0, 0, 800, 800])
    for i in range(32):
        coluna = i%4
        linha = i//4
        if linha%2 == 0:
            pygame.draw.rect(tela, 'light grey', [600 - (coluna*200), linha * 100, 100, 100])
        else:
            pygame.draw.rect(tela, 'light grey', [700 - (coluna*200), linha * 100, 100, 100])
        pygame.draw.rect(tela, 'black', [0, 800, 800, 100])
        pygame.draw.rect(tela, 'black', [0, 800, LARGURA_TELA, 100], 5)
        pygame.draw.rect(tela, 'black', [800, 0, 200, ALTURA_TELA], 5)

        textos_turn_step = ['Brancas: Selecione uma peça', 'Brancas: Selecione um destino',
                            'Pretas: Selecione uma peça', 'Pretas: Selecione um destino']
        
        tela.blit(fonte_grande.render(textos_turn_step[turn_step], True, 'lightskyblue2'), (10, 810))
        
        if turn_step == 1:
            tela.blit(fonte_grande.render(pecas_brancas[peca_selecionada], True, 'lightskyblue2'), (10, 840))
        elif turn_step == 3:
            tela.blit(fonte_grande.render(pecas_pretas[peca_selecionada], True, 'lightskyblue2'), (10, 840))


def desenharPecas():
    for i in range(len(pecas_brancas)):
        index = lista_pecas.index(pecas_brancas[i])
        if pecas_brancas[i] == 'peao':
            tela.blit(peao_branco, (loc_brancas[i][0]*100+19, loc_brancas[i][1]*100+30))
        else:
            tela.blit(imagens_brancas[index], (loc_brancas[i][0]*100+10, loc_brancas[i][1]*100+10))
        if turn_step < 2:
            if peca_selecionada == i:
                pygame.draw.rect(tela, 'violetred', [loc_brancas[i][0]*100, loc_brancas[i][1]*100, 100, 100], 5)


    for i in range(len(pecas_pretas)):
        index = lista_pecas.index(pecas_pretas[i])
        if pecas_pretas[i] == 'peao':
            tela.blit(peao_preto, (loc_pretas[i][0]*100+19, loc_pretas[i][1]*100+30))
        else:
            tela.blit(imagens_pretas[index], (loc_pretas[i][0]*100+10, loc_pretas[i][1]*100+10))
        if turn_step >= 2:
            if peca_selecionada == i:
                pygame.draw.rect(tela, 'violetred', [loc_pretas[i][0]*100, loc_pretas[i][1]*100, 100, 100], 5)

def checkOp():
    pass

# GAME LOOP
run = True
while run:
    timer.tick(fps)
    tela.fill('dark gray')
    desenharTabuleiro()
    desenharPecas()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)

            if turn_step < 2:
                if click_coord in loc_brancas:
                    peca_selecionada = loc_brancas.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in movimentos_validos and peca_selecionada != -1:
                    loc_brancas[peca_selecionada] = click_coord
                    if click_coord in loc_pretas:
                        peca_preta = loc_pretas.index(click_coord)
                        cap_brancas.append(pecas_pretas[peca_preta])
                        pecas_pretas.pop(peca_preta)
                        loc_pretas.pop(peca_preta)
                    op_brancas = checkOp(pecas_pretas, loc_pretas, 'p')
                    op_pretas = checkOp(pecas_brancas, loc_brancas, 'b')
                    turn_step = 2
                    peca_selecionada = -1
                    movimentos_validos = []
            if turn_step >= 2:
                if click_coord in loc_pretas:
                    peca_selecionada = loc_pretas.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in movimentos_validos and peca_selecionada != -1:
                    loc_pretas[peca_selecionada] = click_coord
                    if click_coord in loc_brancas:
                        pecas_brancas = loc_brancas.index(click_coord)
                        cap_pretas.append(pecas_brancas[pecas_brancas])
                        pecas_brancas.pop(pecas_brancas)
                        loc_brancas.pop(pecas_brancas)
                    op_pretas = checkOp(pecas_brancas, loc_brancas, 'b')
                    op_brancas = checkOp(pecas_pretas, loc_pretas, 'p')
                    turn_step = 0
                    peca_selecionada = -1
                    movimentos_validos = []


    pygame.display.flip()
pygame.quit()