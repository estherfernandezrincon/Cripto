from tkinter import *
from tkinter import ttk

import cripto



class Cripto(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width= 900, height= 500)
        self.pack_propagate(False)
        s = ttk.Style()
        s.theme_use('alt')

        
        self.label_euros = ttk.Label(self, text="€ invertidos" , font="Times")
        self.label_euros.pack(side=LEFT, fill=X, expand=True, padx=2, pady=2)

        self.entry_euros = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=5)
        self.entry_euros.pack(side=LEFT, fill= X, expand= True, padx= 0, pady=0)

        self.label_valor = ttk.Label(self, text="valor actual" , font="Times")
        self.label_valor.pack(side=LEFT, fill=X, expand=True, padx=2, pady=2)

        self.entry_valor = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=5)
        self.entry_valor.pack(side=LEFT, fill= X, expand= True, padx= 0, pady=0)



        self.botonCalcular = ttk.Button( self, text="Calcular")        
        self.botonCalcular.pack(side=RIGHT, fill=X, expand=True, padx=35, pady=35)


class NuevaTransaccion(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width= 500, height= 300)
        self.pack_propagate(False)
        s = ttk.Style()
        s.theme_use('alt')


        self.label_From = ttk.Label(self, text="From" , font="Times")
        self.label_From.pack(side=LEFT,  fill= X, expand=True, padx=0, pady=0)

        self.entry_From = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=1)
        self.entry_From.pack(side=LEFT,  fill= X, expand= True,padx= 1, pady=0)


        

        self.label_To = ttk.Label(self, text="To" , font="Times")
        self.label_To.pack(side=RIGHT, fill= X, expand=True, padx=0, pady=0)

        self.entry_To = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=1)
        self.entry_To.pack(side=RIGHT, fill= X, expand= True, padx= 1, pady=0)

        self.botonAceptar = ttk.Button( self, text="Aceptar")        
        self.botonAceptar.pack(side=RIGHT, fill=X, expand=True, padx=35, pady=35)



        self.label_Q = ttk.Label(self, text="Q" , font="Times")
        self.label_Q.pack(side=LEFT,  fill= X, expand=True, padx=0, pady=0)

        self.entry_Q = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=1)
        self.entry_Q.pack(side=LEFT,  fill= X, expand= True,padx= 1, pady=0)



        
        self.label_Q = ttk.Label(self, text="Q" , font="Times")
        self.label_Q.pack(side=LEFT,  fill= X, expand=True, padx=0, pady=0)

        self.entry_Q = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=1)
        self.entry_Q.pack(side=LEFT,  fill= X, expand= True,padx= 1, pady=0)



        self.label_precio_und = ttk.Label(self, text="P.U" , font="Times")
        self.label_precio_und.pack(side=TOP, fill=BOTH, expand=True, padx=2, pady=2)

        self.entry_precio_und = ttk.Entry(self, cursor="arrow",foreground="red", font="Times,10", width=5)
        self.entry_precio_und.pack(side=TOP, fill= BOTH, expand= True, padx= 0, pady=0)



        self.botonCancelar = ttk.Button( self, text="Cancelar")        
        self.botonCancelar.pack(side=RIGHT, fill=X, expand=True, padx=35, pady=35)


class Cuadricula(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack_propagate(False)
        s = ttk.Style()
        s.theme_use('alt')

        self.canvas = Canvas(width=300, height=100, bg='white')
        self.canvas.pack(expand= YES, fill= BOTH)
        self.canvas.create_rectangle(10,10,800,90, fill='green')
        self.canvas.create_line(20,20,20,90)
        self.canvas.create_line(40,20,40,90)
        self.canvas.create_line(60,20,60,90)
        self.canvas.create_line(20,20,800,20)
        self.canvas.create_line(20,40,800,40)
        self.canvas.create_line(20,60,800,60)
        self.canvas.create_line(20,80,800,80)


class MainClass(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width= 900, height= 400)
        self.pack_propagate(False)
        s = ttk.Style()
        s.theme_use('alt')

        self.cuadricula= Cuadricula(self)
        self.cuadricula.pack(side=TOP, fill= BOTH, expand= TRUE)

        self.nueva_transaccion = NuevaTransaccion(self)
        self.nueva_transaccion.pack(side= TOP, fill= BOTH, expand= TRUE)

        self.cripto= Cripto(self)
        self.cripto.pack(side=TOP, fill=BOTH, expand= TRUE)
        