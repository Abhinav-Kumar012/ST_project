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

if __name__ == '__main__':
    unittest.main()
