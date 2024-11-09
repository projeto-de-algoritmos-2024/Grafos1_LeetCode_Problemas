import pygame
import grafoEL

# CONFIGURAÇÕES DA TELA
pygame.init()
pygame.display.set_caption('ChessPaths')
LARGURA_TELA = 1000
ALTURA_TELA = 900
tela = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])
fonte = pygame.font.Font('ChessPaths/assets/fonts/Monocraft-nerd-fonts-patched.ttf', 10)
fonte_grande = pygame.font.Font('ChessPaths/assets/fonts/Monocraft-nerd-fonts-patched.ttf', 25)
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

peca_selecionada = 100

cavalo_selecionado = False
mostrar_caminho = False
cavalo_pos_xy = (-1,-1)
cavalo_dtn_xy = (-1,-1)

movimentos_validos = []

rei_preto   = pygame.image.load('ChessPaths/assets/pieces/rei_preto.png')
rei_preto   = pygame.transform.scale(rei_preto, (80, 80))
rei_preto_p = pygame.transform.scale(rei_preto, (45, 45))

dama_preta   = pygame.image.load('ChessPaths/assets/pieces/dama_preta.png')
dama_preta   = pygame.transform.scale(dama_preta, (80, 80))
dama_preta_p = pygame.transform.scale(dama_preta, (45, 45))

bispo_preto   = pygame.image.load('ChessPaths/assets/pieces/bispo_preto.png')
bispo_preto   = pygame.transform.scale(bispo_preto, (80, 80))
bispo_preto_p = pygame.transform.scale(bispo_preto, (45, 45))

cavalo_preto   = pygame.image.load('ChessPaths/assets/pieces/cavalo_preto.png')
cavalo_preto   = pygame.transform.scale(cavalo_preto, (80, 80))
cavalo_preto_p = pygame.transform.scale(cavalo_preto, (45, 45))

torre_preta   = pygame.image.load('ChessPaths/assets/pieces/torre_preta.png')
torre_preta   = pygame.transform.scale(torre_preta, (80, 80))
torre_preta_p = pygame.transform.scale(torre_preta, (45, 45))

peao_preto   = pygame.image.load('ChessPaths/assets/pieces/peao_preto.png')
peao_preto   = pygame.transform.scale(peao_preto, (65, 65))
peao_preto_p = pygame.transform.scale(peao_preto, (45, 45))

rei_branco   = pygame.image.load('ChessPaths/assets/pieces/rei_branco.png')
rei_branco   = pygame.transform.scale(rei_branco, (80, 80))
rei_branco_p = pygame.transform.scale(rei_branco, (45, 45))

dama_branca   = pygame.image.load('ChessPaths/assets/pieces/dama_branca.png')
dama_branca   = pygame.transform.scale(dama_branca, (80, 80))
dama_branca_p = pygame.transform.scale(dama_branca, (45, 45))

bispo_branco   = pygame.image.load('ChessPaths/assets/pieces/bispo_branco.png')
bispo_branco   = pygame.transform.scale(bispo_branco, (80, 80))
bispo_branco_p = pygame.transform.scale(bispo_branco, (45, 45))

cavalo_branco   = pygame.image.load('ChessPaths/assets/pieces/cavalo_branco.png')
cavalo_branco   = pygame.transform.scale(cavalo_branco, (80, 80))
cavalo_branco_p = pygame.transform.scale(cavalo_branco, (45, 45))

torre_branca   = pygame.image.load('ChessPaths/assets/pieces/torre_branca.png')
torre_branca   = pygame.transform.scale(torre_branca, (80, 80))
torre_branca_p = pygame.transform.scale(torre_branca, (45, 45))

peao_branco   = pygame.image.load('ChessPaths/assets/pieces/peao_branco.png')
peao_branco   = pygame.transform.scale(peao_branco, (65, 65))
peao_branco_p = pygame.transform.scale(peao_branco, (45, 45))

imagens_brancas = [peao_branco, dama_branca, rei_branco, cavalo_branco, torre_branca, bispo_branco]

imagens_pretas = [peao_preto, dama_preta, rei_preto, cavalo_preto, torre_preta, bispo_preto]

imagens_brancas_p = [peao_branco_p, dama_branca_p, rei_branco_p, cavalo_branco_p, torre_branca_p, bispo_branco_p]

imagens_pretas_p = [peao_preto_p, dama_preta_p, rei_preto_p, cavalo_preto_p, torre_preta_p, bispo_preto_p]

