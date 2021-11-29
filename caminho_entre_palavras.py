############################################################################
## Nome do arquivo: caminho_entre_palavras.py                             ##
## Autor: IARA DE MELO DANTAS BEZERRA                                     ##
## Data: 18/07/2021                                                       ##
## Versão: 0.1                                                            ##
## Descrição: Consultar palavras semelhantes e o caminho entre palavras   ##
############################################################################

##################### FUNÇÕES ADICIONAIS ###################################

def extrairPalavras(fonte): # nome da função
    lista_palavras = [] # lista com as palavras

    arquivo = open(fonte, "r") # abrir o arquivo em modo de leitura
    for palavra in arquivo.readlines(): # percorrerá cada linha do arquivo
        # excluirá o caractere de 'enter / fim de linha' e adiciona a palavra na 'lista_palavras'
        lista_palavras.append(palavra[:-1])
    arquivo.close() # fecha o arquivo
    return sorted(lista_palavras) # retorna uma lista com as palavras em ordem alfabética


def testarExistencia(palavra, fonte): # nome da função - recebe a palavra e o arquivo das palavras
    if palavra not in fonte: # testa se a palavra NÃO é encontrada no vocabulário - inválida
        existe = 1
    else: # caso a palavra SEJA encotrada - válida
        existe = 0
    return existe # retorno 1 quando NÃO existe no arquivo e 0 quando existe


def menuOpcoes(): # nome da função - apenas imprime na tela as opções possiveis
    print("CAMINHO ENTRE PALAVRAS".center(30, "_"), "\n")
    print("1 - OPÇÃO 1: Consultar palavras semelhantes") # testar função obtemPalavrasProximas
    print("2 - opção 2: Consultar arvore de palavras") # testar função criaArvoreDeBusca
    print("3 - OPÇÃO 3: Verificar caminho") # testar função obtemCaminho
    print("0 - Encerrar programa")
    print("_".center(30, "_"), "\n")
    print("O tempo de execução pode levar alguns segundos")
    print("_".center(30, "_"), "\n")


##################################################
######### FUNÇÕES OBRIGATÓRIAS ###################


def obtemPalavrasProximas(palavra, vocabulario): # nome da função - opção 1

    # variaveis e listas necerrárias
    limite = len(palavra)
    palavras_semelhantes = []
    lista_temp = []

    # o vocabulario será percorrido e adicionadas palavras
    # que tenham o mesmo tamanho que a palavra inserida
    for p in vocabulario:
        if len(p) == limite:
            lista_temp.append(p)

    # variaveis de navegação - indice das letras nas palavras
    c_antecessor = 1 # demarcação de string - deve ser igual
    c_posterior = -limite # demarcação de string - deve ser igual
    c_indice = 0 # letra - indice da letra a ser verificado - deve ser diferente

    # loop de repetição até que c_indice seja igual ao limite
    while c_indice < limite:

        # Testará a existencia de cada elemento na lista semenlahntes
        for p in lista_temp:
            if p not in palavras_semelhantes:

                # se a palavra NÃO estiver na lista semelhantes, será verificada por seus indices
                if p[c_indice] != palavra[c_indice]: # se a letra é na posição c_indice é diferente
                    if p[c_antecessor:] == palavra[c_antecessor:]: # se os posteriores serão iguais
                        if p[:c_posterior] == palavra[:c_posterior]: # se os antecessores serão iguais

                            # caso a palavra seja diferente em apenas uma letra [da esquerda a direita]
                            # a palavra será adicionada à lista palavras_semelhantes
                            palavras_semelhantes.append(p) # adicionar semelhante

        # incrementação dos indices
        c_indice += 1
        c_posterior += 1
        c_antecessor += 1

    return palavras_semelhantes # retorna a lista das palavras próximas


