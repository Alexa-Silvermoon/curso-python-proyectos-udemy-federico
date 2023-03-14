from tkinter import *  # ideal para sistemas de facturacion
import random  # generar numeros de tickets ficticios
import datetime  # fecha y hora para los recibos
from tkinter import filedialog, messagebox  # guardar recibo en txt mensaje de dialogo

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# calculadora
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


# calculadora
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


# calculadora
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


# activar o desactivar casillas check de columna comidas
def revisar_check():
    # columna de comida
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)  # activar check de comida y desbloquear textbox
            if cuadros_comida[
                x].get() == '0':  # solamente si el cuadro tiene 0 la vuelve a deshabilitar si no esta el cursor encima
                cuadros_comida[x].delete(0, END)  # se va el 0 cuando activamos cualquiera de nuestras comidas
            cuadros_comida[x].focus()  # automaticamente el curso aparece en textbox comida al activar el check
        else:
            cuadros_comida[x].config(state=DISABLED)  # si se quita el check, el textbox se vuelve a deshabilitar
            texto_comida[x].set('0')  # el textbox vuelve a marcar 0
        x += 1

    # columna de bebida
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)  # activar check de bebida y desbloquear textbox
            if cuadros_bebida[
                x].get() == '0':  # solamente si el cuadro tiene 0 la vuelve a deshabilitar si no esta el cursor encima
                cuadros_bebida[x].delete(0, END)  # se va el 0 cuando activamos cualquiera de nuestras bebidas
            cuadros_bebida[x].focus()  # automaticamente el curso aparece en textbox bebida al activar el check
        else:
            cuadros_bebida[x].config(state=DISABLED)  # si se quita el check, el textbox se vuelve a deshabilitar
            texto_bebida[x].set('0')  # el textbox vuelve a marcar 0
        x += 1

    # columna de postre
    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)  # activar check de postre y desbloquear textbox
            if cuadros_postres[
                x].get() == '0':  # solamente si el cuadro tiene 0 la vuelve a deshabilitar si no esta el cursor encima
                cuadros_postres[x].delete(0, END)  # se va el 0 cuando activamos cualquiera de nuestros postres
            cuadros_postres[x].focus()  # automaticamente el curso aparece en textbox postre al activar el check
        else:
            cuadros_postres[x].config(state=DISABLED)  # si se quita el check, el textbox se vuelve a deshabilitar
            texto_postres[x].set('0')  # el textbox vuelve a marcar 0
        x += 1


def total():
    # sub total de comidas
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    # print(sub_total_comida)

    # sub total de bebidas
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    # print(sub_total_bebida)

    # sub total de postres
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    # print(sub_total_postres)

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07  # 7% de impuestos
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)  # borrar informacion de tickets anteriores
    num_recibo = f'N# - {random.randint(1000, 9999)}'  # numero de recibo ficticio
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 73 + '\n')
    texto_recibo.insert(END, 'Items\t\tCantidad\t\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 87 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_comidas[x]}\t\t{comida.get()}\t\t$ {round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t$ {round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postres[x]}\t\t{postres.get()}\t\t$ {round(int(postres.get()) * precios_postres[x], 2)}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 87 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida: \t\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida: \t\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo  del  Postre: \t\t\t\t{var_costo_postres.get()}\n')

    texto_recibo.insert(END, f'-' * 87 + '\n')
    texto_recibo.insert(END, f'Sub-Total: \t\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t\t{var_total.get()}\n')

    texto_recibo.insert(END, f'*' * 73 + '\n')
    texto_recibo.insert(END, '\tMuchas Gracias Por Su Visita')


# guardar toda la informacion en un txt
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'El recibo ha sido guardado')  # cuadro de mensaje de advertencia


# cuando llega nuevo cliente, volver a dejar la pantalla limpia
def resetear():
    texto_recibo.delete(0.1, END)  # limpia el cuadro del recibo

    # dejar cuadro de texto de cada columna en 0
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    # desactivar cuadro de texto de cada columna
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    # desactivar checkbox de cada columna
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    # dejar cuadro de texto de costos limpio
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# Borrado de pantalla
# system("clear")


