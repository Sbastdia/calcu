# Cargamos el módulo unittest
import unittest
from src.calculadora import Calculator

# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
# Creamos una prueba para probar un valor inicial
    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        # Ejecutamos el método
        self.calc.add(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    #Creamos un nuevo test para comprobar una resta
    def test_rest_method(self):
        # Ejecutamos el método
        self.calc.rest(5, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    #Creamos un nuevo test para comprobar un producto
    def test_prod_method(self):
        # Ejecutamos el método
        self.calc.prod(5, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(15, self.calc.value)

    #Creamos un nuevo test para comprobar una división
    def test_div_method(self):
        # Ejecutamos el método
        self.calc.div(4, 2)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    #Creamos un nuevo test para comprobar un factorial
    def test_fact_method(self):
        # Ejecutamos el método
        self.calc.fact(3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(6, self.calc.value)

    #Creamos un nuevo test para comprobar un factorial de 0
    def test_fact0_method(self):
        # Ejecutamos el método
        self.calc.fact(0)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(1, self.calc.value)

    #Creamos un nuevo test para comprobar un factorial de un número negativo
    def test_factNeg_method(self):
        # Ejecutamos el método
        self.calc.fact(-1)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual("No se puede hacer el factorial de un número negativo", self.calc.value)