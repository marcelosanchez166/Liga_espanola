"""Pregunte cuantos equipos desea ingresar"""


from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ConexionDB
from ConexionDB import *


# conexion=sqlite3.connect("Torneo")
# cursor=conexion.cursor()


raiz=Tk()
raiz.title(" Aplicacion de Torneo " )
#raiz.geometry("750x750")
raiz.config(bg="#A9A9E9")


FrameCampos=Frame(raiz)
FrameCampos.grid(row=0, column=0, sticky='nsew')
FrameCampos.config(bg="#E98232")#color del frame
FrameCampos.config(width="1300", height="300")#Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
FrameCampos.grid_propagate(0)
FrameCampos.config(bd=2)#tamaño al borde del frame
FrameCampos.config(relief="raised")#tipo de marco para el frame


NameEQ=StringVar()
Capitan=StringVar()



NombreEQlabel=Label(FrameCampos,text="Nombre de EQ ")
NombreEQlabel.grid(row=1,column=0,pady=4, padx=2)
txtNombreEQ=Entry(FrameCampos, textvariable=NameEQ)
txtNombreEQ.grid(row=1,column=1,padx=8, pady=8)
txtNombreEQ.focus()

Capitanlabel=Label(FrameCampos, text="Nombre de Capitan ")
Capitanlabel.grid(row=2,column=0,pady=4, padx=2)
Capitantxt=Entry(FrameCampos, textvariable=Capitan)
Capitantxt.grid(row=2,column=1,padx=8, pady=8)



Monday=IntVar()
tuesday=IntVar()
wendsday=IntVar()
trushday=IntVar()
friday=IntVar()
Nueve=IntVar()
Diez=IntVar()
Once=IntVar()

class Equipos:
          def __init__(self):
                    Dias_disponibles=Label(FrameCampos, text="Seleccion de Horarios Disponibles ")
                    Dias_disponibles.grid(row=3,column=0,sticky=W+E)
                    """CheckBontones para seleccionar dias disponibles de juego de los equipos"""
                    #Con la opcion variable=Futbol o cualquier otra opcion se le esta pasando al checkbox la variable con valor entero 
                    # ya sea cero o uno
                    #el metodo command se le pasa la funcion al boton en este caso al checkbox 
                    Lunes=Checkbutton(FrameCampos, text="Lunes", variable=Monday, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Lunes.grid(row=3,column=1 , sticky=E)
                    Martes=Checkbutton(FrameCampos, text="Martes", variable=tuesday, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Martes.grid(row=3,column=2)
                    Miercoles=Checkbutton(FrameCampos, text="Miercoles", variable=wendsday, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Miercoles.grid(row=3,column=3)
                    Jueves=Checkbutton(FrameCampos, text="Jueves", variable=trushday, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Jueves.grid(row=3,column=4)
                    Viernes=Checkbutton(FrameCampos, text="Viernes", variable=friday, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Viernes.grid(row=3,column=5)
                    #La opcion onvalue=1 le dice al checkbox que esta marcada, y la opcion offvalue=0 le dice que no esta seleccionado, y cuando llega al if
                    #Hace la validacion si el checkbox esta seleccionado

                    Nuev=Checkbutton(FrameCampos, text="9:00 AM", variable=Nueve, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Nuev.grid(row=4,column=1 , sticky=E)
                    Die=Checkbutton(FrameCampos, text="10:00 AM", variable=Diez, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Die.grid(row=4,column=2)
                    Onc=Checkbutton(FrameCampos, text="11:00 AM", variable=Once, onvalue=1, offvalue=0, command=self.SeleccionarHorario)
                    Onc.grid(row=4,column=3)


                    ingresarUsuarios=Button(FrameCampos, text="Insertar", command=self.IngresarEQ )
                    ingresarUsuarios.grid(row=6, column=0 , sticky=W+E)
                    IngresoHorario=Button(FrameCampos, text="Ingresar Horario", command=self.SeleccionarHorario )
                    IngresoHorario.grid(row=6, column=1 , sticky=W+E)

          def IngresarEQ(self):
                    #lista=[(NameEQ.get(),Capitan.get())]
                    #cursor.execute("INSERT INTO Equipos VALUES (NULL,?,?)", lista)
                    ConexionDB.Cone = DataBase()
                    """ConexionDB.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+
                    "','" + Capitan.get() +"')")"""
                    ConexionDB.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+
                    "','" + Capitan.get() +"')")
                    ConexionDB.Cone.connec.commit()
                    #ConexionDB.Cone.connec.close()
                    messagebox.showinfo("INFO", "Equipo ingresado Exitosamente")
                    NameEQ.set("")
                    Capitan.set("")    ##Metodo .set para limpiar los entry
                    txtNombreEQ.focus()
                    #ConexionDB.Cone.connec.close()
          def SeleccionarHorario(self):
                    opcionescogida=""
                    if Monday.get()==1:
                              opcionescogida+="Lunes  "
                    if tuesday.get()==1:
                              opcionescogida+="Martes  "
                    if wendsday.get()==1:
                              opcionescogida+="Miercoles  "
                    if trushday.get()==1:
                              opcionescogida+="Jueves  "
                    if friday.get()==1:
                              opcionescogida+="Viernes  "
                    #mensaje.config(text=opcionescogida)#Se le pasa al label la opcion escogida
                    opcionescogida2=""
                    if Nueve.get()==1:
                              opcionescogida2+="9:00 AM "
                    if Diez.get()==1:
                              opcionescogida2+="10:00 AM "
                    if Once.get()==1:
                              opcionescogida2+="11:00 AM "
                    ConexionDB.Cone.cursor.execute("INSERT INTO horario_disponible_eq (ID_Horario, Dias_Disponibles, Horas_Disponibles) VALUES (NULL,'" + opcionescogida+
                    "','" + opcionescogida2 +"')")
                    ConexionDB.Cone.connec.commit()
                    #ConexionDB.Cone.connec.close()




#mensaje=Label(FrameCampos)#Label para mostrar lo que el usuario ha seleccionado
#mensaje.grid(row=5,column=0)

# ###Crear listas desplegables 
# Lista_desplegable=ttk.Combobox(FrameCampos, width=17)
# Lista_desplegable.grid(row=6, column=0)
# opciones=["Opcion 1", "Opcion 2", "Opcion 3"]
# Lista_desplegable['values']=opciones










clase=Equipos()
#clase.Crear_Table()

raiz.mainloop()
#conexion.close()


