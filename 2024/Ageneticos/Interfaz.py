#encoding:UTF-8
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuración de Parámetros")

        # Variables
        self.var_rango_articulos = tk.IntVar() #es entero
        self.var_cantidad_depositos = tk.DoubleVar()
        self.var_stock_seguridad = tk.DoubleVar()
        self.var_calefaccion = tk.DoubleVar()
        self.var_seguros = tk.DoubleVar()
        self.var_volumen_unitario = tk.IntVar()
        self.var_emision_orden = tk.DoubleVar()
        self.var_recepcion_lote = tk.DoubleVar()
        self.var_lead_time = tk.IntVar()
        self.var_demanda_mensual = tk.IntVar()
        self.var_interes_mensual = tk.DoubleVar()
        self.var_tamano_poblacion = tk.IntVar()
        self.var_nro_generaciones = tk.IntVar()

        # Datos de rango de costos
        self.rangos = []

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Campos
        tk.Label(self.root, text="Rango de Artículos").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_rango_articulos).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Cantidad de Depósitos").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_cantidad_depositos).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Stock de Seguridad").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_stock_seguridad).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Calefacción").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_calefaccion).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Seguros").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_seguros).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Volumen Unitario").grid(row=5, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_volumen_unitario).grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Emisión de la Orden").grid(row=6, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_emision_orden).grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Recepción del Lote").grid(row=7, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_recepcion_lote).grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Lead Time").grid(row=8, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_lead_time).grid(row=8, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Demanda Mensual").grid(row=9, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_demanda_mensual).grid(row=9, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Interés Mensual").grid(row=10, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_interes_mensual).grid(row=10, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Tamaño de la Población").grid(row=11, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_tamano_poblacion).grid(row=11, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Número de Generaciones").grid(row=12, column=0, padx=10, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.var_nro_generaciones).grid(row=12, column=1, padx=10, pady=5)

        # Botones
        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=13, column=0, columnspan=2, pady=10)

        tk.Button(self.root, text="Agregar Rango", command=self.agregar_rango).grid(row=14, column=0, columnspan=2,
                                                                                    pady=10)

        self.btn_inicio = tk.Button(self.root, text="Inicio", state='disabled', command=self.iniciar_algoritmo)
        self.btn_inicio.grid(row=15, column=0, padx=10, pady=10)

        self.btn_informar_evolucion = tk.Button(self.root, text="Informar Evolución", state='disabled',
                                                command=self.informar_evolucion)
        self.btn_informar_evolucion.grid(row=15, column=1, padx=10, pady=10)

        # Grilla de Rango de Costos
        self.tree = ttk.Treeview(self.root, columns=('UDesde', 'UHasta', 'CostoUnitario', 'CostoAlquiler', 'Deposito'),
                                 show='headings')
        self.tree.heading('UDesde', text='U. Desde')
        self.tree.heading('UHasta', text='U. Hasta')
        self.tree.heading('CostoUnitario', text='C. Unitario')
        self.tree.heading('CostoAlquiler', text='C. Alquiler')
        self.tree.heading('Deposito', text='Deposito')
        self.tree.grid(row=16, column=0, columnspan=2, padx=10, pady=10)

    def calcular(self):
        try:
            rango_articulos = self.var_rango_articulos.get()
            cantidad_depositos = self.var_cantidad_depositos.get()
            stock_seguridad = self.var_stock_seguridad.get()
            calefaccion = self.var_calefaccion.get()
            seguros = self.var_seguros.get()
            volumen_unitario = self.var_volumen_unitario.get()
            emision_orden = self.var_emision_orden.get()
            recepcion_lote = self.var_recepcion_lote.get()
            lead_time = self.var_lead_time.get()
            demanda_mensual = self.var_demanda_mensual.get()
            interes_mensual = self.var_interes_mensual.get()
            tamano_poblacion = self.var_tamano_poblacion.get()
            nro_generaciones = self.var_nro_generaciones.get()

            # Calculo de costos
            costo_preparacion = Calculo.calculo_preliminar_costos(emision_orden, recepcion_lote)
            costo_almacenamiento = Calculo.costo_almacenamiento(rango_articulos, seguros, calefaccion, interes_mensual,
                                                                volumen_unitario, costo_preparacion, calefaccion)
            costo_total = Calculo.calculoctc(costo_preparacion, demanda_mensual, costo_almacenamiento,
                                             costo_preparacion, rango_articulos)

            messagebox.showinfo("Resultado", f"Costo Total: {costo_total:.2f}")

        except Exception as e:
            messagebox.showerror("Error", f"Error en los cálculos: {e}")

    def agregar_rango(self):
        u_desde = simpledialog.askinteger("Entrada", "Ingrese U. Desde:")
        u_hasta = simpledialog.askinteger("Entrada", "Ingrese U. Hasta:")
        costo_unitario = simpledialog.askfloat("Entrada", "Ingrese C. Unitario:")
        costo_alquiler = simpledialog.askfloat("Entrada", "Ingrese C. Alquiler:")
        deposito = simpledialog.askstring("Entrada", "Ingrese Depósito:")

        if u_desde is not None and u_hasta is not None and costo_unitario is not None and costo_alquiler is not None and deposito is not None:
            self.tree.insert('', 'end', values=(u_desde, u_hasta, costo_unitario, costo_alquiler, deposito))

    def iniciar_algoritmo(self):
        # Lógica para iniciar el algoritmo genético
        messagebox.showinfo("Inicio", "Iniciando el algoritmo genético...")

        # Aquí se debería llamar al método correspondiente del algoritmo genético
        # agen = Agenetico()
        # agen.generacion_poblacion(...)
        # ...

    def informar_evolucion(self):
        # Lógica para informar la evolución
        messagebox.showinfo("Evolución", "Informando evolución...")

        # Aquí se debería mostrar los detalles de la evolución del algoritmo
        # ...


if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
