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
        self.status = "BAŞLATILIYOR"
        self._running = False

    def setup(self, config=None):
        self.logger.info(f"Modül kuruluyor: {self.name}")
        # Modüle özgü kurulum mantığı
        self.status = "HAZIR"

    @abstractmethod
    def update(self):
        """Modülün ana operasyonel döngüsü."""
        pass

    def shutdown(self):
        self.logger.info(f"Modül kapatılıyor: {self.name}")
        self._running = False
        self.status = "ÇEVRİMDIŞI"

    def get_health(self):
        return {
            "module": self.name,
            "status": self.status,
            "timestamp": time.time()
        }
