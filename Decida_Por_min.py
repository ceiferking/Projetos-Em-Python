# Faça uma pergunta para o programa e ele tera que lhe dar uma resposta.
from fileinput import close
import random
import PySimpleGUI as sg

class DecidaPorMin():
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você quem sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]
        
    def Iniciar(self):
        # Layout
        self.layout = [
            [sg.Text('Faça uma pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(42,10))],
            [sg.Button('Decida por min')]
        ]
        # Criar a janela
        self.janela = sg.Window('Decida por Min!',layout=self.layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por min':
                print(random.choice(self.respostas))
            else:
                break
        
Decida = DecidaPorMin()
Decida.Iniciar()