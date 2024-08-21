import tkinter as tk
from tkinter import *


calc = tk.Tk()
calc.title("Calculadora de Pablo")  
calc.geometry("410x700") 
calc.resizable(False,False)
calc.configure(bg="#5a5f63")

ecuacion = ""

def show(valor):
    global ecuacion
    ecuacion+=valor
    label_resultado.configure(text=ecuacion)

def clear():
    global ecuacion
    ecuacion=""
    label_resultado.configure(text=ecuacion)

def calcular():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = eval(ecuacion)
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def C_to_F():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = (ecuacion*9/5)+32
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def F_to_C():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = (ecuacion-32)*5/9
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def cm_to_in():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion*0.3937
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def in_to_cm():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion/0.3937
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def Km_to_Mi():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion*0.621371
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def Mi_to_Km():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion/0.621371
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def Kg_to_lb():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion*2.20462
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)

def lb_to_Kg():
    global ecuacion
    resultado = ""
    if ecuacion != "":
        try:
            resultado = ecuacion/2.20462
        except:
            resultado ='ERROR'
            resultado = ""
    label_resultado.configure(text=resultado)
     

label_resultado = tk.Label(calc, text="", font=('Times New Roman', 50, 'bold'), anchor="e").place(x=10, y=3,width=390, height=127 )

b0 = tk.Button(calc, text="0", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('0')).place(x=10, y=605, width=190, height=90)
b_punto = tk.Button(calc, text=".", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('.')).place(x=210, y=605, width=90, height=90)
b_igual = tk.Button(calc, text="=", font=('Times New Roman', 30, 'bold'), bd=1 , fg="#c46104", command=calcular()).place(x=310, y=605, width=90, height=90)

b1 = tk.Button(calc, text="1", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('1')).place(x=10, y=510, width=90, height=90)
b2 = tk.Button(calc, text="2", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('2')).place(x=110, y=510, width=90, height=90)
b3 = tk.Button(calc, text="3", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('3')).place(x=210, y=510, width=90, height=90)
b_mas = tk.Button(calc, text="+", font=('Times New Roman', 30, 'bold'),bd=1 , fg="#c46104", command=show('+')).place(x=310, y=510, width=90, height=90)

b4 = tk.Button(calc, text="4", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('4')).place(x=10, y=415, width=90, height=90)
b5 = tk.Button(calc, text="5", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('5')).place(x=110, y=415, width=90, height=90)
b6 = tk.Button(calc, text="6", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('6')).place(x=210, y=415, width=90, height=90)
b_menos = tk.Button(calc, text="-", font=('Times New Roman', 30, 'bold'), bd=1 , fg="#c46104", command=show('-')).place(x=310, y=415, width=90, height=90)

b7 = tk.Button(calc, text="7", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('7')).place(x=10, y=320, width=90, height=90)
b8 = tk.Button(calc, text="8", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('8')).place(x=110, y=320, width=90, height=90)
b9 = tk.Button(calc, text="9", font=('Times New Roman', 30, 'bold'), bd=1, fg="#3b598a", command=show('9')).place(x=210, y=320, width=90, height=90)
b_multiplicar = tk.Button(calc, text="x", font=('Script', 30), bd=1 , fg="#c46104", command=show('*')).place(x=310, y=320, width=90, height=90)

b_clear = tk.Button(calc, text="C", font=('Script', 30),bd=1, fg="#fc5e03", command=clear()).place(x=10, y=225, width=90, height=90)
b_cambio = tk.Button(calc, text="+/-", font=('Times New Roman', 30, 'bold'),bd=1, fg="#343336", command=show('+/-')).place(x=110, y=225, width=90, height=90)
b_porcentaje = tk.Button(calc, text="%", font=('Times New Roman', 30, 'bold'),bd=1, fg="#343336", command=show('%')).place(x=210, y=225, width=90, height=90)
b_dividir = tk.Button(calc, text="÷", font=('Script', 30), bd=1 , fg="#c46104", command=show('÷')).place(x=310, y=225, width=90, height=90)

b_celsius = tk.Button(calc, text="°C⇒°F", font=('Script', 20), bd=1, fg="#02660a", command=C_to_F()).place(x=10, y=180, width=90, height=40)
b_kilos = tk.Button(calc, text="Kg⇒lb", font=('Times New Roman', 20), bd=1, fg="#02660a", command=Kg_to_lb()).place(x=110, y=180, width=90, height=40)
b_cm = tk.Button(calc, text="cm⇒in", font=('Times New Roman', 20), bd=1, fg="#02660a", command=cm_to_in().place(x=210, y=180, width=90, height=40)
b_km = tk.Button(calc, text="Km⇒Mi", font=('Script', 20), bd=1, fg="#02660a", command=Km_to_Mi()).place(x=310, y=180, width=90, height=40)

b_farengei = tk.Button(calc, text="°F⇒°C", font=('Script', 20), bd=1, fg="#02660a", command=F_to_C()).place(x=10, y=135, width=90, height=40)
b_libras = tk.Button(calc, text="lb⇒Kg", font=('Times New Roman', 20), bd=1, fg="#02660a", command=lb_to_Kg()).place(x=110, y=135, width=90, height=40)
b_in = tk.Button(calc, text="in⇒cm", font=('Times New Roman', 20), bd=1, fg="#02660a", command=in_to_cm()).place(x=210, y=135, width=90, height=40)
b_mi = tk.Button(calc, text="Mi⇒Km", font=('Script', 20), bd=1, fg="#02660a", command=Mi_to_Km()).place(x=310, y=135, width=90, height=40)






calc.mainloop()
