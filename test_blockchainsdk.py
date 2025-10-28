# test_blockchainsdk.py
"""
Tests for BlockchainSDK module.
"""

import unittest
from blockchainsdk import BlockchainSDK

class TestBlockchainSDK(unittest.TestCase):
    """Test cases for BlockchainSDK class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainSDK()
        self.assertIsInstance(instance, BlockchainSDK)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainSDK()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
