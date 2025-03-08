import unittest
import Actividad7_1_numeritos

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        
        self.assertEqual('foo'.upper(), 'FOO')

class TestRacionales(unittest.TestCase):
    def test_print_hello(self):
        m = 0
        racionales = Actividad7_1_numeritos(m)
        self.assertEqual(racionales.print_hello(), "Hello Diego D")

if __name__ == '__main__':
    unittest.main()