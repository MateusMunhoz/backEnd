#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

precoMaiorQue30 = []
for lojas in response:
    for produtos in lojas["produtos"]:
        if(produtos["preço"] >= 30):
            precoMaiorQue30.append(produtos)
for produto in precoMaiorQue30:
    print(f"Os produtos que possuem valor maior que 30 sao {produto['nome']}")

#Embora o desempenho não seja uma preocupação crítica nesse caso específico, a abordagem de filtrar e armazenar uma lista de resultados é geralmente mais eficiente do que realizar várias verificações em um loop, especialmente em conjuntos de dados maiores.
#O código é fácil de manter e modificar. Se você precisar alterar a condição de filtragem ou adicionar novos campos, as mudanças podem ser feitas de maneira simples e direta.
#A abordagem que você usou é facilmente escalável. Se no futuro você precisar adicionar mais critérios de filtragem ou realizar operações mais complexas, a estrutura do código já está preparada para isso, podendo ser ajustada sem grandes mudanças.

#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

import json
responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

for produtos in responsejson["produtos"]:
    if(produtos["nome"] == "Produto B"):
        print(f"O produto B tem o id: {produtos["id"]}, nome: {produtos["nome"]} preço: {produtos["preço"]}")

#eu utilizei esse metodo para que caso o produto B por algum motivo nao seja o segundo produto na lista ele ainda possa ser encontrado, fazendo com que o codigo nao tenha que ser mudado toda que vez que seja necessario achar o produto B em outra posicao, iterando por todos os produtos que estao dentro do json


#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra



lista = [5,8,3,0,8,1,9,10,20,30]
lista.sort()

print(lista)

#eu havia pensado em fazer um algoritmo de bubble sorting, porem o metodo sort de python possui uma complexidade menor em termos de tempo de execucao, sendo mais optimizado


#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]
listaStrip = []
x = 0

for x in range(len(lista)):
    listaStrip.append(lista[x].strip())

print(listaStrip)



#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]
lista.remove(lista[1])
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
x = 0
for x in range(6):
    if(lista[x] == "joao"):
        lista[x] = "maria"
print(lista)
    

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

lista = [1,2,3,4,5,6,7]
x = 0;
while x <= 5: 
    print(lista[x])
    x = x + 1
    
#A solução apresentada é simples e eficiente. O uso de um loop while com um incremento manual de x permite controle direto sobre o índice, o que era necessário para garantir que o loop parasse após o sexto item. Escolhi essa solução em vez de outras mais complexas porque ela é adequada ao problema e mantém o código fácil de entender e manter.



#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra
import requests

def contarTasks():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    
  
    if response.status_code == 200:
        tasks = response.json()
        
        
        tasksCompletas = 0
        tasksIncompletas = 0
        
        
        for task in tasks:
            if task['completed']:
                tasksCompletas += 1
            else:
                tasksIncompletas += 1
        
        return tasksCompletas, tasksIncompletas
    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        return None
    
#eu escolhi essa resolucao pois essa estrutura pode ser facilmente adaptada para lidar com mais tipos de dados ou para processar respostas maiores, mantendo a contagem de tasks simples.


completadas, pendentes = contarTasks()
print(f"Tasks completadas: {completadas}")
print(f"Tasks pendentes: {pendentes}")


#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra
import json
import requests

url = 'https://jsonplaceholder.typicode.com/users'
retorno = requests.get(url)

if(retorno.status_code != 200):
    print(f"Erro na requsicao. Codigo de status: {retorno.status_code} ")
else:
    user = retorno.json()
    for user in user:
        nome = user['name']
        username = user['username']
        email = user['email']
        rua = user['address']['street']
        print(f"Nome: {nome}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Rua: {rua}")
        

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

listaTeste = []
listaTeste.append(1)
listaTeste.append(2)
listaTeste.append(3)
listaTeste.append(4)
print("A lista apos a adicao de novos elementos: ",listaTeste)
listaTeste.pop(0)
print("A lista apos remocao: ",listaTeste)


#11-crie uma lista e adicione um item novo a ela utilizando a metodologia LIFO

pilha = []

pilha.append("primeiro")
pilha.append("segundo")
pilha.append("terceiro")

print("Pilha após adicionar elementos novos:", pilha)

ultimo_item = pilha.pop()

print("Pilha após remoção:", pilha)


#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class contaBancaria:
    id_adicionar = 1
    def __init__(self, nome, cpf):
        self.id = contaBancaria.id_adicionar
        contaBancaria.id_adicionar += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0

    def mostrarSaldo(self):
        print(f"Saldo atual: R${self.saldo:.3f}")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O depósito de R${valor:.3f} foi realizado com sucesso!")
        else:
            print("O valor do depósito deve ser maior que R$0.00.")

    def saque(self, valor_saque):
        if valor_saque > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor_saque
            print(f"Saque de R${valor_saque:.3f} foi realizado.")

class interfaceBanco:
    def __init__(self):
        self.contas = []

    def novaConta(self):
        nome = input("Digite o nome do titular da conta: ")
        cpf = input("Digite o CPF do titular da conta: ")
        nova_conta = contaBancaria(nome, cpf)
        self.contas.append(nova_conta)
        print(f"Conta criada com sucesso! Seu ID único é: {nova_conta.id}")

    def logarConta(self, idConta):
        for conta in self.contas:
            if conta.id == idConta:
                return conta
        print("Nenhuma conta foi encontrada com o ID fornecido.")
        return None


def main():
    banco = interfaceBanco()

    while True:
        print("\n--- Bem-vindo ao Banco ---")
        print("1. Criar nova conta")
        print("2. Logar em uma conta existente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            banco.novaConta()

        elif opcao == "2":
            try:
                id_conta = int(input("Digite o ID da conta: "))
                conta = banco.logarConta(id_conta)
                if conta:
                    while True:
                        print(f"\n--- Bem-vindo(a), {conta.nome} ---")
                        print("1. Ver saldo")
                        print("2. Realizar depósito")
                        print("3. Realizar saque")
                        print("4. Sair da conta")
                        escolha = input("Escolha uma opção: ")

                        if escolha == "1":
                            conta.mostrarSaldo()
                        elif escolha == "2":
                            valor = float(input("Digite o valor para depósito: "))
                            conta.deposito(valor)
                        elif escolha == "3":
                            valorSaque = float(input("Digite o valor para saque: "))
                            conta.saque(valorSaque)
                        elif escolha == "4":
                            print("Saindo da conta...")
                            break
                        else:
                            print("Opção inválida.")
            except ValueError:
                print("ID inválido. Por favor, digite um número válido.")

        elif opcao == "3":
            print("Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

main()
