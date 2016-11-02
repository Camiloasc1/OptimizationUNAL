import unittest
from Workshop6.EdmondsKarp import *
from Workshop6.Graph import *


class MyTestCase(unittest.TestCase):
    def test_edmonds_karp_1(self):
        C = {}
        makeDLinkW(C, 'a', 'b', 1000)
        makeDLinkW(C, 'a', 'c', 1000)
        makeDLinkW(C, 'b', 'c', 1)
        makeDLinkW(C, 'b', 'd', 1000)
        makeDLinkW(C, 'c', 'd', 1000)
        max_flow, F = EdmondsKarp(C, 'a', 'd')
        # print(max_flow, F)
        self.assertEqual(2000, max_flow)
        self.assertEqual({'a': {'c': 1000, 'b': 1000}, 'c': {'a': -1000, 'd': 1000}, 'b': {'a': -1000, 'd': 1000},
                          'd': {'c': -1000, 'b': -1000}}, F)

    def test_edmonds_karp_2(self):
        C = {}
        makeDLinkW(C, 'a', 'b', 3)
        makeDLinkW(C, 'a', 'd', 3)
        makeDLinkW(C, 'b', 'c', 4)
        makeDLinkW(C, 'c', 'a', 3)
        makeDLinkW(C, 'c', 'd', 1)
        makeDLinkW(C, 'c', 'e', 2)
        makeDLinkW(C, 'd', 'e', 2)
        makeDLinkW(C, 'd', 'f', 6)
        makeDLinkW(C, 'e', 'g', 1)
        makeDLinkW(C, 'e', 'b', 1)
        makeDLinkW(C, 'f', 'g', 9)
        max_flow, F = EdmondsKarp(C, 'a', 'g')
        # print(max_flow, F)
        self.assertEqual(5, max_flow)
        self.assertEqual(
            {'e': {'g': 1, 'c': -1}, 'b': {'c': 2, 'a': -2}, 'g': {'e': -1, 'f': -4}, 'f': {'g': 4, 'd': -4},
             'c': {'b': -2, 'e': 1, 'd': 1}, 'a': {'b': 2, 'd': 3}, 'd': {'f': 4, 'c': -1, 'a': -3}}, F)

    def test_edmonds_karp_time(self):
        # C = {}
        # makeDLinkW(C, 'a', 'b', 3)
        # makeDLinkW(C, 'a', 'd', 3)
        # makeDLinkW(C, 'b', 'c', 4)
        # makeDLinkW(C, 'c', 'a', 3)
        # makeDLinkW(C, 'c', 'd', 1)
        # makeDLinkW(C, 'c', 'e', 2)
        # makeDLinkW(C, 'd', 'e', 2)
        # makeDLinkW(C, 'd', 'f', 6)
        # makeDLinkW(C, 'e', 'g', 1)
        # makeDLinkW(C, 'e', 'b', 1)
        # makeDLinkW(C, 'f', 'g', 9)
        # import timeit
        # print(timeit.timeit("EdmondsKarp(C, 'a', 'g')", globals={'C': C, 'EdmondsKarp': EdmondsKarp}, number=100000))
        # print(timeit.timeit("EdmondsKarp(C, 'a', 'g')", globals={'C': C, 'EdmondsKarp': EdmondsKarp_2}, number=100000))
        pass


if __name__ == '__main__':
    unittest.main()
