import sys
import os
import logging
import time

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from aegis.perception.perception_module import PerceptionModule
from aegis.navigation.navigation_module import NavigationModule
from aegis.propulsion.propulsion_module import PropulsionModule

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%H:%M:%S'
)

class AegisOrchestrator:
    def __init__(self):
        self.logger = logging.getLogger("Aegis.Orchestrator")
        self.modules = {
            "perception": PerceptionModule(),
            "navigation": NavigationModule(),
            "propulsion": PropulsionModule()
        }

    def startup(self):
        self.logger.info("Aegis Systems Initializing...")
        for name, module in self.modules.items():
            module.setup()
        self.logger.info("All systems GO.")

    def run_cycle(self, duration=5):
        self.logger.info(f"Starting mission cycle for {duration} seconds...")
        start_time = time.time()
        while time.time() - start_time < duration:
            for name, module in self.modules.items():
                module.update()
            time.sleep(1)
        self.logger.info("Cycle complete.")

    def shutdown(self):
        for name, module in self.modules.items():
            module.shutdown()
        self.logger.info("Systems powered down.")

def main():
    orchestrator = AegisOrchestrator()
    try:
        orchestrator.startup()
        orchestrator.run_cycle()
    except KeyboardInterrupt:
        pass
    finally:
        orchestrator.shutdown()

if __name__ == "__main__":
    main()
