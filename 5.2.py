import fracs

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 3]), [1,6])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac(f1,f4), [-3,2])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac(f1,f4), [-1, 6])

    def test_is_positive(self):
        self.assertFalse(fracs.is_positive(f1))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero(f2))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac(f1,f3), -1)
 
    def test_frac2float(self):
        self.assertEqual(fracs.frac2float(f1), -0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
