import json

with open('cardapio.json', 'r') as arquivo:
    cardapio = json.loads(arquivo.read())

with open('comandas.json', 'r') as arquivo:
    comandas = json.loads(arquivo.read())

menu_escolha_comandas = '''
    Escolha da Comanda
    0 - Sair
    1 - Escolher Comanda
    2 - Deletar Comanda
    3 - Adicionar Comanda
    4 - Editar cardapio

'''

menu_cardapio = '''
    Edição do Cardapio
    0 - Voltar
    1 - Adicionar prato
    2 - Remover prato
    3 - Alterar preco
    4 - Imprimir Cardapio

'''


escolha_comanda = None

while escolha_comanda != 0:

    if escolha_comanda != 4:
        print(menu_escolha_comandas)
        try:
            escolha_comanda = int(input())
        except:''

    if escolha_comanda not in range(5):
        print('Digite um comando valido')
        print(menu_escolha_comandas)
        try:
            escolha_comanda = int(input())
        except:''

    if escolha_comanda == 1:
        comanda_escolhida = input('Qual comanda deseja editar? ')
        if comanda_escolhida not in comandas:
            print('Comanda inexistente.')
        else:
            comanda = comandas[comanda_escolhida]
            break


    if escolha_comanda == 2:
        del_comanda = input('Qual comanda deseja deletar? ')
        if del_comanda not in comandas:
            print('Comanda inexistente. ')
        else:
            del comandas[del_comanda]


    if escolha_comanda == 3:
        add_comanda = input('Comanda a ser adicionada: ')
        if add_comanda in comandas:
            print('Comanda existente. ')
        else:
            comandas[add_comanda] = {}

    if escolha_comanda == 4:
        escolha_cardapio = None
        print(menu_cardapio)
        try:
            escolha_cardapio = int(input())
        except:''


        if escolha_comanda not in range(5):
            print('Digite um comando valido')
            print(menu_escolha_comandas)
            try:
                escolha_cardapio = int(input())
            except:''

        if escolha_cardapio == 0:
            escolha_comanda = None

        if escolha_cardapio == 1:
            prato = input('Prato a ser adicionado: ')
            if prato in cardapio:
                print('Prato existente')
            else:
                preco = float(input('Preço do prato: '))
                while preco <= 0:
                    preco = float(input('Preço não pode ser negativo ou nulo. Preço do prato: '))
                cardapio[prato] = round(preco,2)


        if escolha_cardapio == 2:
            del_prato = input('Qual prato deseja deletar? ')
            if del_prato not in cardapio:
                print('Prato inexistente. ')
            else:
                del cardapio[del_prato]

        if escolha_cardapio == 3:
            prato = input('Prato a ter o preço mudado: ')
            if prato not in cardapio:
                print('Prato inexistente')
            else:
                preco = float(input('Novo preço do prato: '))
                while preco <= 0:
                    preco = float(input('Novo preço não pode ser negativo ou nulo. Novo preço do prato: '))
                cardapio[prato] = round(preco,2)

        if escolha_cardapio == 4:
            for item in cardapio:
                print(item + '( R$' + str(cardapio[item])  + ')')


escolha_menu = None

menu = '''
    Comanda Eletronica
    0 - Sair
    1 - Imprimir Cardapio
    2 - Adicionar Item
    3 - Remover Item
    4 - Imprimir Comanda
    5 - Trocar Comanda
'''

while escolha_menu != 0 and escolha_comanda != 0:
    print(menu)
    try:
        escolha_menu = int(input())
    except:''

    if escolha_menu not in range(6):
        print('Digite um comando valido')
        print(menu)
        try:
            escolha_menu = int(input())
        except:''


    if escolha_menu == 1:
        for item in cardapio:
            print(item + '( R$' + str(cardapio[item])  + ')')


    if escolha_menu == 2:
        item = input('Item a ser adicionado: ')
        if item not in cardapio:
            print('Item inexistente ')
        else:
            quantidade = int(input('Quantidade a ser adicionada: '))
            while quantidade <= 0:
                quantidade = int(input('Quantidade não pode ser negativa ou nula. Quantidade a ser adicionada: '))
            preco = cardapio[item]
            if item not in comanda:
                comanda[item] = {'quantidade': quantidade, 'preco total': (preco*quantidade)}
            else:
                nova_quantidade = comanda[item]['quantidade'] + quantidade
            print(item + 'adicionado a comanda.')

    if escolha_menu == 3:
        item = input('Item a ser removido: ')
        if item not in comanda:
            print('Item não existente na comanda')
        else:
            quantidade = int(input('Quantidade a ser removida: '))
            while quantidade <= 0:
                quantidade = int(input('Quantidade não pode ser negativa ou nula. Quantidade a ser removida: '))
            preco = cardapio[item]
            nova_quantidade = comanda[item]['quantidade'] - quantidade
            while nova_quantidade < 0:
                quantidade = int(input('Nova quantidade não pode ser negativa. Quantidade a ser removida: '))
                nova_quantidade = comanda[item]['quantidade'] - quantidade
            if nova_quantidade > 0:
                comanda[item] = {'quantidade': nova_quantidade, 'preco total': (preco*nova_quantidade)}
            else:
                del comanda[item]


    if escolha_menu == 4:
        total = 0
        for item in comanda:
            print(item)
            print('    preço unitario R$ ' + str(comanda[item]['preco total']))
            print('    preço total R$ ' + str(cardapio[item]))
            total += comanda[item]['preco total']
        print('Valor total a ser pago R$' + str(total))
        print('Valor total a ser pago (c/ 10%) R$' + str(round(total*1.1, 2)))

print('Até mais')

with open('cardapio.json', 'w') as arquivo:
    json.dump(cardapio, arquivo, sort_keys=True, indent=4)

with open('comandas.json', 'w') as arquivo:
    json.dump(comandas, arquivo, sort_keys=True, indent=4)
