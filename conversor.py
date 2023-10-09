import math

class NumeroALetras:
    def __init__(self):
        self.UNIDADES = ('', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve')
        self.DECENAS = ('Diez', 'Once', 'Doce', 'Trece', 'Catorce', 'Quince', 'Dieciséis', 'Diecisiete', 'Dieciocho', 'Diecinueve', 'Veinte')
        self.DECENAS_Y = ('', '', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta', 'Setenta', 'Ochenta', 'Noventa')
        self.CENTENAS = ('', 'Ciento', 'Doscientos', 'Trescientos', 'Cuatrocientos', 'Quinientos', 'Seiscientos', 'Setecientos', 'Ochocientos', 'Novecientos')

    def convertir(self, n):
        output = ''
        es_negativo = False
        if n < 0:
            es_negativo = True
            n = abs(n)

        entero = int(n)
        decimal = int((n - entero) * 100)

        if entero == 0:
            output = 'Cero'
        elif entero < 10:
            output = self.UNIDADES[entero]
        elif entero < 30:
            output = self.DECENAS[entero-10]
        elif entero < 100:
            if entero%10 == 0:
                output = self.DECENAS_Y[entero//10]
            else:
                output = self.DECENAS_Y[entero//10] + ' y ' + self.UNIDADES[entero%10]
        elif entero < 1000:
            output = self.CENTENAS[entero//100] + ('' if entero%100 == 0 else ' ' + self.convertir(entero%100))
        elif entero < 1000000:  # hasta 999,999
            if entero < 2000:
                output = 'Mil ' + self.convertir(entero%1000)
            else:
                output = self.convertir(entero//1000) + ' Mil ' + ('' if entero%1000 == 0 else ' ' + self.convertir(entero%1000))
        elif entero < 1000000000:  # hasta 999,999,999
            output = self.convertir(entero//1000000) + ' Millones ' + ('' if entero%1000000 == 0 else ' ' + self.convertir(entero%1000000))
        elif entero < 1000000000000:  # hasta 999,999,999,999
            output = self.convertir(entero//1000000000) + ' Billones ' + ('' if entero%1000000000 == 0 else ' ' + self.convertir(entero%1000000000))
        elif entero < 1000000000000000:  # hasta 999,999,999,999,999
            output = self.convertir(entero//1000000000000) + ' Trillones ' + ('' if entero%1000000000000 == 0 else ' ' + self.convertir(entero%1000000000000))
        else:
            output = "Número fuera de rango"

        if decimal > 0:
            output += ' punto ' + self.convertir(decimal)

        if es_negativo:
            output = "Menos " + output
        return output

class Operaciones:
    def __init__(self):
        self.convertidor = NumeroALetras()

    def suma(self, a, b):
        if a is None or b is None:
            return "Math error"
        resultado = a + b
        return self.convertidor.convertir(resultado)

    def resta(self, a, b):
        if a is None or b is None:
            return "Math error"
        resultado = a - b
        return self.convertidor.convertir(resultado)

    def multiplicacion(self, a, b):
        if a is None or b is None:
            return "Math error"
        resultado = a * b
        return self.convertidor.convertir(resultado)

    def division(self, a, b):
        if a is None or b is None or b == 0:
            return "Math error"
        resultado = a / b
        return self.convertidor.convertir(resultado)

    def seno(self, a):
        if a is None or a < -90 or a > 90:
            return "Math error"
        resultado = math.sin(math.radians(a))
        return self.convertidor.convertir(resultado)

    def coseno(self, a):
        if a is None:
            return "Math error"
        resultado = math.cos(math.radians(a))
        return self.convertidor.convertir(resultado)

    def tangente(self, a):
        if a is None or a == 90 or a == -90:
            return "Math error"
        resultado = math.tan(math.radians(a))
        return self.convertidor.convertir(resultado)

    def media(self, *args):
        try:
            # Convertimos los valores separados por comas a una lista de números
            valores = [float(val) for val in args if val.strip()]
            resultado = sum(valores) / len(valores)
            return self.convertidor.convertir(resultado)
        except:
            return "Math error"

    def maximo(self, *args):
        try:
            valores = [float(val) for val in args if val.strip()]
            resultado = max(valores)
            return self.convertidor.convertir(resultado)
        except:
            return "Math error"

    def minimo(self, *args):
        try:
            valores = [float(val) for val in args if val.strip()]
            resultado = min(valores)
            return self.convertidor.convertir(resultado)
        except:
            return "Math error"