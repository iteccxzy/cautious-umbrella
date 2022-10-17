import imp
import unittest

from problemas import facto, primo


class TestBuilFunc(unittest.TestCase):
    
    # @classmethod
    # def setUpClass(cls):
    #     print('inicio')

    # @classmethod
    # def tearDownClass(cls):
    #     print('fin')

    # def setUp(self) -> None:
    #     print('')

    # def tearDown(self) -> None:
    #     print('')

    def test_primo02(self):
        r = primo.isPrime(13)
        self.assertTrue(r)

    def test_factorial02(self):
        r = facto.facto(13)
        self.assertEqual(6227020800, r)


if __name__ == '__main__':
    unittest.main()
