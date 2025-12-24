import sys
import os
import logging
import time

# src dizinini python yoluna ekle
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from aegis.perception.perception_module import PerceptionModule
from aegis.navigation.navigation_module import NavigationModule
from aegis.propulsion.propulsion_module import PropulsionModule

# Temel loglama yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%H:%M:%S'
)

class AegisOrkestrator:
    def __init__(self):
        self.logger = logging.getLogger("Aegis.Orkestrator")
        self.modules = {
            "perception": PerceptionModule(),
            "navigation": NavigationModule(),
            "propulsion": PropulsionModule()
        }

    def startup(self):
        self.logger.info("Aegis Sistemleri Başlatılıyor...")
        for name, module in self.modules.items():
            module.setup()
        self.logger.info("Tüm sistemler aktif.")

    def run_cycle(self, duration=5):
        self.logger.info(f"Görev döngüsü başlatılıyor, süre: {duration} saniye...")
        start_time = time.time()
        while time.time() - start_time < duration:
            for name, module in self.modules.items():
                module.update()
            time.sleep(1)
        self.logger.info("Döngü tamamlandı.")

    def shutdown(self):
        for name, module in self.modules.items():
            module.shutdown()
        self.logger.info("Sistemler kapatıldı.")

def main():
    orchestrator = AegisOrkestrator()
    try:
        orchestrator.startup()
        orchestrator.run_cycle()
    except KeyboardInterrupt:
        pass
    finally:
        orchestrator.shutdown()

if __name__ == "__main__":
    main()
