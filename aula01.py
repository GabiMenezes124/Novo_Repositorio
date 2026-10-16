import os # O import 'os' é um sistema de biblioteca acionado dentro da própria linguagem de programação;

# restaurantes = ['Pizza', 'Sushi'] # aqui definimos uma nova váriavel com o intuito de se tornar uma lista pois ela pode armazenar informações do usuario;
restaurantes = [{'nome':'Espetinho do lui', 'categoria':'Espetinho','ativo':True}, # aqui definimos um dicionario com valores variados dentro de uma lista (o dicionario permite aplicar registro de um valor ou mais dentro de uma lista de forma organizada.)
                {'nome':'Pizza Hot', 'categoria':'Pizza', 'ativo':False}, # um dicionario pode possuir variados tipos de dados sendo eles: string, inteiro, décimal e booleano.
                {'nome':'Doces do amor', 'categoria':'Doces', 'ativo':True}
]

#Primeiro passo para criar um sistema é decompor o projeto em pequenas partes e abstraí-lo de forma que fique légivel para o cliente (usuario do aplicativo);
def exibir_nome_do_programa():
    ''' Essa função é responsavel por exibir a informação do titulo do programa.'''
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    ''') # a função "print" exibe informações do console (onde digitamos o código) atráves do output (dado de saída) no caso o terminal;
# o carácter espécial "\n" significa a quebra de linha ou pular linha;

def exibir_opcao():
    ''' Essa função é responsavel por exibir ao cliente no terminal cada print sendo referente a opção que o usuario vai escolher.'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_app(): # o 'def' é igual a 'function' nesta linguagem de programação é uma boa prática de programação pois ele vai isolar ações atráves de determinada função; (isso impede que o programa fique poluído).
    ''' Essa função é responsavel por finalizar o sistema.'''
    os.system('cls') # esse comando da biblioteca 'os' permite que limpe todo o terminal atráves da ação aplicada.
    print('Encerrando o programa.\n')

def opcao_invalida():
    ''' Essa função é responsavel por exibir a mensagem de que a opção é inválida.'''
    print('opção inválida!\n')
    input('digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar um novo restaurante.
    
    Inputs 
    - Cadastra um novo Restaurante.
    - Define a categoria do restaurante.
    

    Outputs 
    - Adiciona um novo restaurante a lista dicionario restaurantes.
    
    '''
    os.system('cls')
    print('Cadastrando novo restaurante...\n')
    nome_do_restaurante = input('Escolha o nome do restaurante que deseja cadastrar: ') # aqui pedimos ao usuario o nome do restaurante que ele gostaria de adicionar ao sistema.
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ') # aqui pedimos ao usuario a categoria do nome do restaurante que ele gostaria de adicionar ao sistema.
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} # armazenamos os valores do dicionario nessa variavel de dados para quando o usuario cadastrar o novo restaurante e categoria ela sera armazenada automaticamente pela função "append".
    restaurantes.append(dados_do_restaurante) # atráves da função "append" estamos puxando/armazenando oque estiver dentro do colchetes para a váriavel citada antes do ponto.
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\ndigite uma tecla para voltar ao menu principal: ')
    main()

def listar_restaurantes(): #criamos uma nova função para armazenar ações (isso simplifica a legibilidade do código e deixa mais escasso o número de linhas digitados);
    ''' Essa função é responsavel por listar cada restaurante cadastrado no sistema.'''
    os.system('cls') #comando para limpar o sistema antes de executar qualquer bloco de código abaixo;
    print('Listando Restaurantes do sistema: \n') #vai informar ao usuario exatamente oque esta escrito entre aspas duplas;

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes: #o laço for tem como finalidade a repetição de um comando de código até que exiba o numero determinado de ações;
        nome_restaurante = restaurante['nome'] # aqui criamos uma variavel referente ao nome de cada dicionario criado dentro da lista "restaurantes" e especificamos para informar o item com o valor "nome".
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado' # adicionamos um operador térnario ao código pois possui dois valores (exibe a primeira mensadem se for verdadeiro e a segunda se for)
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # aqui pedimos para passar informação ao usuario com cada variavel especificando os valores do dicionario.

    input('\ndigite uma tecla para voltar ao menu principal: ')
    main()

def alternar_estado_restaurante():
    ''' Essa função é responsavel por alternar o estado de ativação/desativação do restaurante.'''
    os.system('cls')
    print('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False # aqui criamos uma variavel com um valor falso para alterar a chave "status" de um restaurante para verdadeiro. 

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']: # acrescentamos uma estrutura condicional ao laço for pois estamos especificando ao usuario credenciais que serão mantidas ou alteradas.
            restaurante_encontrado = True #alteramos a variavel para "True" caso o nome do restaurante digitado pelo usuario seja correspondente a chave "nome" do dicionario.
            restaurante['ativo'] = not restaurante['ativo'] # aqui ele ira alterar o valor da chave status para True ou False caso o usuario queira alterar.
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' #utilizamos um operador térnario para passar informações verdadeiras e falsas ao usuario.
            print(mensagem)
    if not restaurante_encontrado: #se o nome digitado pelo usuario nao for correspondente ao do dicionario ele ira continuar no loop ate digitar um nome correto.
        print('O restaurante não foi encontrado.')

    input('\ndigite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    ''' Essa função é responsavel por escolher determinada opção exibidas na tela inicial do programa.'''
    try: # o try tem como funcionalidade a tentativa de rodar um bloco de código caso ele seja uma exeção;
        # váriavel com nomenclatura: snake_case (underscore case);
        opcao_escolhida = int(input('Escolha uma opcao: ')) # assim como o print que é uma função o input também é. O input é o inverso do print já que ele é capaz de absorver uma informação digitada pelo usuario atráves do terminal;
        # para armazenar determinada função ou método utilizamos as váriaveis;

        # print(f'Voce escolheu a opcao: {opcao_escolhida}') # para exibir uma variavel armazenada no console utilizamos métodos como o .format ou apenas exibimos o nome da váriavel no console;

        #Estrutura Condicional para informar ao cliente as opções escolhidas atráves de mensagens:

        if opcao_escolhida == 1: #'if' = 'se' uma variavel '==' = 'for equivalente a um' tipo de dado(variavel/modelo/estrutura...) ele passará por essa condição caso seja verdadeiro;
            cadastrar_novo_restaurante() #Caso for Falso ele não ira responder a esta condição e sim a de baixo e vice-versa;
        elif opcao_escolhida == 2: # O elif é referente a uma continuidade opcional da estrutura de bloco de código de cima;
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:  # o Else é a última estrutura do bloco de código de uma condicional pois ele atenderá ao pedido do usuario caso as outras condições sejam falsas;
            opcao_invalida()
    except: #caso o try não rode irá gerar o "except" que tem como finalidade a tentativa de rodar outro comando de código;
        opcao_invalida()

def main(): #aqui definimos a função do arquivo principal do programa e acrescentamos outras funções dentro para tornar o programa mais abstrato;
    ''' Essa função é responsavel pelo arquivo principal do programa(pithon) e tem como objetivo priorizar a exibição e escolhas feitas na tela inicial do programa.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__': # aqui definimos o arquivo gerado(aula01.p) como o principal atráves do "__main__" todo arquivo criado em pithon vem de fábrica como secundário pois permite a extração de scripts entre outros arquivos;
    main() # definindo as ações principais dentro do arquivo atráves da função gerada;
