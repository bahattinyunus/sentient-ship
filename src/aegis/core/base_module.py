from abc import ABC, abstractmethod
import logging
import time

class BaseModule(ABC):
    """
    Base class for all Sentient Ship modules.
    Ensures consistent lifecycle management across the Aegis system.
    """
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(f"Aegis.{name}")
        self.status = "INITIALIZING"
        self._running = False

    def setup(self, config=None):
        self.logger.info(f"Setting up module: {self.name}")
        # Module-specific setup logic
        self.status = "READY"

    @abstractmethod
    def update(self):
        """Main operational loop for the module."""
        pass

    def shutdown(self):
        self.logger.info(f"Shutting down module: {self.name}")
        self._running = False
        self.status = "OFFLINE"

    def get_health(self):
        return {
            "module": self.name,
            "status": self.status,
            "timestamp": time.time()
        }
