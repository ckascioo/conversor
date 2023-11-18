# Instalação:
    # pip install pyttsx3
    # pip install pygame

import pyttsx3 # Biblioteca que irá fazer a conversão digitada
import gtts
import pygame
import time
import os

conversor = pyttsx3.init() # Conversor

# Intro:
nome = input('Digite seu nome: ')
escolha = 'Escolha uma das opções'
intro = 'Bem-vindo' + nome + 'ao Conversor de Texto em Fala'
print(f'Bem-vindo {nome} ao Conversor de Texto em Fala!\n----------------------------------')
conversor.say(intro) # Ler a mensagem
conversor.runAndWait()
conversor.say(escolha) # Ler a mensagem
conversor.runAndWait()

pygame.mixer.init()
pg = pygame.mixer.music

while True:
    opcao = input('[1] - Digitar o que deseja escutar\n[2] - Converter o texto.txt em voz\nEscolha uma das opções: ')
    if int(opcao) == 1:
        while True:
            mensagem = input('Digite o que quer escutar ou voltar para ir para o Menu anterior: ') # Mensagem que deseja ouvir
            if mensagem == 'voltar':
                opcao = input('[1] - Digitar o que deseja escutar\n[2] - Converter o texto.txt em voz\nEscolha uma das opções: ')
                break #Correção
            conversor.say(mensagem) # Ler a mensagem
            conversor.runAndWait()

    elif int(opcao) == 2:
        texto_completo = ""
        with open('texto.txt', 'r') as arquivo:
            for linha in arquivo:
                texto_completo += linha

        if texto_completo:
            texto = gtts.gTTS(texto_completo,lang='pt-br')
            texto.save('texto.mp3')
            pg.load('texto.mp3')
            pg.play()

            while pg.get_busy():
                pygame.time.Clock().tick(10)  # Aguarda 10 milissegundos

            # Parar a reprodução
            pg.stop()
            # Fechar o arquivo de áudio
            pg.unload()

            # Remover o arquivo de áudio
            os.remove('texto.mp3')

        else:
            print('O arquivo texto.txt está vazio!')

    else:
        print('Opção invalida!')
    


