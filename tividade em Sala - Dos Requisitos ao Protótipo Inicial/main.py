# Passo 1
# Requisitos escolhidos:
#   1) Requisito 1: Cadastro com validação de entrada
#   2) Requisito 2: Autenticação                          
# README e ajustes finais                        
# Uso de IA: pedi ajuda para revisar o código.

from r1_cadastro import cadastrar_usuario
from rf02_login import autenticar


usuarios = {}

#Requisito 1:
print("=== Requisito 1 - Cadastro ===")
testes_cadastro = [
    ("allan", "abc123"),   #criando 1 usuario

    ("allan", "xyz789"),   #com nome repetido
    ("", "abc123"),        #nome vazio
    ("maria", "abc"),      #senha muito curta
    ("joao", "abcdefg"),   #senha sem numero
]
for nome, senha in testes_cadastro:
    ok, mensagem = cadastrar_usuario(usuarios, nome, senha)
    print("cadastro de '" + nome + "':", "OK" if ok else "FALHOU", "-", mensagem)

#Requisito 2:
print("\n=== RF02 - Login ===")
testes_login = [
    ("allan", "abc123"),   #Login e senha certa
    ("allan", "errada1"),  #Senha errada
    ("fulano", "abc123"),  #Usuario errado
]

for nome, senha in testes_login:
    ok, mensagem = autenticar(usuarios, nome, senha)
    if ok:
        resultado = "sucesso"
    else:
        resultado = "deu ruim"
    print("login de '" + nome + "': " + resultado + " - " + mensagem)


