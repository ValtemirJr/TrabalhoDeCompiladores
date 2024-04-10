def reconhecerStrings():
    with open("programa.txt", "r") as programa:  # Abre o arquivo onde contém os tokens a serem reconhecidos
        linhas = programa.readlines()  # Lê todas as linhas do arquivo
        tokens_por_linha = []
        for num_linha, linha in enumerate(linhas, start=1):  # Enumera as linhas começando de 1
            tokens = linha.strip().split()  # Remove espaços em branco e quebra a linha em tokens
            tokens_por_linha.append((num_linha, tokens))  # Adiciona a lista de tokens com o número da linha
    return tokens_por_linha

def verificarToken(afd, token, tabela_de_simbolos, num_linha):
    estado = 0  # Inicializa a posição como 0 (que corresponde à estado inicial)

    for simbolo in token: # Percorre o token
        if simbolo not in afd[estado]: # Verifica se o simbolo não está presente no estado atual
            tabela_de_simbolos.append((num_linha, token, "x")) # Adiciona na tabela de simbolos um erro
            return
        estado = afd[estado][simbolo][0]  # Atualiza o estado para o proximo estado a ser verificado 

    if '*' in afd[estado]: # Após verificar todos os simbolos, verifica se o estado atual é um estado final
        tabela_de_simbolos.append((num_linha, token, estado))  # Se o estado atual for final reconheceu o token e adiciona na tabela de simbolos
        return 

    if 'Îµ' in afd[estado]:  # Após verificar todos os simbolos e o estado atual não for final tenta fazer uma epsilon transição
        estado = afd[estado]["Îµ"][0] # Realiza a epsilon transição
        if '*' in afd[estado]: # Após a epsilon transição verifica se o estado atual é final
            tabela_de_simbolos.append((num_linha, token, estado)) # Se o estado atual for final reconheceu o token e adiciona na tabela de simbolos
            return

    tabela_de_simbolos.append((num_linha, token, "x")) # Caso o estado não seja final e não possua epsilon transição o token não foi reconhecido e adiciona um erro a tabela de simbolos


def fazerAnaliseLexica(afd):
    tokens_por_linha = reconhecerStrings() # Ler o arquivo a ser analisado
    tabela_de_simbolos = []
    for num_linha, tokens in tokens_por_linha: # Percorre os token do arquivo e a linha em que ele está
        for token in tokens: # Para cada token da linha ele verifica se é valido e preenche a tabela de simbolos
            verificarToken(afd, token, tabela_de_simbolos, num_linha) 

    fita = gerarFita(tabela_de_simbolos) # Apartir da tabela de simbolos é gerada a fita de saida
    imprimirTabelaDeSimbolosEFita(tabela_de_simbolos, fita)

def imprimirTabelaDeSimbolos(tabelaDeSimbolos):
    print("Tabela de saída:")
    for item in tabelaDeSimbolos:
        print(item)

def gerarFita(tabelaDeSimbolos):
    fita = [item[2] for item in tabelaDeSimbolos]
    return fita

def imprimirFita(fita):
    print("Fita:")
    print(fita)

def imprimirTabelaDeSimbolosEFita(tabela, fita):
    print("Tabela de saída:")
    for item in tabela:
        print(item)

    print(f"\nFita: {fita}")