# Eduardo Fedeli Souza RM:550132
# Gabriel Torres Luiz RM: 98600

import json
import datetime

#login = admin
#senha = 12345

# Funções para ler e escrever dados do banco de dados
def ler_dados_json(file_name):
    try:
        with open(file_name, "r") as file:
            dados = json.load(file)
            return dados
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def escrever_dados_json(dados, file_name):
    with open(file_name, "w") as file:
        json.dump(dados, file, indent=4)

# Adicione um usuário padrão ao arquivo "users.json"
usuarios_iniciais = {"admin": {"senha": "12345"}}
escrever_dados_json(usuarios_iniciais, "users.json")

def realizar_login():
    # Crie um banco de dados para armazenar as informações dos usuários
    usuarios = ler_dados_json("users.json")

    while True:
        # Solicite as informações de login
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        # Verifique se o usuário existe e se a senha está correta
        if nome_usuario in usuarios:
            if usuarios[nome_usuario]["senha"] == senha:
                print("Login bem-sucedido!")
                return nome_usuario
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")

# Sobre Nós
def sobre_nos():
    print("\nBem-vindo à HealthSync, onde tornamos o agendamento e acompanhamento da sua vacinação") 
    print("e das vacinas de crianças mais fácil e eficiente. Nosso compromisso é oferecer um")
    print("serviço de agendamento acessível e centrado na família, combinado com um inovador")
    print("Caderno Digital de Vacinas para manter tudo organizado. Acreditamos na prevenção ")
    print("e bem-estar infantil, e nossa equipe dedicada está aqui para tornar a experiência ")
    print("de vacinação positiva e tranquila para todos os pais. Confie em nós para cuidar do")
    print("que mais importa - a saúde e felicidade das suas crianças.\n")


# Agendamento de vacinação
def agendar_vacinacao():
    # Solicite as informações da vacinação
    nome = input("Digite seu nome: ")
    vacina = input("Digite o nome da vacina: ")
    data_da_vacinacao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Verifique se a vacina já foi feita
    vacinas_feitas = ler_dados_json("vacinas.json")
    if nome in vacinas_feitas:
        if vacina in vacinas_feitas[nome]:
            print("Você já tomou essa vacina.")
        else:
            # Acrescente a vacina à ficha médica
            vacinas_feitas[nome][vacina] = data_da_vacinacao
            escrever_dados_json(vacinas_feitas, "vacinas.json")
            print("Vacinação agendada com sucesso!")
    else:
        # Crie uma nova ficha médica
        vacinas_feitas[nome] = {vacina: data_da_vacinacao}
        escrever_dados_json(vacinas_feitas, "vacinas.json")
        print("Vacinação agendada com sucesso!")

# Editar caderno de vacinas
def editar_caderno_vacinas():
    vacinas = ler_dados_json("vacinas.json")
    
    nome = input("Digite o nome da pessoa a ser vacinada para editar: ")

    if nome in vacinas:
        # Mostrar vacinas existentes
        print(f"Vacinas para {nome}: {', '.join(vacinas[nome].keys())}")

        # Adicionar nova vacina, remover existente ou voltar
        opcao = input("Deseja adicionar uma nova vacina (A), remover uma existente (R) ou voltar (V)? ").upper()
        if opcao == "A":
            nova_vacina = input("Digite o nome da nova vacina: ")
            data_da_vacinacao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            vacinas[nome][nova_vacina] = data_da_vacinacao
            print("Nova vacina adicionada com sucesso!")
        elif opcao == "R":
            vacina_remover = input("Digite o nome da vacina a ser removida: ")
            if vacina_remover in vacinas[nome]:
                del vacinas[nome][vacina_remover]
                print("Vacina removida com sucesso!")
                
                # Verificar se não há mais vacinas associadas ao nome
                if not vacinas[nome]:
                    del vacinas[nome]
                    print(f"Nome {nome} removido do caderno de vacinas.")
            else:
                print("Vacina não encontrada.")
        elif opcao == "V":
            return
        else:
            print("Opção inválida.")
    else:
        print("Nome não encontrado no caderno de vacinas.")

    escrever_dados_json(vacinas, "vacinas.json")

# Ler JSON de vacinas
def ler_json_vacinas():
    while True:
        vacinas = ler_dados_json("vacinas.json")
        print("Conteúdo do caderno de vacinas:")
        print(json.dumps(vacinas, indent=4))

        opcao = input("Escolha uma opção: (E) Editar vacinas ou (V) Voltar ao menu principal ").upper()
        if opcao == "E":
            editar_caderno_vacinas()
        elif opcao == "V":
            break
        else:
            print("Opção inválida!")

# Execução do código
usuario_atual = realizar_login()
menu_principal_exibido = False

while True:
    if not menu_principal_exibido:
        print("Bem-vindo ao Sistema Médico")
        print("1. Sobre nós")
        print("2. Agendar vacinação")
        print("3. Acessar caderno de vacinas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sobre_nos()
        elif opcao == "2":
            agendar_vacinacao()
        elif opcao == "3":
            ler_json_vacinas()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida!")

        menu_principal_exibido = True
    else:
        opcao = input("Escolha uma opção: (V) Voltar ao menu principal ").upper()

        if opcao == "V":
            menu_principal_exibido = False
        else:
            print("Opção inválida!")
