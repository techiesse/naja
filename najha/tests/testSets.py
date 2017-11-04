import unittest

import najha.sets as sets

class TestSets(unittest.TestCase):

    def test_union(self):
        a = [1, 2, 3]
        b = [2, 3, 4]
        self.assertEqual(sorted(sets.union(a, b)), [1,2,3,4])
        self.assertEqual(sets.union([1,2,3], []), [1,2,3])
        self.assertEqual(sets.union([], [1,2,3]), [1,2,3])


    def test_intersection(self):
        self.assertEqual(sorted(sets.intersection([1,2,3], [2,3,4])), [2,3])
        self.assertEqual(sets.intersection([1,2,3], []), [])
        self.assertEqual(sets.intersection([], [1,2,3]), [])


    def test_sub(self):
        self.assertEqual(sorted(sets.sub([1,2,3], [2,3,4])), [1])
        self.assertEqual(sorted(sets.sub([0,2,3,4], [1,2,3])), [0,4])
        self.assertEqual(sets.sub([1,2,3], []), [1,2,3])
        self.assertEqual(sets.sub([], [1,2,3]), [])


if __name__ == '__main__':
    unittest.main()
