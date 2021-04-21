"""
    Tests for ulog
"""

import unittest

from src import ulog

class TestUlog(unittest.TestCase):
    """Test ulog"""

    def test_log(self):
        """
            Test that log works with all possible parameters
        """

        log = ulog.set_logger()

        # Test all logging levels
        log.error("Test error")
        log.warning("Test warning")

        try:
            1/0
        except Exception as e:
            log.error("Try errors", error=e)


    def test_fancy_string_time_from_seconds(self):
        """
            Test fancy_string_time_from_seconds
        """

        self.assertEqual(ulog.fancy_string_time_from_seconds(23), "23s")
        self.assertEqual(ulog.fancy_string_time_from_seconds(60), "1m")
        self.assertEqual(ulog.fancy_string_time_from_seconds(3600), "1h")
        
    def test_get_csv_file_handler(self):
        """
            Test get scv from file handeler
        """
        
        pass
        



if __name__ == '__main__':
    unittest.main()
