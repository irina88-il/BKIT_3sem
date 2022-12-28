import unittest

from lab_python_oop.color import color_figure

class TestColor_figure(unittest.TestCase):
    def setUp(self):
        self.color = color_figure()
    
    def test_get_color(self):
        self.assertEqual(self.color.get_color('красный'),'красный')
    
if __name__ == "__main__":
    unittest.main()
    
