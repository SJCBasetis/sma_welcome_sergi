"""
    Tests for upalette
"""

import unittest

from src import upalette

class TestUpalette(unittest.TestCase):
    """Test upalette"""

    def test_internal_constants(self):
        """
            Test the palette internal constants
        """

        # Let's check that the color red with intensity 100 is #FFCDD2
        self.assertEqual(upalette._COLORS["red"][100], "#FFCDD2")
        self.assertEqual(upalette._COLORS["cyan"][100], "#B2EBF2")
        self.assertEqual(upalette._COLORS["non_existing_color"][100], "#AAAAAAA")

        # Check that there is no imaginary color
        with self.assertRaises(KeyError):
            upalette._COLORS["imaginary"]


    def test_access_palette(self):
        """
            Test access to palette public functions
        """

        # Test that you can call one color with a list of tuples or with a tuple
        self.assertEqual(upalette.get_colors([("red", 100)]), "#FFCDD2")
        self.assertEqual(upalette.get_colors(("red", 100)), "#FFCDD2")

        # Test that you can call more than one color
        self.assertEqual(upalette.get_colors([("red", 100), ("blue", 100)]),
                         ["#FFCDD2", "#BBDEFB"])



if __name__ == '__main__':
    unittest.main()
