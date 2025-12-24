from ..core.base_module import BaseModule
import random

class PerceptionModule(BaseModule):
    def __init__(self):
        super().__init__("Perception")
        self.detected_entities = []

    def update(self):
        # Simulate sensor scanning
        if random.random() > 0.7:
            entity = f"Bilinmeyen_Nesne_{random.randint(100, 999)}"
            self.detected_entities.append(entity)
            self.logger.info(f"Yeni varlık tespit edildi: {entity}")
        
        self.status = "TARIYOR"
        return self.detected_entities
