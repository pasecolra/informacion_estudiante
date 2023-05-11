from tkinter import*
from tkinter import messagebox , ttk

# ventana principal
ventana_principal = Tk()
ventana_principal.title("INFORMCION ESTUDIANTIL")
ventana_principal.geometry("800x600")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="yellow")


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
entry_x=Entry(frame_inf)
entry_x.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_x.focus_set()
entry_x.place(x=150 , y=60)

# texto edad
nombre=Label(frame_inf, text="edad =")
nombre.config(bg="blue", fg="black", font=("Helvetica",20))
nombre.place(x=20,y=100)

# caja de texto para edad
entry_x=Entry(frame_inf)
entry_x.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_x.focus_set()
entry_x.place(x=150 , y=100)

# texto grado
nombre=Label(frame_inf, text="grado =")
nombre.config(bg="blue", fg="black", font=("Helvetica",20))
nombre.place(x=20,y=140)

# caja de texto para grado
entry_x=Entry(frame_inf)
entry_x.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_x.focus_set()
entry_x.place(x=150 , y=140)

# texto TI
nombre=Label(frame_inf, text="TI =")
nombre.config(bg="blue", fg="black", font=("Helvetica",20))
nombre.place(x=20,y=180)

# caja de texto para TI
entry_x=Entry(frame_inf)
entry_x.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_x.focus_set()
entry_x.place(x=150 , y=180)

# texto sede
nombre=Label(frame_inf, text="sede =")
nombre.config(bg="blue", fg="black", font=("Helvetica",20))
nombre.place(x=20,y=220)

# caja de texto para sede
entry_x=Entry(frame_inf)
entry_x.config(bg="blue", fg="black",font=("Time New Roman",16), width=20)
entry_x.focus_set()
entry_x.place(x=150 , y=220)

# boton para subir informacion
bt_sumar=Button(frame_inf, text="subir informacion",)
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
bt_notas=Button(ventana_principal)
bt_notas.place(x=100, y=420, width=150, height=150) 

# boton salud
imagen_salud=PhotoImage(file="img/salud.png")
bt_salud=Button(ventana_principal)
bt_salud.config(image=imagen_salud)
bt_salud.place(x=600, y=420, width=150, height=150)


ventana_principal.mainloop()