from tkinter import*
from tkinter import messagebox , ttk

# ventana principal
ventana_principal = Tk()
ventana_principal.title("INFORMCION ESTUDIANTIL paul colmenares")
ventana_principal.geometry("800x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="yellow")


# abrir toplevel notas
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("Notas")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("600x400")
    toplevel_notas.config(bg="yellow")

    # salir
    def salir():
        messagebox.showinfo("Notas", "La ventana se va a cerrar")
        toplevel_notas.destroy()

    # menu salir
    barra_menu = Menu()
    toplevel_notas.config(menu=barra_menu)
    menu_salir = Menu(tearoff=0)
    menu_salir.add_command(label="Salir", command=salir)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)


    # texto procedimental
    proce=Label(toplevel_notas, text="procedimental =")
    proce.config(bg="blue", fg="black", font=("Helvetica",20))
    proce.place(x=20,y=30)

    # caja de texto para procedimental
    entry_proce=Entry(toplevel_notas)
    entry_proce.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_proce.focus_set()
    entry_proce.place(x=220 , y=30)

    # texto cognitivo
    cog=Label(toplevel_notas, text="cognitiva =")
    cog.config(bg="blue", fg="black", font=("Helvetica",20))
    cog.place(x=20,y=70)

    # caja de texto para cognitivo
    entry_cog=Entry(toplevel_notas)
    entry_cog.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_cog.focus_set()
    entry_cog.place(x=220 , y=70)

    # texto autoevaluacion
    auto=Label(toplevel_notas, text="autoevaluacion =")
    auto.config(bg="blue", fg="black", font=("Helvetica",19))
    auto.place(x=20,y=110)

    # caja de texto para autoevaluacion
    entry_auto=Entry(toplevel_notas)
    entry_auto.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_auto.focus_set()
    entry_auto.place(x=220 , y=110)

    # texto actitudinal
    acti=Label(toplevel_notas, text="actitudinal =")
    acti.config(bg="blue", fg="black", font=("Helvetica",20))
    acti.place(x=20,y=150)

    # caja de texto para actitudinal
    entry_acti=Entry(toplevel_notas)
    entry_acti.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_acti.focus_set()
    entry_acti.place(x=220 , y=150)

    # texto bimestral
    bime=Label(toplevel_notas, text="bimestral =")
    bime.config(bg="blue", fg="black", font=("Helvetica",20))
    bime.place(x=20,y=190)

    # caja de texto para bimestral
    entry_bime=Entry(toplevel_notas)
    entry_bime.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_bime.focus_set()
    entry_bime.place(x=220 , y=190)

    def convertir():
        messagebox.showinfo("Nota Difinitiva", "Operacion realizada")

        # variables notas
        entry_proce_def = float(entry_proce.get())
        entry_cog_def = float(entry_cog.get())
        entry_auto_def = float(entry_auto.get())
        entry_acti_def = float(entry_acti.get())
        entry_bime_def = float(entry_bime.get())

        entry_not_final = (0.3*entry_proce_def) + (0.3*entry_cog_def) + (0.1*entry_auto_def) + (0.1*entry_acti_def) + (0.2*entry_bime_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "El alumno reprobo la asignatura  xd  "+str(entry_not_final))
        else:
                messagebox.showinfo("Resultado", "El alumno aprobo la asignatura xd  "+str(entry_not_final))

    # boton para convertir
    bt_convertir = Button(toplevel_notas,text="Resultado", command=convertir)
    bt_convertir.place(x=200, y=250, width=150, height=100)



