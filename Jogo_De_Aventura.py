# Projeto - Jogo de aventura
# Um jogo de decisões onde terei que criar varios finais baseados nas respostas que forem dadas.

from ast import For, While
from fileinput import close
from time import sleep
import PySimpleGUI as sg


# Qual é o cenário : Uma guerra entre duas nações.
class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s)' # norte = LadoA, sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # espada = Lado1, escudo Lado = Lado2
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico)' # linha de frente = Lado1, tático = lado2
        self.digite1 = 'Digite Apenas as respostas dentro dos parenteses ao lado da pergunta.'
        self.digite2 = 'Por favor reinicie apertando no botão iniciar e responda corretamente.'
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nossa batalha!'
        
    def Iniciar(self):
        # Layout
        self.layout = [
            [sg.Output(size=(60,10),key='resposta')],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar  a janela
        self.janela = sg.Window('Jogo de Aventura',layout=self.layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)

                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)
                else:
                    print(self.digite1)
                    sleep(1)
                    print(self.digite2)
            else:
                break
    
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()
            

jogo = JogoAventura()
jogo.Iniciar()