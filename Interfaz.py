import tkinter as tk
from tkinter import messagebox
from CurpGenerator import generar_curp
from datetime import datetime

def actualizar_dias(*args):
    mes = int(var_mes.get())
    anio = int(var_anio.get())
    
    if mes in [4, 6, 9, 11]:
        dias_del_mes = 30
    elif mes == 2:
        dias_del_mes = 29 if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0) else 28
    else:
        dias_del_mes = 31
    
    menu_dia['menu'].delete(0, 'end')
    for dia in range(1, dias_del_mes + 1):
        menu_dia['menu'].add_command(label=dia, command=lambda d=dia: var_dia.set(d))
    var_dia.set(1)

def generar_curp_gui():
    try:
        nombre = entry_nombre.get().strip().upper()
        apellido_paterno = entry_apellido_paterno.get().strip().upper()
        apellido_materno = entry_apellido_materno.get().strip().upper()
        anio = int(var_anio.get())
        mes = str(var_mes.get()).zfill(2)
        dia = str(var_dia.get()).zfill(2)
        sexo = var_sexo.get()
        estado = entry_estado.get().strip().upper()

        curp = generar_curp(nombre, apellido_paterno, apellido_materno, anio, mes, dia, sexo, estado)
        curp_label.config(text=f"CURP Generada: {curp}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Formulario de Generación de CURP - CURPGenrator")
root.geometry("400x400")
root.configure(bg="white")

form_frame = tk.Frame(root, padx=20, pady=20, bg="white")
form_frame.pack(pady=20)

# Estilos del formulario
tk.Label(form_frame, text="Generador de CURP", font=("Arial", 14, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(form_frame, text="Nombre:", bg="white", anchor="w").grid(row=1, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(form_frame, width=25)
entry_nombre.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Apellido Paterno:", bg="white", anchor="w").grid(row=2, column=0, sticky="w", pady=5)
entry_apellido_paterno = tk.Entry(form_frame, width=25)
entry_apellido_paterno.grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Apellido Materno:", bg="white", anchor="w").grid(row=3, column=0, sticky="w", pady=5)
entry_apellido_materno = tk.Entry(form_frame, width=25)
entry_apellido_materno.grid(row=3, column=1, pady=5)

tk.Label(form_frame, text="Año de Nacimiento:", bg="white", anchor="w").grid(row=4, column=0, sticky="w", pady=5)
anios = [str(anio) for anio in range(1924, datetime.now().year + 1)]
var_anio = tk.StringVar(root)
var_anio.set(anios[-1])
menu_anio = tk.OptionMenu(form_frame, var_anio, *anios, command=actualizar_dias)
menu_anio.grid(row=4, column=1, pady=5)

tk.Label(form_frame, text="Mes de Nacimiento:", bg="white", anchor="w").grid(row=5, column=0, sticky="w", pady=5)
meses = list(range(1, 13))
var_mes = tk.IntVar(root)
var_mes.set(1)
menu_mes = tk.OptionMenu(form_frame, var_mes, *meses, command=actualizar_dias)
menu_mes.grid(row=5, column=1, pady=5)

tk.Label(form_frame, text="Día de Nacimiento:", bg="white", anchor="w").grid(row=6, column=0, sticky="w", pady=5)
var_dia = tk.IntVar(root)
var_dia.set(1)
menu_dia = tk.OptionMenu(form_frame, var_dia, *range(1, 32))
menu_dia.grid(row=6, column=1, pady=5)

tk.Label(form_frame, text="Sexo (H/M):", bg="white", anchor="w").grid(row=7, column=0, sticky="w", pady=5)
var_sexo = tk.StringVar(root)
var_sexo.set("H")
menu_sexo = tk.OptionMenu(form_frame, var_sexo, "H", "M")
menu_sexo.grid(row=7, column=1, pady=5)

tk.Label(form_frame, text="Estado:", bg="white", anchor="w").grid(row=8, column=0, sticky="w", pady=5)
entry_estado = tk.Entry(form_frame, width=25)
entry_estado.grid(row=8, column=1, pady=5)

generate_button = tk.Button(form_frame, text="Generar CURP", command=generar_curp_gui, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="flat")
generate_button.grid(row=9, column=0, columnspan=2, pady=10)

curp_label = tk.Label(form_frame, text="CURP Generada: ", font=("Arial", 10, "italic"), bg="white", fg="blue")
curp_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()