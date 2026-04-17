import unittest
from main import recommend_movies, recommend_by_cluster, evaluate_recommendation

class TestRecommenderSystem(unittest.TestCase):
    def test_recommend_movies(self):
        result = recommend_movies(1)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    def test_recommend_by_cluster(self):
        result = recommend_by_cluster(1)
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    def test_evaluate_recommendation(self):
        score = evaluate_recommendation(1)
        self.assertIsInstance(score, (int, float))

if __name__ == "__main__":
    unittest.main()