lista_pecas = ['peao', 'dama', 'rei', 'cavalo', 'torre', 'bispo']

clock = 0

vencedor = ''

game_over = False

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
        
        pygame.draw.rect(tela, 'gray20', [805, 805, 66, 66])
        pygame.draw.rect(tela, 'blue', [810, 810, 55, 55])
        tela.blit(fonte_grande.render('AMC', True, 'yellow'), (814, 820))

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

def checkOp(pecas, locs, vez):
    lista_movimentos = []
    todos_movimentos = []

    for i in range((len(pecas))):
        loc = locs[i]
        peca = pecas[i]
        if peca == 'peao':
            lista_movimentos = movimentoPeao(loc, vez)
        elif peca == 'cavalo':
            lista_movimentos = movimentoCavalo(loc, vez)
        elif peca == 'bispo':
            lista_movimentos = movimentoBispo(loc, vez)
        elif peca == 'torre':
            lista_movimentos = movimentoTorre(loc, vez)
        elif peca == 'dama':
            lista_movimentos = movimentoDama(loc, vez)
        elif peca == 'rei':
            lista_movimentos = movimentoRei(loc, vez)
        todos_movimentos.append(lista_movimentos)

    return todos_movimentos

def movimentoPeao(posicao, vez):
    lista_movimentos = []
    if vez == 'b':
        if (posicao[0], posicao[1] - 1) not in loc_brancas and (posicao[0], posicao[1] - 1) not in loc_pretas and posicao[1] > 0:
           lista_movimentos.append((posicao[0], posicao[1] - 1))
        if (posicao[0], posicao[1] - 2) not in loc_brancas and (posicao[0], posicao[1] - 2) not in loc_pretas and posicao[1] == 6:
           lista_movimentos.append((posicao[0], posicao[1] - 2))
        if (posicao[0] + 1, posicao[1] - 1) in loc_pretas:
           lista_movimentos.append((posicao[0] + 1, posicao[1] - 1))
        if (posicao[0] - 1, posicao[1] - 1) in loc_pretas:
           lista_movimentos.append((posicao[0] - 1, posicao[1] - 1))
    else:
        if (posicao[0], posicao[1] + 1) not in loc_brancas and (posicao[0], posicao[1] + 1) not in loc_pretas and posicao[1] < 7:
           lista_movimentos.append((posicao[0], posicao[1] + 1))
        if (posicao[0], posicao[1] + 2) not in loc_brancas and (posicao[0], posicao[1] + 2) not in loc_pretas and posicao[1] == 1:
           lista_movimentos.append((posicao[0], posicao[1] + 2))
        if (posicao[0] + 1, posicao[1] + 1) in loc_brancas:
           lista_movimentos.append((posicao[0] + 1, posicao[1] + 1))
        if (posicao[0] - 1, posicao[1] + 1) in loc_brancas:
           lista_movimentos.append((posicao[0] -1, posicao[1] + 1))
    
    return lista_movimentos

def movimentoCavalo(posicao, vez):
    lista_movimentos = []
    if vez == 'b':
        # lista_inimigos = loc_pretas
        lista_aliados = loc_brancas
    else:
        # lista_inimigos = loc_brancas
        lista_aliados = loc_pretas

    casas_possiveis = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (posicao[0] + casas_possiveis[i][0], posicao[1] + casas_possiveis[i][1])
        if target not in lista_aliados and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            lista_movimentos.append(target)

    return lista_movimentos

def movimentoBispo(posicao, vez):
    lista_movimentos = []
    if vez == 'b':
        lista_inimigos = loc_pretas
        lista_aliados = loc_brancas
    else:
        lista_inimigos = loc_brancas
        lista_aliados = loc_pretas
    
    for i in range(4):
        passagem_liberada = True
        cadeia = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        
        while passagem_liberada:
            if (posicao[0] + (cadeia * x), posicao[1] + (cadeia * y)) not in lista_aliados and 0 <= posicao[0] + (cadeia * x) <= 7 and 0 <= posicao[1] + (cadeia * y) <= 7:
                lista_movimentos.append((posicao[0] + (cadeia * x), posicao[1] + (cadeia * y)))
                if (posicao[0] + (cadeia * x), posicao[1] + (cadeia * y)) in lista_inimigos:
                    passagem_liberada = False
                cadeia += 1
            else:
                passagem_liberada = False
    
    return lista_movimentos

