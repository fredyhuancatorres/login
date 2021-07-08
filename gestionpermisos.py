
import tkinter
from tkinter import ttk
from easygui import *
from tkinter import *
import tkinter.messagebox as tk
import sqlite3

from tkinter import messagebox



conn = sqlite3.connect('basededatos.db')
cur = conn.cursor()
conn.execute("CREATE TABLE balance(empleado_i text, licencia_enfermedad int, licencia_maternindad int, licencia_emergencia int)")
conn.execute("CREATE TABLE empleado (registro_id text, empleado_id text, nombre text, numero_telefono text, email text, direccion, password)")


class AdminClass():

    def AdminLogin(self):
        mensaje = "Ingrese un usuario y contraseña"
        titulo = "Inicio"
        campodelogin = ["Usuario", "Password"]
        campo = []
        campo = multpasswordbox(mensaje, titulo, campodelogin)
        if campo[0] == 'admin' and campo[1] == 'admin':
            messagebox.showinfo("Login", "satisfactorio")
            self.adminwindow()
        else:
            messagebox.showerror("información erronea", "usuario o password incorrecto")

    def adminwindow(self):
        adminmainwindow = Toplevel()
        adminmainwindow.wm_attributes('-fullscreen', '1')
        informacionEmpleado = Button(adminmainwindow, text = 'toda la información', command = self.todaInformacionWindow, bd=12, relief=GROOVE, fg="black", bg="yellow",font=("Calibri", 36, "bold"), activebackground = "yellow")
        informacionEmpleado.pack(fill=X)
        LeaveListButton = Button(adminmainwindow, text = 'Leave approval list', command = "", bd=12, relief=GROOVE, fg="black", bg="yellow",font=("Calibri", 36, "bold"), activebackground = "yellow")
        LeaveListButton.pack(fill=X)
        ApprovalButton = Button(adminmainwindow, text = 'Approve leave', command = "", bd=12, relief=GROOVE, fg="black", bg="yellow",font=("Calibri", 36, "bold"), activebackground = "yellow")
        ApprovalButton.pack(fill=X)

        LogoutBtn = Button(adminmainwindow, text = 'Logout', command = adminmainwindow.destroy, bd=12, relief=GROOVE, fg="red",bg="yellow",font=("Calibri", 36, "bold"), activebackground = "yellow")
        LogoutBtn.pack(fill=X) 

    def todaInformacionWindow(self):
        todaInformacionEmpleado = Toplevel()
        todaInformacionEmpleado.resizable(0, 0)

        appLabel = Label(todaInformacionEmpleado, text="All Employee Information", fg="#06a099", width=40)
        appLabel.config(font=("Sylfaen", 30))
        appLabel.pack()
        
        tree = ttk.Treeview(todaInformacionEmpleado)
        tree.pack(side = 'left')
        
        verscrlbar = ttk.Scrollbar(todaInformacionEmpleado, command = tree.yview)  
        verscrlbar.pack(side ='left', fill = "y") 
    
        tree.configure(yscrollcommand = verscrlbar.set) 

        tree["columns"] = ('one', 'two', 'three', 'four', 'five', 'six')
        tree['show'] = 'headings'

        tree.column("one", anchor = 'c', minwidth = 0, width = 150)
        tree.column("two", anchor = 'c', minwidth = 0, width = 150)
        tree.column("three", anchor = 'c', minwidth = 0, width = 150)
        tree.column("four", anchor = 'c', minwidth = 0, width = 200)
        tree.column("five", anchor = 'c', minwidth = 0, width = 150)
        tree.column("six", anchor = 'c', minwidth = 0, width = 400)

        tree.heading("one", text = "ID Empleado")
        tree.heading("two", text = "Nombre")
        tree.heading("three", text = "Nro. Telefonico")
        tree.heading("four", text = "E-mail")
        tree.heading("six", text = "Direccion")
        
        cursor = conn.execute('SELECT .... FROM empleado')
        i = 1

        for row in cursor:
            tree.insert('', 'end', values = (row[0], row[1], row[2], row[3], row[4], row[5]))
            i = i + 1


if __name__ == "__main__":
    adminwindow()
