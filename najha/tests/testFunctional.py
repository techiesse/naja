import unittest

import najha.functional as f

class TestFunctional(unittest.TestCase):

    def test_zipWith(self):
        self.assertEqual(f.zipWith(f.op.sum, [1,2,3], [10,20,30]), [11,22,33])
        self.assertEqual(f.zipWith(lambda a, b: a + b, ["a", "b"], ["c", "d"]), ["ac", "bd"])
        #self.assertNotEqual(f.zipWith(lambda a, b: a + b, ["a", "b"], ["c", "d"]), ["ac", "bd"])


#    def test_isupper(self):
#        self.assertTrue('FOO'.isupper())
#        self.assertFalse('Foo'.isupper())
#
#    def test_split(self):
#        s = 'hello world'
#        self.assertEqual(s.split(), ['hello', 'world'])
#        # check that s.split fails when the separator is not a string
#        with self.assertRaises(TypeError):
#            s.split(2)

if __name__ == '__main__':
    unittest.main()