def movimentoTorre(posicao, vez):
    lista_movimentos = []
    if vez == 'b':
        lista_inimigos = loc_pretas
        lista_aliados = loc_brancas
    else:
        lista_inimigos = loc_brancas
        lista_aliados = loc_pretas
    for i in range(4):
        passagem_liberada = True
        cadeia = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while passagem_liberada:
            if (posicao[0] + (cadeia*x), posicao[1] + (cadeia*y)) not in lista_aliados and 0 <= posicao[0] + (cadeia*x) <= 7 and 0 <= posicao[1] + (cadeia*y) <= 7:
                lista_movimentos.append((posicao[0] + (cadeia * x), posicao[1] + (cadeia * y)))
                if (posicao[0] + (cadeia * x), posicao[1] + (cadeia * y)) in lista_inimigos:
                    passagem_liberada = False
                cadeia += 1
            else:
                passagem_liberada = False
    return lista_movimentos

def movimentoDama(posicao, vez):
    lista_movimentos = []
    bispo = movimentoBispo(posicao, vez)
    torre = movimentoTorre(posicao, vez)
    for i in range(len(bispo)):
        lista_movimentos.append(bispo[i])
    for i in range(len(torre)):
        lista_movimentos.append(torre[i])
    return lista_movimentos

def movimentoRei(posicao, vez):
    lista_movimentos = []
    if vez == 'b':
        # lista_inimigos = loc_pretas
        lista_aliados = loc_brancas
    else:
        # lista_inimigos = loc_brancas
        lista_aliados = loc_pretas

    casas_possiveis = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (posicao[0] + casas_possiveis[i][0], posicao[1] + casas_possiveis[i][1])
        if target not in lista_aliados and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            lista_movimentos.append(target)

    return lista_movimentos

def movimentosValidos():
    if turn_step < 2:
        opcoes = op_brancas
    else:
        opcoes = op_pretas
    opcoes_validas = opcoes[peca_selecionada]
    return opcoes_validas

def desenharMovimentosValidos(movimentos):
    for i in range(len(movimentos)):
        pygame.draw.rect(tela, 'violetred', pygame.Rect(movimentos[i][0] * 100 + 40, movimentos[i][1] * 100 + 40, 20, 20)
)

def desenharCoordenadas():
    n = 8
    l = 'a'
    for i in range(8):
        tela.blit(fonte_grande.render(l, True, 'grey50'), (100 * i + 80, 771))
        tela.blit(fonte_grande.render(str(n), True, 'grey50'), (3, 100 * i))
        n -= 1
        l = chr(ord(l) + 1)

def desenharCheque():
    if turn_step < 2:
        if 'rei' in pecas_brancas:
            index_rei = pecas_brancas.index('rei')
            loc_rei = loc_brancas[index_rei]
            for i in range(len(op_pretas)):
                if loc_rei in op_pretas[i]:
                    if clock < 15:
                        pygame.draw.rect(tela, 'red', [loc_brancas[index_rei][0]*100, loc_brancas[index_rei][1]*100, 100, 100], 5)
    else:
        if 'rei' in pecas_pretas:
            index_rei = pecas_pretas.index('rei')
            loc_rei = loc_pretas[index_rei]
            for i in range(len(op_brancas)):
                if loc_rei in op_brancas[i]:
                    if clock < 15:
                        pygame.draw.rect(tela, 'red', [loc_pretas[index_rei][0]*100, loc_pretas[index_rei][1]*100, 100, 100], 5)

def desenharGameOver():
    pygame.draw.rect(tela, 'black', [200, 200, 400, 200])
    tela.blit(fonte_grande.render(f'{vencedor} VENCERAM!', True, 'white'), (260, 210))
    tela.blit(fonte_grande.render(f'Pressione', True, 'white'), (325, 240))
    tela.blit(fonte_grande.render(f'ENTER', True, 'green'), (360, 270))
    tela.blit(fonte_grande.render(f'Para jogar novamente!', True, 'white'), (225, 300))

def desenharCapturadas():
    for i in range(len(cap_brancas)):
        captured_piece = cap_brancas[i]
        index = lista_pecas.index(captured_piece)
        tela.blit(imagens_pretas_p[index], (825, 5+50*i))
    for i in range(len(cap_pretas)):
        captured_piece = cap_pretas[i]
        index = lista_pecas.index(captured_piece)
        tela.blit(imagens_brancas_p[index], (925, 5+50*i))

