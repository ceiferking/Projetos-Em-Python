# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    #  Def inical para dar valor as variaveis e criar o layout da janela que sera craiada 
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        
        #  layout 
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        
    #  Inicia o programa e pede os inputs de entrada para realizar a geração do dado 
    def Iniciar(self):
        
        #  Criar uma janela 
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        
        #  Ler os valores da tela 
        self.eventos, self.valores = self.janela.Read()
        
        #  Executa as verificações atravez da interação com a janela criada 
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            if self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            #else:
            #    print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')
            
    #  Realisa Print no console 
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

#  Atribui a def Inicar para ser executada apos executar o script 
simulador = SimuladorDeDado()
simulador.Iniciar()