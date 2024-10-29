#encoding:UTF-8

import tkinter as tk

def guardar_datos():
    print("Datos guardados")

def cancelar_operacion():
    print("Operación cancelada")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Ejemplo")

# Crear botones
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
boton_guardar.pack(pady=10)

boton_cancelar = tk.Button(ventana, text="Cancelar", command=cancelar_operacion)
boton_cancelar.pack(pady=10)

# Ejecutar la interfaz
ventana.mainloop()
