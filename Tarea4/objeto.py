class Persona:

    def __init__(self, nombre, edad,activo,saldo):
        self.nom=nombre
        self.eda=edad
        self.act=activo
        self.sald= saldo


    def getNombre(self):
        return self.nom

    def getEdad(self):
        return  self.eda

    def getActivo(self):
        return self.act

    def getSaldo(self):
        return self.sald