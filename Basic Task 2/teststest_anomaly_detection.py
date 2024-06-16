import unittest
from scripts.anomaly_detection import detect_anomalies

class TestAnomalyDetection(unittest.TestCase):
    
    def test_detection(self):
        data = [0.1, 0.2, 0.3, 0.4, 0.5]
        anomalies = detect_anomalies(data)
        self.assertEqual(anomalies, [2, 4])

if __name__ == '__main__':
    unittest.main()
