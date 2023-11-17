# Instalação:
    # pip install pyttsx3

import pyttsx3 # Biblioteca que irá fazer a conversão

conversor = pyttsx3.init() # Conversor
while True:
    mensagem = input('Digite o que quer escutar: ') # Mensagem que deseja ouvir
    conversor.say(mensagem) # Ler a mensagem
    conversor.runAndWait() 