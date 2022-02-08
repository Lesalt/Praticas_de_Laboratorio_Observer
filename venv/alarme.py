from typing import Type
import observador
import pessoa
class Alarme:

    def __init__(self):
        self.beep = False
        self.dorminhocos = []
    def addPessoa(self, pessoa: Type[observador]):
        self.dorminhocos.append(pessoa)

    def estado_alarme(self):
        return self.beep

    def tocar(self):
        self.beep = True
        for pessoa in self.dorminhocos:
            pessoa.update()
            