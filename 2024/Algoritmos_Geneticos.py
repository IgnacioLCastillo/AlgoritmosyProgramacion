#encoding:UTF-8

import random

class Agenetico:
    def __init__(self):
        self.generaciones = []
        self.proxima_generacion = []

    def generacion_poblacion(self, tope, tamano_poblacion):
        self.generaciones.clear()
        for _ in range(tamano_poblacion):
            valor = int(1 + tope * random.random())
            binario = self.dectobin(valor)
            binario = binario.zfill(11)
            self.generaciones.append({'idgen': 1, 'valor': valor, 'binario': binario})

    def funcion_adaptacion(self, promedio, cte):
        return promedio / cte

    def seleccion(self, idgen):
        for gen in self.generaciones:
            if gen['idgen'] == idgen:
                gen['apto'] = gen.get('fadap', 0) > 1

    def post_seleccion(self, idgen):
        pares = []
        candidatos = [gen for gen in self.generaciones if gen['idgen'] == idgen and gen.get('apto', False) and not gen.get('parcon', 0)]
        while candidatos:
            random.shuffle(candidatos)
            for i in range(0, len(candidatos) - 1, 2):
                pares.append((candidatos[i], candidatos[i + 1]))
                candidatos[i]['parcon'] = i + 1
                candidatos[i + 1]['parcon'] = i + 1

    def reproduccion(self, idgen):
        pares = [(gen['parcon'], gen) for gen in self.generaciones if gen['idgen'] == idgen and gen.get('apto', False)]
        for par in pares:
            papa = par[0]['binario']
            mama = par[1]['binario']
            nmonopunto = int(1 + 11 * random.random())
            hijo_a = papa[:nmonopunto] + mama[nmonopunto:]
            hijo_b = mama[:nmonopunto] + papa[nmonopunto:]
            valor_a = self.bintodec(hijo_a)
            valor_b = self.bintodec(hijo_b)
            self.generaciones.append({'idgen': idgen + 1, 'valor': valor_a, 'binario': hijo_a})
            self.generaciones.append({'idgen': idgen + 1, 'valor': valor_b, 'binario': hijo_b})

    def bintodec(self, cbinario):
        return int(cbinario, 2)

    def insertar_hijos(self, idgen):
        for gen in self.generaciones:
            if gen['idgen'] == idgen and gen.get('apto', False):
                self.proxima_generacion.append(gen)

    def mutacion(self, idgen):
        for gen in self.generaciones:
            if gen['idgen'] == idgen:
                binario = list(gen['binario'])
                for i in range(len(binario)):
                    if random.random() < 0.001:
                        binario[i] = '1' if binario[i] == '0' else '0'
                gen['binario'] = ''.join(binario)
                gen['valor'] = self.bintodec(gen['binario'])
                gen['muto'] = True


class Calculo:
    @staticmethod
    def calculocte(costo_uni, demanda, costo_almacenamiento, costo_preparacion, valor):
        return (costo_uni * demanda) + (0.5 * costo_almacenamiento * valor) + (costo_preparacion * demanda / valor)

    @staticmethod
    def calculo_preliminar_costos(emision, recepcion):
        return emision + recepcion

    @staticmethod
    def costo_almacenamiento(valor, seguro, calefaccion, interes, volumen, costo, alquiler):
        return seguro + (alquiler * volumen) + (calefaccion * volumen) + (costo * interes)
