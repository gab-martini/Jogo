'''
Jogo do Adivinhe o Número
2024.07.30
Gabriele Martini
'''
# Objetivo: Desenvolver um Jogo, onde o usuário deverá tentar adivinhar um número secreto sorteado pelo PC

# Módulos e Bibliotecas
from random import randint

# Variáveis
msg = ''
numeroSecreto = 0 # Usado para sorteio do Número Secreto

# CONSTANTES
CAR = "*" # Caractere usado para desenhar a estrutura do Jogo
TDT = 40 # # Tamanho da tela a ser desenhada
MAR = 2 # Margem de dois caracteres
INI = 1
FIM = 100
TVS = 3

# Listas
listaMsgs = [] # Variável de lista de msgs

# Funções
# Função para mostrar uma linha de Caracteres
def mostraLinha():
  print(CAR*TDT)

# Função para mostrar um texto centralizado entre um número de Caracteres
def msgCentro(msg):
  print(f"{CAR} {msg:^{TDT-MAR-MAR}} {CAR}")

# Função para mostrar um cabeçalho com texto entre linhas
def cabecalho(listaMsgs):
  mostraLinha()
  for msg in listaMsgs:
    msgCentro(msg)
  mostraLinha()

# Função para sortear um número secreto
def sorteianum():
  numeroSecreto = randint(INI,FIM)
  return numeroSecreto

# Função para pegar a Resposta e Testar se é um número
def pegaResposta():
  resposta = input(f"{CAR} Sua resposta: ")
  while not resposta.isdigit():
    listaMsgs = ["Resposta Inválida!", "Tente um Número!"]
    cabecalho(listaMsgs)
    resposta = input(f"{CAR} Sua resposta: ")
  resposta = int(resposta)
  return resposta

# Função para dar a dica
def dica(numeroSecreto, resposta):
  if numeroSecreto < resposta:
    cabecalho("Tente um Número MENOR!")
  else:
    cabecalho("Tente um Número MAIOR!")

# Função para Startar o Jogo
def startGame():
  TVS = 3
  numeroSecreto = sorteianum()
  listaMsgs = ["JOGO ADIVINHE O NÚMERO", "Powered by Gabriele Martini"]
  cabecalho(listaMsgs)
  playGame(TVS, numeroSecreto)

def playGame(TVS, numeroSecreto):
  for tentativas in range(TVS):
    resposta = pegaResposta()
    testeAcerto = resposta == numeroSecreto
    if testeAcerto:
      listaMsgs =  ["OLOKO BIXO!!!", "ACERTOU MEMO!!!", "PARABÉNS YOU WIN!"]
      cabecalho(listaMsgs)
      break
    elif tentativas != 2:
      listaMsgs = ["SE É RUIM D+", "NÃO É ASSIM CRIATURA!"]
      cabecalho(listaMsgs)
      dica(numeroSecreto, resposta)
    else:
        cabecalho("Mel Dels que Feio!!!")
  else:
    listaMsgs = ["FIM DE JOGO", "O NUM SECRETO ERA", numeroSecreto, "PARABÉNS YOU LOSE!"]
    cabecalho(listaMsgs)
    listaMsgs = ["Deseja jogar Novamente?", "[0 - NÃO]", "[1 - SIM]"]
    cabecalho(listaMsgs)
    resposta = pegaResposta()
    if resposta == 1:
     startGame()
    else:
     listaMsgs = ["FOI BOM JOGAR COM VOCÊ!", "ATÉ A PRÓXIMA"]
     cabecalho(listaMsgs)
                
  
# Programa Principal
startGame()