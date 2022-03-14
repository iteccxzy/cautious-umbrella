import unittest
from problemas.integersums import add_it_up


class TestBuilFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('inicio')

    def test_primo02(self):
        r = add_it_up(8)
        self.assertEqual(36, r)


if __name__ == '__main__':
    unittest.main()
