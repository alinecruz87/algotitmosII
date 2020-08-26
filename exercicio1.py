'''
Construir um algoritmo que contenha 3 listas:

      • Nomes de produtos

      • Preços de cada produto

      • Quantidades de cada produto

• Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas



Criar um repositório GIT remoto (Github, Gitlab ou Bitbucket), fazer commit do trabalho para este repositório e postar aqui apenas o link do repositório.
'''

nome_produto = ['a', 'b', 'c', 'd', 'e']
preco_produto = [1,2,3,4,5]
qt_produto = [5,4,3,2,1]
menu = '''
    [1] - Escolher produto
    [2] - Deletar produto
    '''

def lista_produtos():
    for i in range (len(nome_produto)):
        print(f'{i} - Produto: {nome_produto[i]}')


def escolhe_produto(): 
    i = int(input('Informe o índice do produto que deseja listar: '))
    input(f'Produto: {nome_produto[i]} - Preço: {preco_produto[i]} - Quantidade: {qt_produto[i]}')

def deleta_produto():
    d = int(input('Informe o índice do produto que deseja deletar: '))
    del nome_produto[d]
    del preco_produto[d]
    del qt_produto[d]
    return nome_produto

while True:
    print(menu)
    escolha =  int(input('Escolha: '))
    if escolha == 1:
        lista_produtos()
        escolhe_produto()
    elif escolha == 2:
        lista_produtos()
        deleta_produto()
        lista_produtos()
    else: 
        input('Opção inválida')

    