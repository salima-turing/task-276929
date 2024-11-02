# test_iot_analytics.py
import unittest
from unittest.mock import patch
from IoTAnalytics import IoTAnalytics

class TestIoTAnalytics(unittest.TestCase):

    @patch('IoTAnalytics.IoTAnalytics.process_data_packet')
    def test_fault_tolerance_with_error_packet(self, mock_process_data_packet):
        # Create an instance of IoTAnalytics
        analytics = IoTAnalytics()

        # Simulate a data packet with an error
        error_packet = {'error': 'Invalid data format'}

        # Call the process_data_packet method with the error packet
        analytics.process_data_packet(error_packet)

        # Assert that the mock method was called with the error packet
        mock_process_data_packet.assert_called_once_with(error_packet)

        # Optionally, you can check if the error message was printed as expected
        with self.assertLogs(level='INFO') as cm:
            analytics.process_data_packet(error_packet)
            self.assertIn("Error detected in packet: Invalid data format", cm.output[0])

if __name__ == '__main__':
    unittest.main()
