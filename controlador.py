from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)
    
    def calcular(self, operacion):
        self.modelo.calcular(operacion)
        resultado = self.modelo.resultado
     
        if es_funcion:
            x = np.linspace(-10, 10, 1000)
            y = eval(resultado)
            self.vista.actualizar_grafico(x, y)
