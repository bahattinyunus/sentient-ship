import sys
import os
import logging
import time

# src dizinini python yoluna ekle
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from aegis.perception.perception_module import PerceptionModule
from aegis.navigation.navigation_module import NavigationModule
from aegis.propulsion.propulsion_module import PropulsionModule
from aegis.core.aegis_core import AegisCore

# Temel loglama yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%H:%M:%S'
)

class SefineOrkestrator:
    def __init__(self):
        self.logger = logging.getLogger("Sefine-i Şuûr")
        self.modules = {
            "kalp": AegisCore(),
            "basiret": PerceptionModule(),
            "seyr": NavigationModule(),
            "himmet": PropulsionModule()
        }

    def startup(self):
        self.logger.info("﷽ BİSMİLLAHİRRAHMANİRRAHİM - Sistemler Uyanıyor...")
        for name, module in self.modules.items():
            module.setup()
        self.logger.info("Tüm latifeler zikre başladı (Active).")

    def run_cycle(self, duration=10):
        self.logger.info(f"Vira Bismillah! Sefer başlıyor ({duration} saniye)...")
        
        # Örnek bir niyet (Rota) belirleyelim
        self.modules["seyr"].niyet_et([10, 10, 10])
        # Biraz cezbe verelim
        self.modules["himmet"].cezbe_katsayisi = 2
        
        start_time = time.time()
        while time.time() - start_time < duration:
            self.logger.debug("--- Anlık Murakabe ---")
            for name, module in self.modules.items():
                module.update()
            time.sleep(1.5) # Tefekkür süresi
            
        self.logger.info("Sefer tamamlandı. Elhamdulillah.")

    def shutdown(self):
        for name, module in self.modules.items():
            module.shutdown()
        self.logger.info("Sistemler istirahate çekildi.")

def main():
    orchestrator = SefineOrkestrator()
    try:
        orchestrator.startup()
        orchestrator.run_cycle()
    except KeyboardInterrupt:
        pass
    finally:
        orchestrator.shutdown()

if __name__ == "__main__":
    main()
