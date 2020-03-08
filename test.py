import unittest
from Analiza import *
import pandas as pd

class Test_Analizy(unittest.TestCase):

# Test przeprowadzany na małym zbiorze danych
    def setUp(self):
        self.d1 = pd.DataFrame({"A": ["o", "o", "u", "j", "u"], \
                           "B": [1, 1, 3, 2, 3]})

        self.d2 = pd.DataFrame({"C": ["ola", "jola", "ula"], \
                           "B": [1, 2, 3]})


    def test_merge(self):
        d_merge = merge(self.d2, self.d1, "B")

        for number, name in enumerate(d_merge["C"]):
            if name == "ola":
                self.assertEqual("o", d_merge["A"].iloc[number])
            else:
                self.assertNotEqual("o", d_merge["A"].iloc[number])


    def test_author_count(self):
        d_merge = merge(self.d2, self.d1, "B")
        d_list = author_count(d_merge["C"])

        good_list = ['ula napisała(a) 2 postów', 'ola napisała(a) 2 postów', 'jola napisała(a) 1 postów']
        self.assertEqual(d_list, good_list)


    def test_unique_titles(self):
        d_merge = merge(self.d2, self.d1, "B")
        unique = unique_titles(d_merge["C"])
        self.assertEqual(unique, ["ola", "ula"])

# Nowa klasa do testowania funkcji neighbour
class Test_Analizy2(unittest.TestCase):
    def setUp(self):
        self.data = pd.Series({"ola": {"geo": {"lat": 1, "lng": 1}}, \
            "jola" : {"geo": {"lat": 3, "lng": 2}}, \
            "ula" : {"geo": {"lat": 10, "lng": 1}}, \
            "jan" : {"geo": {"lat": 100, "lng": 1}}})

    def test_neighbour(self):
        result = neighbour(self.data)
        good_list = [1, 0, 1, 2]
        self.assertEqual(good_list, result)


if __name__ == '__main__':
    unittest.main()