def desenharCaminhoCavalo(caminho):
    for i, movimento in enumerate(caminho):
        if i == 0:
            tela.blit(fonte_grande.render('Caminho:', True, 'white'), (10, 870))
            continue
        
        pygame.draw.rect(tela, 'darkslategray4', pygame.Rect(movimento[1] * 100 + 40, movimento[0] * 100 + 40, 20, 20))
        coordenada = grafoEL.coordenadaParaCasa(movimento[1], movimento[0])

        pos_texto_x = i*100+100
        pos_texto_y = 870
        tela.blit(fonte_grande.render(coordenada, True, 'white'), (pos_texto_x, pos_texto_y))

# GAME LOOP
op_pretas = checkOp(pecas_pretas, loc_pretas, 'p')
op_brancas = checkOp(pecas_brancas, loc_brancas, 'b')
run = True
while run:
    timer.tick(fps)
    if clock < 30:
        clock += 1
    else:
        clock = 0
    tela.fill('dark gray')
    desenharTabuleiro()
    desenharPecas()
    desenharCapturadas()
    desenharCheque()
    desenharCoordenadas()
    if cavalo_selecionado and mostrar_caminho:
        desenharCaminhoCavalo(grafoEL.caminho_convertido)

    if peca_selecionada != 100:
        movimentos_validos = movimentosValidos()
        desenharMovimentosValidos(movimentos_validos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coord = (x_coord, y_coord)
            print(x_coord, y_coord)
            if turn_step < 2:
                if click_coord == (8, 8):
                    mostrar_caminho = not mostrar_caminho
                if click_coord in loc_brancas:
                    peca_selecionada = loc_brancas.index(click_coord)
                    if pecas_brancas[peca_selecionada] == 'cavalo' and not cavalo_selecionado:
                        cavalo_selecionado = True
                    elif pecas_brancas[peca_selecionada] != 'cavalo':
                        cavalo_selecionado = False
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in movimentos_validos and peca_selecionada != 100:
                    loc_brancas[peca_selecionada] = click_coord
                    if click_coord in loc_pretas:
                        peca_preta = loc_pretas.index(click_coord)
                        cap_brancas.append(pecas_pretas[peca_preta])
                        if pecas_pretas[peca_preta] == 'rei':
                            vencedor = 'BRANCAS'
                        pecas_pretas.pop(peca_preta)
                        loc_pretas.pop(peca_preta)
                    op_pretas = checkOp(pecas_pretas, loc_pretas, 'p')
                    op_brancas = checkOp(pecas_brancas, loc_brancas, 'b')
                    turn_step = 2
                    mostrar_caminho = False
                    peca_selecionada = 100
                    movimentos_validos = []
            if turn_step >= 2:
                if click_coord == (8, 8):
                    mostrar_caminho = not mostrar_caminho
                if click_coord in loc_pretas:
                    peca_selecionada = loc_pretas.index(click_coord)
                    if pecas_pretas[peca_selecionada] == 'cavalo' and not cavalo_selecionado:
                        cavalo_selecionado = True
                    elif pecas_pretas[peca_selecionada] != 'cavalo':
                        cavalo_selecionado = False
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in movimentos_validos and peca_selecionada != 100:
                    loc_pretas[peca_selecionada] = click_coord
                    if click_coord in loc_brancas:
                        peca_branca = loc_brancas.index(click_coord)
                        cap_pretas.append(pecas_brancas[peca_branca])
                        if pecas_brancas[peca_branca] == 'rei':
                            vencedor = 'PRETAS'
                        pecas_brancas.pop(peca_branca)
                        loc_brancas.pop(peca_branca)
                    op_pretas = checkOp(pecas_pretas, loc_pretas, 'p')
                    op_brancas = checkOp(pecas_brancas, loc_brancas, 'b')
                    turn_step = 0
                    mostrar_caminho = False
                    peca_selecionada = 100
                    movimentos_validos = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                vencedor = ''
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

                peca_selecionada = 100

                cavalo_selecionado = False
                mostrar_caminho = False

                movimentos_validos = []

                op_pretas = checkOp(pecas_pretas, loc_pretas, 'p')
                op_brancas = checkOp(pecas_brancas, loc_brancas, 'b')

    if vencedor != '':
        game_over = True
        desenharGameOver()

    pygame.display.flip()
pygame.quit()
## ESTAVEL