def criaArvoreDeBusca(inicio, fim, vocabulario): # nome da função - opção 2

    ## VARIAVEIS E LISTAS USADAS NA FUNÇÃO
    semelhantes = obtemPalavrasProximas(inicio, vocabulario)
    limite = 0 # palavras possiveis - de mesmo tamanho
    l_p = []  # lista de palavras
    l_n = []  # lista de nos - numeros
    c_i = 0  # contador
    arvore = [[inicio, -1]] # a arvore já inicia com a a palavra pai - mesmo que não seja encontrada palavras semelhantes

    ## retorna um limite de palavras de mesmo tamnaho que a palavra inicio
    # se lista de semelhantes não estiver vazia
    if len(semelhantes) > 0:
        for palavra in vocabulario:
            if len(palavra) == len(inicio):
                limite += 1

    # se todas as listas zeradas, menos semelhantes
    # irá percorrer a lista semelhantes e caso o elemento seja igual ao fim o código não continuará
    if len(l_p) == 0 and len(l_n) == 0 and len(semelhantes) != 0:
        for p in semelhantes: # testa os elementos na lista semelhantes
            if p == fim:
                l_p.append(p)  # palavra
                l_n.append(c_i)  # indice do nó - 0
                break
            else:
                l_p.append(p)  # palavra
                l_n.append(c_i)  # indice do nó - 0


    # loop dependerá de limite - se houver palavras possiveis
    # repetirá no máximo 'limite' vezes
    for i in range(limite):

        # caso a palavra seja igual ao fim o loop para
        if fim in l_p:
            break

        else:
            # caso fim não tenha sido encontrado irá encontrar
            # palavras semelhantes para cada palavra na lista - palavras filhas
            for palavra in l_p:

                # será gerado outra lista de semelhantes para cada elemento [subnó]
                subno = obtemPalavrasProximas(palavra, vocabulario) # lista com palavras semelhantes a 'p'

                #print("SUBNO", subno) - descomentar se desejar acompanhar o código
                #print(c_i) - descomentar para acompanhar o código
                # [É INTERESSANTE ver a variavel ser incrementada]
                c_i += 1 # contador referente a posição do nó

                # se o tamanho do subnó é maior que 0 e o fim não esta nele,
                # as palavras serão adicionadas na lista e a busca continuará
                # e adicionará a palavra e o indice em suas respectivas listas
                if len(subno) > 0 and fim not in subno:
                    for subpalavra in subno:
                        if subpalavra not in l_p:
                            l_p.append(subpalavra)
                            l_n.append(c_i)

                # se o tamanho do subno foi maior que 0 e a palavra fim, estiver contida nele
                # a palavra será adicionada na lista geral e o código não continuará a busca
                elif len(subno) > 0 and fim in subno:
                    for subp in subno:
                        if subp == fim:
                            if subp not in l_p:
                                l_p.append(subp)
                                l_n.append(c_i)
                                break # para a busca

                        else:
                            if subp not in l_p:
                                l_p.append(subp)
                                l_n.append(c_i)
                    break # para a busca

    # Após o loop, será verificado a lista geral de palavras e
    # será vinculada as palavras e os nós na matriz 'arvore'
    for i in range(len(l_p)):
        if [l_p[i], l_n[i]] not in arvore and [l_p[i], l_n[i]] != [inicio, 1]: # testa a existencia na lista
            arvore.append([l_p[i], l_n[i]]) # adiciona na arvore

    return arvore # retorna uma lista com listas [palavra, nó]


