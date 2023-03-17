import tkinter as tk

root = tk.Tk()
root.title("LPBB Simulator")

puntos_equipo1 = 0
puntos_equipo2 = 0

perdiodo = 0

def actualizar_puntos_equipo1(puntos):
    global puntos_equipo1
    puntos_equipo1 += puntos
    lbl_puntos_equipo1.config(text=str(puntos_equipo1))

def actualizar_puntos_equipo2(puntos):
    global puntos_equipo2
    puntos_equipo2 += puntos
    lbl_puntos_equipo2.config(text=str(puntos_equipo2))

def actualizar_periodo(perdiodo2):
    global perdiodo
    perdiodo += perdiodo2
    lbl_periodo.config(text=str(perdiodo))


lbl_periodo = tk.Label(root, text="Periodo: ", font=("Arial", 20))
lbl_periodo.grid(row=0, column=0, padx=10, pady=10)

btn_periodom = tk.Button(root, text="<", font=("Arial", 20), command=lambda: actualizar_periodo(-1))
btn_periodom.grid(row=0, column=1, padx=10, pady=10)

lbl_periodo = tk.Label(root, text="0", font=("Arial", 30))
lbl_periodo.grid(row=0, column=2, padx=10, pady=10)

btn_periodo = tk.Button(root, text=">", font=("Arial", 20), command=lambda: actualizar_periodo(1))
btn_periodo.grid(row=0, column=3, padx=10, pady=10)


lbl_equipo1 = tk.Label(root, text="Equipo 1", font=("Arial", 20))
lbl_equipo1.grid(row=1, column=0, padx=10, pady=10)

lbl_equipo2 = tk.Label(root, text="Equipo 2", font=("Arial", 20))
lbl_equipo2.grid(row=1, column=2, padx=10, pady=10)


btn_punto1 = tk.Button(root, text="+1", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(1))
btn_punto1.grid(row=3, column=0, padx=10, pady=10)

btn_puntom1 = tk.Button(root, text="-1", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(-1))
btn_puntom1.grid(row=3, column=1, padx=10, pady=10)



btn_punto2 = tk.Button(root, text="+2", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(2))
btn_punto2.grid(row=4, column=0, padx=10, pady=10)

btn_puntom2 = tk.Button(root, text="-2", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(-2))
btn_puntom2.grid(row=4, column=1, padx=10, pady=10)



btn_punto3 = tk.Button(root, text="+3", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(3))
btn_punto3.grid(row=5, column=0, padx=10, pady=10)

btn_puntom3 = tk.Button(root, text="-3", font=("Arial", 20), command=lambda: actualizar_puntos_equipo1(-3))
btn_puntom3.grid(row=5, column=1, padx=10, pady=10)



btn_punto1_equipo2 = tk.Button(root, text="+1", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(1))
btn_punto1_equipo2.grid(row=3, column=2, padx=10, pady=10)

btn_puntom1_equipo2 = tk.Button(root, text="-1", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(-1))
btn_puntom1_equipo2.grid(row=3, column=3, padx=10, pady=10)


btn_punto2_equipo2 = tk.Button(root, text="+2", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(2))
btn_punto2_equipo2.grid(row=4, column=2, padx=10, pady=10)
btn_puntom2_equipo2 = tk.Button(root, text="-2", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(-2))
btn_puntom2_equipo2.grid(row=4, column=3, padx=10, pady=10)

btn_punto3_equipo2 = tk.Button(root, text="+3", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(3))
btn_punto3_equipo2.grid(row=5, column=2, padx=10, pady=10)
btn_puntom3_equipo2 = tk.Button(root, text="-3", font=("Arial", 20), command=lambda: actualizar_puntos_equipo2(-3))
btn_puntom3_equipo2.grid(row=5, column=3, padx=10, pady=10)

lbl_puntos_equipo1 = tk.Label(root, text="0", font=("Arial", 30))
lbl_puntos_equipo1.grid(row=2, column=1, padx=10, pady=10)

lbl_puntos_equipo2 = tk.Label(root, text="0", font=("Arial", 30))
lbl_puntos_equipo2.grid(row=2, column=3, padx=10, pady=10)


root.mainloop()
