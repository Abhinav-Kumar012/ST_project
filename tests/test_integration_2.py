import unittest
from src import integration_2

class TestIntegration2(unittest.TestCase):
    def test_text_processing_pipeline(self):
        words = ["RaceCar", "Hello", "Level", "World", "Madam", "Python"]
        # 1. to_snake_case: ["race_car", "hello", "level", "world", "madam", "python"]
        # 2. is_palindrome: 
        #    - race_car: r-a-c-e-_-c-a-r -> racecar (palindrome logic ignores non-alnum) -> True
        #    - hello: False
        #    - level: True
        #    - world: False
        #    - madam: True
        #    - python: False
        # Palindromes: ["race_car", "level", "madam"]
        
        # 3. Sort: ["level", "madam", "race_car"]
        
        # 4. Search for "Madam" -> "madam"
        # Index should be 1
        
        # 5. Mean length:
        # level: 5
        # madam: 5
        # race_car: 8
        # Mean: (5+5+8)/3 = 6.0
        
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
    def  test_v4(self):
        words = ["abc", "def", "ghi"]
        index, mean_len = integration_2.text_processing_pipeline(words, "abc")
        
        self.assertEqual(index, -1)
        self.assertEqual(mean_len, 0.0)
    def test_v5(self):
        words = [None, "", "   "]
        index, mean_len = integration_2.text_processing_pipeline(words, "anyword")
        
        self.assertEqual(index, -1)
        self.assertEqual(mean_len, 1.0)

if __name__ == '__main__':
    unittest.main()