def obtemCaminho(inicio, fim, vocabulario): # nome da função
    # Variaveis e listas necessárias
    arvore = criaArvoreDeBusca(inicio, fim, vocabulario) # arvore entre a palavra inicio e fim
    caminho = []
    l = [] # lista com todas as palavras da arvore
    n = [] # lista com os nos
    cn = [] # lista com nos e quantidades - para acompanhar
    # isola as palavras dos nos
    for i in arvore:
        l.append(i[0])
        n.append(i[1])

    for i in n: # conta e isola nos e quantidade [nó, quantidade de elementos]
        if i not in cn:
            cn.append(i)
            cn.append(n.count(i))

    #print(cn) # descomentar para ver os nós e a quantidade, ex: -1, 1 [no -1 possui 1 elemento]
    limite = len(arvore) # limite de nos
    # print(limite) # descomentar para acompanhar código
    caminhocerto = [] # caminho - lista contendo as palavras
    ccerto = 0 # contador - deverá ir de 0 ao limite da lista arvore -2 [inicio e fim]
    minimo = len(arvore) # contador - indicará o caminho minimo a ser percorrido
    tamanho_teste = limite -1 # testará o tamanho da lista

    # funcionará até que o ccerto chegue no limite determinado
    while ccerto < len(arvore) -2:
        ltemp = []  # lista com os caminhos
        ltemp2 = []  # lista com o tamanho de cada caminho
        # para cada lista dentro de arvore
        for i in arvore:
            # testará se o no é igual a ccerto
            # obterá caminhos para cada palavra e verificará o menor caminho
            if i[1] == ccerto and i[1] != arvore[limite -1][1]: # se o indice do nó for igual ao contador ccerto
                ncaminho = criaArvoreDeBusca(i[0], fim, vocabulario) # fará um caminho
                tamanho = len(ncaminho) # calculará o tamanho

                if len(ltemp) == 0 and tamanho != 0 and tamanho <= limite: # primeiro nó
                        ltemp.append(ncaminho[0][0]) # adicionará a palavra na lista
                        ltemp2.append(len(ncaminho))

                elif len(ltemp) > 0 and tamanho != 0 and tamanho < limite:
                    if minimo > tamanho: # se o tamanho foi menor que o minimo já existente
                        ltemp.insert(0, ncaminho[0][0]) # adicionará a palavra na lista
                        ltemp2.insert(0, len(ncaminho))
                        minimo = tamanho # incrementará o LIMITE - ESSA PARTE É IMPORTANTE
                    else:
                        pass

        #print(ltemp) # descomentar para acompanhar código
        # para cada elemento a lista arvore irá confirmar que o caminho a ser adicionado será o menor
        for p in arvore: # loop para remover adicionais
            camiho = criaArvoreDeBusca(p[0], fim, vocabulario) # cria uma arvore de palavras
            limite_teste = len(camiho) # calcula o tamanho
            if p[1] == ccerto and p[0] in ltemp and ccerto > 0: # se o indice for igual ao ccerto e a palavra já estiver na lista ltemp
                if limite_teste < tamanho_teste: # verifica se o tamanho é menor que o limite
                    tamanho_teste = limite_teste # incrementa o contador - importante
                    caminhocerto.append(p[0]) # palavra de caminho mais curto é adicionada
            elif p[1] == ccerto and p[0] in ltemp and ccerto == 0:
                tamanho_teste = limite_teste  # incrementa o contador - importante
                caminhocerto.append(p[0])
        #print(caminhocerto) # descomentar para acompanhar código
        ccerto += 1 # incrementa o contador - importante para parar o loop no momento certo

    #print(caminhocerto)
    caminhocerto.append(fim) # adiciona a palavra fim na posição final na lista
    return caminhocerto # retorna a lista contendo as palavras


