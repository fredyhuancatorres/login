
from tkinter import ttk
from tkinter import *
import tkinter.messagebox  as tk
import sqlite3

conn = sqlite3.connect('basededatos.db')
cur = conn.cursor()

#conn.execute("CREATE TABLE balance(empleado_i text, licencia_enfermedad int, licencia_maternindad int, licencia_emergencia int)")
