import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        
        self.label_operacion = ttk.Label(self.ventana, text="Operación:")
        self.label_operacion.pack()
        
        self.entry_operacion = ttk.Entry(self.ventana)
        self.entry_operacion.pack()
        
        self.button_calcular = ttk.Button(self.ventana, text="Calcular", command=self.calcular)
        self.button_calcular.pack()
        
        self.figure = plt.figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.ventana)
        self.canvas.get_tk_widget().pack()
        
        self.ventana.mainloop()
    
    def calcular(self):
        operacion = self.entry_operacion.get()
        self.controlador.calcular(operacion)
        
    def actualizar_grafico(self, x, y):
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        self.canvas.draw()