# FUNÇÃO PRINCIPAL - interface com as demais funções e o usuário
def main():

    vocabulario = extrairPalavras("vocabulario.txt")  # lista com as palavras do arquivo .txt
    menuOpcoes()  # demonstra as opções ao cliente - apenas uma vez

    # Laço de repetição, parará quando encontrar o break contido na opção 0 encerrar programa]
    while True:
        escolha = int(input("Digite a opção: ")) # coleta a opção do teclado [inteiro]

        # testa se a opção é igual à 1
        if escolha == 1:

            while True:
                # coletará a palavra a ser consultada
                palavra = input("Insira uma palavra: ")  # recebe a palavra inicial

                # valida a existencia na lista
                if testarExistencia(palavra, vocabulario) == 1:
                    print("ERROR, Palavra não existe. Tente novamente!")

                else:
                    # obter uma lista com palavras semelhantes
                    palavras_semelhantes = obtemPalavrasProximas(palavra, vocabulario)
                    print("Palavras proximas de %s: " % palavra, palavras_semelhantes)
                    break # encerra o loop de validação


        # testa se a opção é igual à 2
        elif escolha == 2:

            # laço de repetição - para validação
            while True:
                # coletará a palavra a ser consultada de inicio
                palavra_i = input("Insira a palavra de inicio: ")

                # testará a existencia no vocabulário
                if testarExistencia(palavra_i, vocabulario) == 1:
                    print("ERROR, Palavra não existe. Tente novamente!")

                # caso exista
                else:

                    # laço de repetição para validar a palavra
                    while True:

                        # coletará a palavra a ser consultada de fim
                        palavra_f = input("Insira a palavra de fim: ")

                        if testarExistencia(palavra_f, vocabulario) == 1:  # valida a existencia na lista
                            print("ERROR, Palavra não existe. Tente novamente!")

                        # caso exista, testará se as palavras de inicio e de fim são diferentes
                        else:
                            if palavra_f == palavra_i: # caso seja igual, apresentarpa erro
                                print("ERROR, Palavras devem diferir. Tente novamente!")

                            else:
                                # se forem diferentes testará se possuem o mesmo tamanho [para serem semelhantes]
                                if len(palavra_i) != len(palavra_f):
                                    print("ERROR, Palavras devem ter mesmo tamanho. Tente novamente!")

                                else:
                                    #print("Palavras válidas")
                                    arvore = criaArvoreDeBusca(palavra_i, palavra_f, vocabulario)
                                    print("Quantidade de nós da arvore: %i" % len(arvore))
                                    print("Arvore:", arvore)
                                    break # encerra o loop de validação
                    break # encerra o loop de validação


        # testa se a opção é igual à 3
        elif escolha == 3:

            while True: # loop de valifação
                # coleta a palavra de inicio
                palavra_i = input("Insira a palavra de inicio: ")
                if testarExistencia(palavra_i, vocabulario) == 1:  # valida a existencia na lista
                    print("ERROR, Palavra não existe. Tente novamente!")

                # caso seja válida solicitará a palavra final
                else:
                    while True: # loop de valifação
                        # coleta a palavra final
                        palavra_f = input("Insira a palavra de fim: ")
                        if testarExistencia(palavra_f, vocabulario) == 1:  # valida a existencia na lista
                            print("ERROR, Palavra não existe. Tente novamente!")

                        # caso existam no arquivo
                        # será validado se são de mesmo tamanho e se são diferentes
                        else:
                            if palavra_f == palavra_i: # caso de palavras iguais - erro
                                print("ERROR, Palavras devem diferir. Tente novamente!")

                            else:
                                if len(palavra_i) != len(palavra_f): # caso sejam e tamanhos diferentes
                                    print("ERROR, Palavras devem ter mesmo tamanho. Tente novamente!")

                                else:
                                    #print("Palavras válidas") # palavrs válidas - existem, são diferentes e de mesmo tamanho
                                    # recebe a lista das palavras e imprime na tela
                                    caminho = obtemCaminho(palavra_i, palavra_f, vocabulario)
                                    print("A distancia entre %s e %s é %i" % (palavra_i, palavra_f, len(caminho)))
                                    caminho_p = palavra_i
                                    for palavra in caminho:
                                        caminho_p += " -> %s" % palavra # imprime na tela
                                    print(caminho_p)
                                    break # encerra o loop de validação
                break # encerra o loop de validação


        # testa se a opção é igual à 0
        elif escolha == 0:
            print("Programa encerrado com sucesso")
            print("_".center(30, "_"))
            break


        # testa se a opção é inválida
        else:
            print("ERROR, OPÇÃO INVÁLIDA. Tente novamente")


# evoca a função main()
if __name__ == '__main__':
    main()