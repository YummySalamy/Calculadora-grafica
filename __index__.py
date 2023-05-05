from controlador import Controlador

controlador = Controlador()

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np

# Clase para la interfaz gráfica
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Matemática")

        # Variables de entrada y salida
        self.expression = tk.StringVar()
        self.result = tk.StringVar()

        # Entrada de texto
        self.expression_entry = ttk.Entry(self.master, width=50, textvariable=self.expression, font=("Arial", 16))
        self.expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones de operaciones matemáticas
        ttk.Button(self.master, text="sin", command=lambda: self.add_expression("np.sin(")).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.master, text="cos", command=lambda: self.add_expression("np.cos(")).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="tan", command=lambda: self.add_expression("np.tan(")).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(self.master, text="log", command=lambda: self.add_expression("np.log(")).grid(row=1, column=3, padx=5, pady=5)

        ttk.Button(self.master, text="sqrt", command=lambda: self.add_expression("np.sqrt(")).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.master, text="^", command=lambda: self.add_expression("**")).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="(", command=lambda: self.add_expression("(")).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.master, text=")", command=lambda: self.add_expression(")")).grid(row=2, column=3, padx=5, pady=5)

        # Botones de números y operadores
        ttk.Button(self.master, text="7", command=lambda: self.add_expression("7")).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(self.master, text="8", command=lambda: self.add_expression("8")).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="9", command=lambda: self.add_expression("9")).grid(row=3, column=2, padx=5, pady=5)
        ttk.Button(self.master, text="+", command=lambda: self.add_expression("+")).grid(row=3, column=3, padx=5, pady=5)

        ttk.Button(self.master, text="4", command=lambda: self.add_expression("4")).grid(row=4, column=0, padx=5, pady=5)
        ttk.Button(self.master, text="5", command=lambda: self.add_expression("5")).grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="6", command=lambda: self.add_expression("6")).grid(row=4, column=2, padx=5, pady=5)
        ttk.Button(self.master, text="-", command=lambda: self.add_expression("-")).grid(row=4, column=3, padx=5, pady=5)

        ttk.Button(self.master, text="1", command=lambda: self.add_expression("1")).grid(row=5, column=0, padx=5, pady=5)
        ttk.Button(self.master, text="2", command=lambda: self.add_expression("2")).grid(row=5, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="3", command=lambda: self.add_expression("3")).grid(row=5, column=2, padx=5, pady=5)
        ttk.Button(self.master, text="*", command=lambda: self.add_expression("*")).grid(row=5, column=3, padx=5, pady=5)
    
        ttk.Button(self.master, text="0", command=lambda: self.add_expression("0")).grid(row=6, column=0, padx=5, pady=5)
        ttk.Button(self.master, text=".", command=lambda: self.add_expression(".")).grid(row=6, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="C", command=lambda: self.clear_expression()).grid(row=6, column=2, padx=5, pady=5)
        ttk.Button(self.master, text="/", command=lambda: self.add_expression("/")).grid(row=6, column=3, padx=5, pady=5)

        # Botón para calcular
        ttk.Button(self.master, text="Calcular", command=lambda: self.calculate_expression()).grid(row=7, column=0, columnspan=4, padx=10, pady=10)
    
        # Etiqueta para mostrar el resultado
        ttk.Label(self.master, textvariable=self.result, font=("Arial", 16)).grid(row=8, column=0, columnspan=4, padx=10, pady=10)
    
def add_expression(self, value):
    """Agrega un valor a la expresión matemática"""
    self.expression.set(self.expression.get() + value)

def clear_expression(self):
    """Borra la expresión matemática"""
    self.expression.set("")
    self.result.set("")

def calculate_expression(self):
    """Calcula el resultado de la expresión matemática"""
    try:
        result = eval(self.expression.get())
        self.result.set(result)
    except:
        self.result.set("Error")
