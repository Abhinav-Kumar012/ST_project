import unittest
from src import integration_2


class TestIntegration2(unittest.TestCase):
    def test_text_processing_pipeline(self):
        words = ["RaceCar", "Hello", "Level", "World", "Madam", "Python"]

        index, mean_len = integration_2.text_processing_pipeline(words, "Madam")

        self.assertEqual(index, 1)
        self.assertEqual(mean_len, 6.0)

    def test_v2(self):
        words = ["RaceCar", "Hello", "Level", "World", "Madam", "Python"]
        index, mean_len = integration_2.text_processing_pipeline(words, "")

        self.assertEqual(index, -1)
        self.assertEqual(mean_len, 6.0)

    def test_v3(self):
        words = ["Noon", "Civic", "Deified", "Rotor"]
        index, mean_len = integration_2.text_processing_pipeline(words, "civic")

        self.assertEqual(index, 0)
        self.assertEqual(mean_len, 5.25)

    def test_v4(self):
        words = ["abc", "def", "ghi"]
        index, mean_len = integration_2.text_processing_pipeline(words, "abc")

        self.assertEqual(index, -1)
        self.assertEqual(mean_len, 0.0)

    def test_v5(self):
        words = [None, "", "   "]
        index, mean_len = integration_2.text_processing_pipeline(words, "anyword")

        self.assertEqual(index, -1)
        self.assertEqual(mean_len, 1.0)


if __name__ == "__main__":
    unittest.main()
