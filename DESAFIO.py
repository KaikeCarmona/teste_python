#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , 
# aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. 
# a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class Conta:

    # Variável para controlar o próximo id disponível
    id_contador = 1  

    # Lista para armazenar todas as instâncias de contas criadas
    instancias = []

    def __init__(self, nome, cpf):
        # Atribui o próximo ID disponível à instância
        self.id = Conta.id_contador  
        # Incrementa o ID para a próxima instância
        Conta.id_contador += 1  
        # Atribui os parâmetros fornecidos aos atributos da instância
        self.nome = nome
        self.cpf = cpf
        # Inicializa o saldo como 0
        self.saldo = 0  
        # Adiciona a instância recém-criada à lista de instâncias
        Conta.instancias.append(self)

    # Método para mostrar os detalhes da conta
    def mostrar_conta(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Saldo: {self.saldo}")

    # Método para realizar depósito na conta
    def deposito(self, valor):
        self.saldo += valor

    # Método para realizar saque da conta
    def saque(self, valor):
        # Verifica se há saldo suficiente para o saque
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo menor que o saque solicitado!")

# Variável para controlar o loop do menu
var = True

# Loop principal do menu
while var:
    print("\n------------------------ MENU ------------------------")
    print("1 - Criar Conta\n2 - Acessar Conta\n3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    # Estrutura de controle para as opções do menu
    match opcao:
        case 1:
            print("\n------------ Criar Conta ------------")
            # Solicita o nome e CPF do usuário
            nome = input("Digite o nome: ")
            cpf = input("Digite o CPF: ")
            # Cria uma nova conta com os dados fornecidos
            nova_conta = Conta(nome, cpf)
            print(f"\nUma conta no nome de {nova_conta.nome.upper()} acabou de ser criada!")
            # Mostra os detalhes da conta recém-criada
            nova_conta.mostrar_conta()
            print("\n")
             
        case 2:
            print("\n------------ Acessar Conta ------------")

            # Solicita o CPF do usuário para buscar a conta
            ContaCPF = input("Digite o seu CPF: ")  
            
            conta_encontrada = None
            # Procura a conta na lista de instâncias pelo CPF
            for conta in Conta.instancias:
                if conta.cpf == ContaCPF:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                # Mostra os detalhes da conta encontrada
                conta_encontrada.mostrar_conta()

                print("\n------------ OPERAÇÕES ------------\n1 - Deposito\n2 - Saque")
                operacao = int(input("Digite a opção desejada: "))

                match operacao:
                    case 1:
                        # Solicita o valor do depósito e realiza a operação
                        valor = float(input("Digite o valor do deposito: "))
                        conta_encontrada.deposito(valor)
                        print(f"O saldo atual é de {conta_encontrada.saldo}")
                    case 2:
                        # Solicita o valor do saque e realiza a operação
                        valor = float(input("Digite o valor do saque: "))
                        conta_encontrada.saque(valor)
                        print(f"O saldo atual é de {conta_encontrada.saldo}")

        case 3:
            # Sai do loop e encerra o programa
            var = False
            break

