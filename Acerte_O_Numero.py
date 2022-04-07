# Projeto - Chute o número
# objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando acertar o número gerado até eu acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    # +++++++++Def inicial para dar valor minimo e maximo e as variaveis necessarias+++++++++
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
            # Layout da janela
        self.layout = [
            [sg.Text('Seu Chute',size=(20,0))],
            [sg.Input(size=(10,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,15))]
            ]
        # criar janela
        self.janela = sg.Window('Chute o numero!',layout=self.layout)
    
    # ++++Def Iniciar responsavel pela função geral do algoritmo++++
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        # Realisa a checagem das variaveis na execução do programa e executa enquanto essas variaveis não forem satisfatorias++++
        try:
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # ++++Executa o codigo de checagem da caixa de texto++++
                if self.evento == 'Chutar!':
                    # ++++Executa o codigo ate que a variavel tentar_novamente receba False++++
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        # ++++Executa a checagem o valor digitado se é maior que o valor aleatorio gerado++++
                        # ++++Pede outro valor atravez da Def PedirValorAleatorio++++
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!:')
                            break
                        # ++++Executa a checagem o valor digitado se é menor que o valor aleatorio gerado++++
                        # ++++Pede outro valor atravez da Def PedirValorAleatorio++++
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!:')
                            break
                        # ++++Executa a checagem caso o valor aleatorio seja igual ao valor digitado++++
                        # ++++Executa um print caso acerte o valor++++
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!')
                            break
                else:
                    break
                    

        # ++++Chama a função iniciar novamente caso digite qualquer outra coisa que não seja um numero++++
        # ++++Apresenta menssagem de erro++++
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            
    # Chama novamente os valores de checagem da janela
    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()
        
    # ++++Def responsavel por gerar um numero aleatorio com a biblioteca random++++
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)
    
    # ++++Def Responsavel por pedir um valor para o usuario tentar acertar o numero gerado++++
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número:')

# ++++Instancia as variaveis do codigo para execução++++
chute = ChuteONumero()
chute.Iniciar()