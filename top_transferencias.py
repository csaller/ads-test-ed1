import csv

transferencias = []

with open("top250-00-19.csv", encoding="utf-8") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        transferencias.append(linha)


def top_10_transacoes():
    clubes = list([x['Team_to'] for x in transferencias])
    compras = [0] * len(clubes)
 
    for transferencia in transferencias:
        indice = clubes.index(transferencia['Team_to'])
        compras[indice] += 1

    juntos = sorted(zip(compras, clubes), reverse=True)
    transferencias2, clubes2 = zip(*juntos)

    print("Nº Nome do Clube............. Compras")
    print("-------------------------------------")

    for num, (transferencia, clube) in enumerate(zip(transferencias2, clubes2), start=1):
        print(f"{num:2d} {clube:25s} {transferencia:5d}")
        if num == 10:
            break


def compara_clubes():
    clube1 = input("1ª clube: ")
    clube2 = input("2ª clube: ")
    jogadores_clube_1 = []
    jogadores_clube_2 = []

    for transferencia in transferencias:
        if clube1 in transferencia["Team_to"]:
            jogadores_clube_1.append(transferencia["Name"])
        elif clube2 in transferencia["Team_to"]:
            jogadores_clube_2.append(transferencia["Name"])

    print(f"Jogadores comprados pelo {clube1}: {jogadores_clube_1}\n")
    print(f"Jogadores comprados pelo {clube2}: {jogadores_clube_2}\n")
    
    print(f"Total de jogadores comprados por cada clube:\n{clube1}: {len(jogadores_clube_1)}\n{clube2}: {len(jogadores_clube_2)}")


def top_10_transferencias():
    lista = sorted(transferencias, key=lambda row: row["Transfer_fee"], reverse=True)
    print("Top 10 transferencias:")
    for i in range(10):
        print(f"{i+1}º Lugar: {lista[i]["Transfer_fee"]}")
        i = i + 1


def procura_jogador():
    jogador = input("Insira o nome do jogador para pesquisar: ")
    jogadores_lista = []

    for transferencia in transferencias:
        if jogador in transferencia["Name"]:
            jogadores_lista.append(transferencia["Name"])
    
    if len(jogadores_lista) == 0:
        print("Nenhum jogador encontrado com esse nome!")
    else:    
        print("Jogadores encontrados com esse nome:")
        for x in set(jogadores_lista):
            print(f"{x}")


def lista_logadores_clube():
    clube = input("Insira o clube para pesquisar: ")
    jogadores_lista = []

    for transferencia in transferencias:
        if clube in transferencia["Team_to"]:
            jogadores_lista.append(transferencia)

    print("Lista de jogadores e idades:")
    idades = 0
    for jogador in jogadores_lista:
        print(f"{jogador["Name"]}: {jogador["Age"]} anos")
        idades += int(jogador["Age"])
    print(f"Média de idades: {round(idades / len(jogadores_lista), 1)} anos")


def agrupar_idade():
    transf_idades = list([x['Age'] for x in transferencias])
    idades = [0] * len(transf_idades)
 
    for transferencia in transferencias:
        indice = transf_idades.index(transferencia['Age'])
        idades[indice] += 1

    juntos = sorted(zip(idades, transf_idades), reverse=True)
    transferencias2, transf_idades2 = zip(*juntos)

    print("Nº   Idade...... Negociações")
    print("--------------------------")

    for num, (transferencia, transf_idade) in enumerate(zip(transferencias2, transf_idades2), start=1):
        print(f"{num:2d} {transf_idade:>4} anos {transferencia:>10}")
        if num == 10:
            break