# Iniciar tkinter
aplicacion = Tk()

# Resolucion de pantalla
aplicacion.geometry('1150x630+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Sistema de facturación - Alexander Millan")

# Color de fondo de la venta
aplicacion.config(bg="burlywood")

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg="azure4", font=("Andale Mono", 58),
                        bg="burlywood", width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold",),
                           bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold",),
                           bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold",),
                           bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

# Lista de productos
lista_comidas = ["pollo", "cordero", "salmon", "merluza", "kebab", "pizza1", "pizza2", "pizza3"]
lista_bebidas = ["agua", "soda", "jugo", "cola", "vino1", "vino2", "cerveza1", "cerveza2"]
lista_postres = ["helado", "fruta", "brownies", "flan", "mousse", "pastel1", "pastel2", "pastel3"]

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 19, "bold",),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)

    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])

    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 19, "bold",),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])

    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    variables_postres.append("")
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=("Dosis", 19, "bold",),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # Crear los cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=("Dosis", 18, "bold"),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])

    cuadros_postres[contador].grid(row=contador,
                                   column=1)

    contador += 1

# Postres
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo comida",
                              font=("dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo bebida",
                              font=("dosis", 12, "bold"),
                              bg="azure4",
                              fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                               text="Costo postres",
                               font=("dosis", 12, "bold"),
                               bg="azure4",
                               fg="white")
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                          text="Subtotal",
                          font=("dosis", 12, "bold"),
                          bg="azure4",
                          fg="white")
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=("Dosis", 12, "bold"),
                       bd=1,
                       width=10,
                       state="readonly",
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                           text="Impuestos",
                           font=("dosis", 12, "bold"),
                           bg="azure4",
                           fg="white")
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=("Dosis", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                       text="Total",
                       font=("dosis", 12, "bold"),
                       bg="azure4",
                       fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=10,
                    state="readonly",
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ["total", "recibo", "guardar", "resetear"]
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=9)  # ancho de botones

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area de recibo (donde aparece la factura)
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    width=49,
                    height=12)  # altura del panel derecho (calculador, botones de calculadora, recibo, botones)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=37,  # ancho de txt enciama de los botones de calculadora
                          bd=1)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       'CE', '0', '=', '/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))

# 12 es CE
botones_guardados[12].config(command=borrar)

botones_guardados[13].config(command=lambda: click_boton('0'))

# 14 es =
botones_guardados[14].config(command=obtener_resultado)

botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla no cierre
aplicacion.mainloop()

# configurar la ventana tkinter https://www.udemy.com/course/python-total/learn/lecture/29403202?start=15#questions
# paneles https://www.udemy.com/course/python-total/learn/lecture/29424056#questions
# checkbuttons: https://www.udemy.com/course/python-total/learn/lecture/29424064?start=15#questions
# cuadros de entrada: https://www.udemy.com/course/python-total/learn/lecture/29424074#questions
# valores por defecto: https://www.udemy.com/course/python-total/learn/lecture/29429914#questions
# panel de costos: https://www.udemy.com/course/python-total/learn/lecture/29429926?start=15#questions
# botones y recibo: https://www.udemy.com/course/python-total/learn/lecture/29429930#questions
# calculadora: https://www.udemy.com/course/python-total/learn/lecture/29429938?start=15#questions
# funcionalidad de calculadora: https://www.udemy.com/course/python-total/learn/lecture/29441602?start=420#questions
# configurar los checkbuttons: https://www.udemy.com/course/python-total/learn/lecture/29429944#questions
# calcular totales: https://www.udemy.com/course/python-total/learn/lecture/29420834?start=735#questions
# generar recibo: https://www.udemy.com/course/python-total/learn/lecture/29429952#questions
# guardar recibo en archivo: https://www.udemy.com/course/python-total/learn/lecture/29429956?start=15#questions
# resetear pantalla: https://www.udemy.com/course/python-total/learn/lecture/29429960#questions

# Made By: CHRISTIAN ALEXANDER MARTINEZ MILLAN