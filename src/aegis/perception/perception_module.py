from ..core.base_module import BaseModule
import random

class PerceptionModule(BaseModule):
    def __init__(self):
        super().__init__("Perception")
        self.detected_entities = []

    def update(self):
        # Simulate sensor scanning
        if random.random() > 0.7:
            entity = f"Unknown_Object_{random.randint(100, 999)}"
            self.detected_entities.append(entity)
            self.logger.info(f"New entity detected: {entity}")
        
        self.status = "SCANNING"
        return self.detected_entities
