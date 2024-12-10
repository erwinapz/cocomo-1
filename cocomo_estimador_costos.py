import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        entrada = float(entry_entrada.get())
        salida = float(entry_salida.get())
        costo = float(entry_costo.get())
        valor_rango = float(entry_valor_rango.get())
        modo_desarrollo = modo_desarrollo_var.get()

        if modo_desarrollo == "organico":
            a, b, c, d, min_rango, max_rango = 3.2, 1.05, 2.5, 0.38, 51, 80
        elif modo_desarrollo == "semiAcoplado":
            a, b, c, d, min_rango, max_rango = 3.0, 1.12, 2.5, 0.35, 81, 100
        elif modo_desarrollo == "acoplado":
            a, b, c, d, min_rango, max_rango = 2.8, 1.20, 2.5, 0.32, 101, 150
        else:
            messagebox.showerror("Error", "Modo de desarrollo no válido.")
            return

        if valor_rango < min_rango or valor_rango > max_rango:
            messagebox.showerror("Error", f"Valor rango fuera del rango permitido para {modo_desarrollo}.")
            return

        LDC = (entrada + salida) * valor_rango
        MLDC = LDC / 1000
        E = a * (MLDC ** b)
        TD = c * (E ** d)
        P = LDC / E
        PN = E / TD
        COSTO = costo * E
        COSTO_LDC = COSTO / LDC

        resultado = [
            ['Líneas de código', LDC],
            ['Miles de líneas de código', MLDC],
            ['Esfuerzo', E],
            ['Tiempo de desarrollo', TD],
            ['Productividad', P],
            ['Personal necesario', PN],
            ['Costo total', COSTO],
            ['Costo por línea de código', COSTO_LDC]
        ]

        mostrar_resultados(resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese todos los valores correctamente.")

def mostrar_resultados(resultado):
    result_window = tk.Toplevel(ventana)
    result_window.title("Resultados")

    for i, (nombre, valor) in enumerate(resultado):
        tk.Label(result_window, text=f"{nombre}: {valor:.2f}").pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Estimación de Costos de Software")
ventana.geometry("600x500")  # Aumentar el tamaño de la ventana

# Etiquetas y campos de entrada
tk.Label(ventana, text="Entrada").pack(pady=5)
entry_entrada = tk.Entry(ventana)
entry_entrada.pack(pady=5)

tk.Label(ventana, text="Salida").pack(pady=5)
entry_salida = tk.Entry(ventana)
entry_salida.pack(pady=5)

tk.Label(ventana, text="Costo Honorario").pack(pady=5)
entry_costo = tk.Entry(ventana)
entry_costo.pack(pady=5)

tk.Label(ventana, text="Modo de Desarrollo").pack(pady=5)
modo_desarrollo_var = tk.StringVar(value="organico")
tk.OptionMenu(ventana, modo_desarrollo_var, "organico", "semiAcoplado", "acoplado").pack(pady=5)

tk.Label(ventana, text="Valor Rango").pack(pady=5)
entry_valor_rango = tk.Entry(ventana)
entry_valor_rango.pack(pady=5)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
