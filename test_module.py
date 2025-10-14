import matplotlib
matplotlib.use('Agg')  # non-GUI backend for testing
import unittest
import os
from sea_level_predictor import draw_plot

class SeaLevelTestCase(unittest.TestCase):
    def test_plot_creation(self):
        ax = draw_plot()
        # Check that file exists
        self.assertTrue(os.path.exists("sea_level_plot.png"))
        # Check axes labels
        self.assertEqual(ax.get_xlabel(), "Year")
        self.assertEqual(ax.get_ylabel(), "Sea Level (inches)")
        self.assertEqual(ax.get_title(), "Rise in Sea Level")
        # Check that there are 3 line artists (scatter + 2 regression lines)
        lines = ax.get_lines()
        # There should be two regression lines (scatter is not a line)
        self.assertGreaterEqual(len(lines), 2)

if __name__ == "__main__":
    unittest.main()