# abrir toplevel notas
def abrir_toplevel_salud():
    global toplevel_salud
    toplevel_salud = Toplevel()
    toplevel_salud.title("Salud")
    toplevel_salud.resizable(False, False)
    toplevel_salud.geometry("500x300")
    toplevel_salud.config(bg="yellow")

    # salir
    def salir():
        messagebox.showinfo("Salud", "La ventana se va a cerrar")
        toplevel_salud.destroy()

    # menu salir
    barra_menu = Menu()
    toplevel_salud.config(menu=barra_menu)
    menu_salir = Menu(tearoff=0)
    menu_salir.add_command(label="Salir", command=salir)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)

    # texto altura
    altura=Label(toplevel_salud, text="Altura =")
    altura.config(bg="blue", fg="black", font=("Helvetica",20))
    altura.place(x=20,y=30)

    # caja de texto para altura
    entry_altura=Entry(toplevel_salud)
    entry_altura.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_altura.focus_set()
    entry_altura.place(x=140 , y=30)

    # texto Peso
    peso=Label(toplevel_salud, text="Peso =")
    peso.config(bg="blue", fg="black", font=("Helvetica",20))
    peso.place(x=20,y=70)

    # caja de texto Peso
    entry_peso=Entry(toplevel_salud)
    entry_peso.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
    entry_peso.focus_set()
    entry_peso.place(x=140 , y=70)

    def convertir_imc ():
        estatura = float(entry_altura.get())
        peso = float(entry_peso.get())
        imc = peso / estatura**2
      
        if imc < 16:
            messagebox.showinfo("Resultado","Usted tiene delgadez severa")
        elif imc < 17:
            messagebox.showinfo("Resultado","Usted tiene delgadez moderada")
        elif imc < 18.5:
            messagebox.showinfo("Resultado","Usted tiene delgadez ligera")
        elif imc < 25:
            messagebox.showinfo("Resultado","Usted tiene Saludable")
        elif imc < 30:
            messagebox.showinfo("Resultado","Usted tiene Sobrepeso")
        elif imc < 35:
            messagebox.showinfo("Resultado","Usted tiene Obesidad grado I")
        elif imc < 40:
            messagebox.showinfo("Resultado","Usted tiene Obesidad grado II (grave)")
        else:
             messagebox.showinfo("Resultado","Usted tiene Obesidad grado III (mórbida)")
    # boton para convertir
    bt_convertir = Button(toplevel_salud,text="Resultado", command=convertir_imc)
    bt_convertir.place(x=200, y=170, width=150, height=100)


# salir
def salir():
    messagebox.showinfo("Informacion estudiantil", "La app se va a cerrar")
    ventana_principal.destroy()

# borrar
def borrar():
    messagebox.showinfo("Informacion", "Los datos se guardaron")




# menu salir
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)
menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)


# frame entrada de datos
frame_inf = Frame(ventana_principal)
frame_inf.config(bg="blue", width=550, height=350)
frame_inf.place(x=130, y=20)

# titulo
titulo=Label(frame_inf, text="informcion del estudiante")
titulo.config(bg="blue", fg="black", font=("Helvetica",20))
titulo.place(x=120,y=10)

# texto nombre
nombre=Label(frame_inf, text="nombre =")
nombre.config(bg="blue", fg="black", font=("Helvetica",20))
nombre.place(x=20,y=60)

# caja de texto para nombre
entry_nom=Entry(frame_inf)
entry_nom.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_nom.focus_set()
entry_nom.place(x=150 , y=60)

# texto edad
edad=Label(frame_inf, text="edad =")
edad.config(bg="blue", fg="black", font=("Helvetica",20))
edad.place(x=20,y=100)

# caja de texto para edad
entry_edad=Entry(frame_inf)
entry_edad.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_edad.focus_set()
entry_edad.place(x=150 , y=100)

# texto grado
grado=Label(frame_inf, text="grado =")
grado.config(bg="blue", fg="black", font=("Helvetica",20))
grado.place(x=20,y=140)

# caja de texto para grado
entry_grado=Entry(frame_inf)
entry_grado.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_grado.focus_set()
entry_grado.place(x=150 , y=140)

# texto TI
ti=Label(frame_inf, text="TI =")
ti.config(bg="blue", fg="black", font=("Helvetica",20))
ti.place(x=20,y=180)

# caja de texto para TI
entry_ti=Entry(frame_inf)
entry_ti.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_ti.focus_set()
entry_ti.place(x=150 , y=180)

# texto sede
sede=Label(frame_inf, text="sede =")
sede.config(bg="blue", fg="black", font=("Helvetica",20))
sede.place(x=20,y=220)

# caja de texto para sede
entry_sede=Entry(frame_inf)
entry_sede.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_sede.focus_set()
entry_sede.place(x=150 , y=220)

# boton para subir informacion
bt_sumar=Button(frame_inf, text="subir informacion",command=borrar)
bt_sumar.place(x=180,y=280 , width=200, height=30)

# etiqueta notas
lb_not=Label(ventana_principal, text="NOTAS")
lb_not.config(bg="yellow", fg="blue",font=("Helvetica",18))
lb_not.place(x=135 , y=380)

# etiqueta salud
lb_sal=Label(ventana_principal, text="SALUD")
lb_sal.config(bg="yellow", fg="blue",font=("Helvetica",18))
lb_sal.place(x=640 , y=380)

# boton notas
imagen_notas=PhotoImage(file="img/notas.png")
bt_notas=Button(ventana_principal,command=abrir_toplevel_notas)
bt_notas.config(image=imagen_notas)
bt_notas.place(x=100, y=420, width=150, height=150) 

# boton salud
bt_salud=Button(ventana_principal, command=abrir_toplevel_salud)
imagen_salud=PhotoImage(file="img/salud.png")
bt_salud.config(image=imagen_salud)
bt_salud.place(x=600, y=420, width=150, height=150)


ventana_principal.mainloop()