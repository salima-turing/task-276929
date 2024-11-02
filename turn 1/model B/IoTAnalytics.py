# IoTAnalytics.py
class IoTAnalytics:
    def __init__(self):
        self.fault_tolerance_enabled = True

    def process_data_packet(self, data_packet):
        if self.fault_tolerance_enabled:
            # Simulate fault tolerance logic here
            if 'error' in data_packet:
                print(f"Error detected in packet: {data_packet['error']}")
                return

        # Perform analytics on the data packet
        print(f"Processing data packet: {data_packet}")
