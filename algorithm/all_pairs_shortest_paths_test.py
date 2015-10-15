from all_pairs_shortest_paths import extend_shortest_paths, slow_all_pairs_shortest_paths, faster_all_pairs_shortest_paths
import unittest
import numpy as np

class TestAllPairsShortestPaths(unittest.TestCase):
    def test_slow_all_pairs_shortest_paths(self):
        W = np.array([[0, 3, 8, float("Inf"), -4], [float("Inf"), 0, float("Inf"), 1, 7], [float("Inf"), 4, 0, float("Inf"), float("Inf")], [2, float("Inf"), -5, 0, float("Inf")], [float("Inf"), float("Inf"), float("Inf"), 6, 0]])
        R = slow_all_pairs_shortest_paths(W)
        L = np.array([[0, 1, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 3], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]])
        self.assertEquals((R == L).all(), True)
#        W = np.array([[0, float("Inf"), float("Inf"), float("Inf"), -1, float("Inf")], [1, 0, float("Inf"), 2, float("Inf"), float("Inf")], [float("Inf"), 2, 0, float("Inf"), float("Inf"), -8], [-4, float("Inf"), float("Inf"), 0, 3, float("Inf")], [float("Inf"), 7, float("Inf"), float("Inf"), 0, float("Inf")], [float("Inf"), 5, 10, float("Inf"), float("Inf"), 0]]) 
#        R = slow_all_pairs_shortest_paths(W)
#        L = np.array([[0, 1, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 3], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]])
#        self.assertEquals((R == L).all(), True)
    def test_faster_all_pairs_shortest_paths(self):
        W = np.array([[0, 3, 8, float("Inf"), -4], [float("Inf"), 0, float("Inf"), 1, 7], [float("Inf"), 4, 0, float("Inf"), float("Inf")], [2, float("Inf"), -5, 0, float("Inf")], [float("Inf"), float("Inf"), float("Inf"), 6, 0]])
        R = faster_all_pairs_shortest_paths(W)
        L = np.array([[0, 1, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 3], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]])
        self.assertEquals((R == L).all(), True)
