# test_discstate.py
"""
Tests for DiscState module.
"""

import unittest
from discstate import DiscState

class TestDiscState(unittest.TestCase):
    """Test cases for DiscState class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DiscState()
        self.assertIsInstance(instance, DiscState)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DiscState()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
