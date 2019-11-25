import unittest
from unittest.mock import patch
import baraja


def eligeCartaFija(i, longitud):
    if i == longitud - 1:
        return 0
    else:
        return i + 1


class BarajaTest(unittest.TestCase):

    def testCrearBaraja(self):
        b = baraja.crearBaraja()
        self.assertEqual(len(b), 40)
        self.assertEqual(b, ['As de Oro', '2 de Oro', '3 de Oro', '4 de Oro', '5 de Oro', '6 de Oro', '7 de Oro', 'Sota de Oro', 'Caballo de Oro', 'Rey de Oro', 'As de Copa', '2 de Copa', '3 de Copa', '4 de Copa', '5 de Copa', '6 de Copa', '7 de Copa', 'Sota de Copa', 'Caballo de Copa', 'Rey de Copa', 'As de Espada',
                             '2 de Espada', '3 de Espada', '4 de Espada', '5 de Espada', '6 de Espada', '7 de Espada', 'Sota de Espada', 'Caballo de Espada', 'Rey de Espada', 'As de Basto', '2 de Basto', '3 de Basto', '4 de Basto', '5 de Basto', '6 de Basto', '7 de Basto', 'Sota de Basto', 'Caballo de Basto', 'Rey de Basto'])

        self.assertEqual(b[0], 'As de Oro')
        self.assertEqual(b[39], 'Rey de Basto')
        self.assertEqual(b[10], 'As de Copa')
        self.assertEqual(b[20], 'As de Espada')

    @patch('baraja.eligeCarta', eligeCartaFija)
    def testBarajar(self):
        b = ['A', 'B', 'C', 'D', 'E']
        barajada = ['A', 'C', 'D', 'E', 'B']

        self.assertEqual(baraja.barajar(b), barajada)


if __name__ == '__main__':
    unittest.main()
