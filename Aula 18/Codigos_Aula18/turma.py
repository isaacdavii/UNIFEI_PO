import tkinter as tk
from tkinter import messagebox

class Turma:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nome(self):
        return self.__nome

class LimiteInsereTurmas(tk.Toplevel):
    def __init__(self, controle):
        pass