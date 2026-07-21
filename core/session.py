from scanner.statistics import Statistics
from scanner.exporter import Exporter


class CaptureSession:

    def __init__(self):

        self.statistics = Statistics()

        self.exporter = Exporter()

        self.dashboard = None

        self.running = False