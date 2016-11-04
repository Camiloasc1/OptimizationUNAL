import unittest
from Workshop6.Graph import makeNDLinkW
from Workshop6.Prim import Prim


class MyTestCase(unittest.TestCase):
    def test_prim_1(self):
        G = {}
        makeNDLinkW(G, 'a', 'b', 2)
        makeNDLinkW(G, 'a', 'd', 1)
        makeNDLinkW(G, 'b', 'd', 2)
        makeNDLinkW(G, 'c', 'd', 3)
        print(Prim(G))
        total_cost, F = Prim(G)
        self.assertEqual(6, total_cost)
        self.assertEqual(F, {'a': {'d': 1, 'b': 2}, 'd': {'a': 1, 'c': 3}, 'c': {'d': 3}, 'b': {'a': 2}})


if __name__ == '__main__':
    unittest.main()
