import unittest
from unittest.mock import Mock, patch
import random


# Function to be tested
def process_data_packet(data_packet, analytics_engine):
    try:
        analytics_engine.process(data_packet)
        return "Data packet processed successfully"
    except Exception as e:
        return f"Error processing data packet: {e}"


class TestIoTAnalyticsFaultTolerance(unittest.TestCase):

    @patch('__main__.AnalyticsEngine')
    def test_fault_tolerance_to_data_packet_loss(self, MockAnalyticsEngine):
        analytics_engine = MockAnalyticsEngine()

        # Simulate data packet loss by making process method raise an exception
        analytics_engine.process.side_effect = Exception("Data packet lost")

        test_data_packet = {"sensor_data": 42}

        result = process_data_packet(test_data_packet, analytics_engine)

        self.assertEqual(result, "Error processing data packet: Data packet lost")

        analytics_engine.process.assert_called_once_with(test_data_packet)


if __name__ == '__main__':
    unittest.main()
