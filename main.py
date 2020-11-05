for c in range(0, 10, 3):
    print(c)

from random import randint

n = randint(10, 100)
print(n)


import PySimpleGUI as sg

class TelaPython:
    def _init_(self):

        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar')]
         ]

        janela= sg.Window("Dados usuario").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar (self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()